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

[MIT](https://github.com/LeonGuertler/TextArena/blob/main/LICENSE).

## Tasks

There are two splits: train (450 tasks) and test (450 tasks). Each split contains 50 tasks across each of 9 variants:

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

This is a sparse reward environment. Rewards are mapped from TextArena's native range of {-1, 0, 1} to {0.0, 0.5, 1.0} via `(raw + 1) / 2`.

We do not use LLM graders for this environment; reward is determined programmatically.

## Data

Game state is generated procedurally by the TextArena engine using seeded randomness. No external data files are required.

## Tools

Agents are given a single tool:

- `guess_code(code)`: Submit a code guess as space-separated numbers (e.g. '1 2 3 4'). You'll receive feedback on correct positions and correct digits.

## Time Horizon

Mastermind is a multi-turn environment.

## Environment Difficulty

This environment ranges from moderate to very challenging depending on the variant. The hard and extreme variants significantly increase difficulty with longer codes and more possible values.

## Other Environment Requirements

There are no further environment requirements; Mastermind works out of the box without any secrets or API keys.

## Safety

Agents in Mastermind interact only with a code-breaking game and have no access to external systems, the internet, or sensitive data. The environment does not present safety risks.

## Citations

```bibtex
@software{textarena2024,
  author    = {Guertler, Leon and Banting, Wilfried and Pignatelli, Eduardo},
  title     = {TextArena},
  year      = {2024},
  publisher = {GitHub},
  url       = {https://github.com/LeonGuertler/TextArena}
}
```
