import asyncio
import json
import os
from openai import AsyncOpenAI
from openreward import OpenReward


async def test_with_openai():
    or_client = OpenReward()
    oai_client = AsyncOpenAI()

    MODEL_NAME = "gpt-5.2"
    ENV_NAME = "mastermindenvironment"
    SPLIT = "test"

    environment = or_client.environments.get(name=ENV_NAME, base_url="http://localhost:8080")
    tasks = await environment.list_tasks(split=SPLIT)

    # Define tool schema manually
    tools = [{
        "type": "function",
        "name": "guess_code",
        "description": "Submit a code guess as space-separated numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Space-separated numbers, e.g. '1 2 3 4'"
                }
            },
            "required": ["code"],
            "additionalProperties": False
        }
    }]

    print(f"Found {len(tasks)} tasks")

    for task in tasks[:1]:  # Test first task
        print(f"\nTesting task: {task['id']}")

        async with environment.session(task=task) as session:
            prompt = await session.get_prompt()
            input_list = [{"role": "user", "content": prompt[0].text}]
            finished = False
            max_turns = 20

            turn = 0
            while not finished and turn < max_turns:
                turn += 1
                print(f"\n--- Turn {turn} ---")

                # Use responses.create(), NOT chat.completions.create()
                response = await oai_client.responses.create(
                    model=MODEL_NAME,
                    tools=tools,
                    input=input_list
                )

                # Response has 'output', NOT 'choices'
                input_list += response.output

                for item in response.output:
                    if item.type == "function_call":
                        print(f"Tool: {item.name}")
                        print(f"Arguments: {item.arguments}")

                        tool_result = await session.call_tool(
                            item.name,
                            json.loads(str(item.arguments))
                        )

                        finished = tool_result.finished

                        input_list.append({
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": tool_result.blocks[0].text
                        })

                        print(f"Reward: {tool_result.reward:.3f}")
                        print(f"Output: {tool_result.blocks[0].text}")

                        if tool_result.finished:
                            print('\nFINISHED!')
                            break

            if not finished:
                print(f"\nReached max turns ({max_turns}) without finishing")


if __name__ == "__main__":
    asyncio.run(test_with_openai())
