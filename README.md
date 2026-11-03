# Mastermind

[![OpenReward Environment](https://img.shields.io/badge/%E2%AD%90%20OpenReward-Environment-f7e6cc)](https://openreward.ai/GeneralReasoning/Mastermind)

## Description

**Mastermind** is an environment for evaluating agents on code-breaking and deductive reasoning with feedback. This environment wraps the Mastermind implementation from [TextArena](https://github.com/LeonGuertler/TextArena), a framework for text-based game environments.

## Capabilities

- Deductive reasoning from feedback signals
- Strategic hypothesis generation and testing
- Pattern elimination and constraint satisfaction
- Information-theoretic reasoning under uncertainty

## Compute Requirements

Mastermind does not require a sandbox. It has minimal compute requirements.

## License

[MIT](https://opensource.org/licenses/MIT). The underlying [TextArena](https://github.com/LeonGuertler/TextArena) framework is also MIT.

## Tasks

There are 450 tasks in the `train` split and 450 in `test`. Each split contains 50 tasks across each of 9 variants:

- **Mastermind-v0**
- **Mastermind-v0-train**
- **Mastermind-v0-raw**
- **Mastermind-v0-hard**
- **Mastermind-v0-hard-train**
- **Mastermind-v0-hard-raw**
- **Mastermind-v0-extreme**
- **Mastermind-v0-extreme-train**
- **Mastermind-v0-extreme-raw**

Each task is seeded for reproducibility.

## Reward Structure

This is a sparse reward environment. TextArena's Mastermind reward is already in `[0.0, 1.0]` and is passed through unchanged: cracking the code scores `1.0`, and every other terminal outcome (turn limit or an invalid guess) scores a partial-credit fraction, `(black + 0.5 * white) / code_length` from the final guess. Intermediate guesses score `0.0`.

We do not use LLM graders for this environment; reward is determined programmatically.

## Data

Game state is generated procedurally by the TextArena engine using seeded randomness. No external data files are required.

## Tools

Agents are given a single tool:

- `guess_code(code)`: Submit a code guess as space-separated numbers (e.g. '1 2 3 4'). You'll receive feedback on correct positions and correct digits.

## Time Horizon

Mastermind is a multi-turn environment.

## Environment Difficulty

Difficulty depends on the variant. In TextArena's registration the base `Mastermind-v0` variants use a 4-digit code over 6 values with no repeats and 20 turns, hard uses a 4-digit code over 8 values with 30 turns, and extreme uses a 6-digit code over 12 values with repeats allowed and 50 turns. The `-train` and `-raw` suffixes change only the observation wrappers, not the game.

## Other Environment Requirements

There are no further environment requirements; Mastermind works out of the box without any secrets or API keys.

## Safety

Agents in Mastermind interact only with a code-breaking game and have no access to external systems, the internet, or sensitive data. The environment does not present safety risks.

## Citations

```bibtex
@misc{guertler2025textarena,
    title={TextArena},
    author={Leon Guertler and Bobby Cheng and Simon Yu and Bo Liu and Leshem Choshen and Cheston Tan},
    year={2025},
    eprint={2504.11442},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2504.11442},
}
```
