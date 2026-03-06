import asyncio
from env import MastermindEnvironment, GuessCodeParams


async def test_locally():
    """Test the environment directly without going through the server"""

    # Get tasks
    tasks = MastermindEnvironment.list_tasks(split="test")
    print(f"Found {len(tasks)} tasks")

    example_task = tasks[0]
    print(f"Testing task: {example_task['id']}")

    # Create environment instance
    env_instance = MastermindEnvironment(task_spec=example_task, secrets={})

    # Test prompt generation
    prompt = await env_instance.get_prompt()
    print(f"\n=== PROMPT ===")
    print(prompt[0].text)

    # Test tool call with guess_code
    print(f"\n=== GUESS CODE: '1 2 3 4' ===")
    params = GuessCodeParams(code="1 2 3 4")
    result = await env_instance.guess_code(params)
    print(f"Output: {result.blocks[0].text}")
    print(f"Reward: {result.reward}")
    print(f"Finished: {result.finished}")
    print(f"Metadata: {result.metadata}")

    # If not finished, try another guess
    if not result.finished:
        print(f"\n=== GUESS CODE: '5 6 1 2' ===")
        params = GuessCodeParams(code="5 6 1 2")
        result = await env_instance.guess_code(params)
        print(f"Output: {result.blocks[0].text}")
        print(f"Reward: {result.reward}")
        print(f"Finished: {result.finished}")

    print("\n=== TEST PASSED ===")


if __name__ == "__main__":
    asyncio.run(test_locally())
