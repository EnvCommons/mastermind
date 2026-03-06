from openreward.environments import Server
from env import MastermindEnvironment

if __name__ == "__main__":
    server = Server([MastermindEnvironment])
    server.run()
