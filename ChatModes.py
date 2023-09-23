import os
import sys


class ChatMode:
    def respond(self, agent) -> None:
        pass


class ShortChatMode(ChatMode):

    def respond(self, agent) -> None:
        try:
            print(agent.run(sys.argv[1]))
        except Exception as e:
            print(e.args[0].split(':', 1)[-1].strip())


class ProlongedChatMode(ChatMode):
    def respond(self, agent) -> None:
        while True:
            question = input(">")
            if question == "exit":
                return
            try:
                print(agent.run(question))
            except Exception as e:
                print(e.args[0].split(':', 1)[-1].strip())
