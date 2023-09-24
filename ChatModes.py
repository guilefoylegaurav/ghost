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
        print(
            "Hello! I am ghost, a command line utility that lets you communicate with your terminal and get tasks "
            "done USING NATURAL LANGUAGE!")
        print("What do you want me to do?")
        while True:
            question = input(">")
            if question == "exit":
                return
            try:
                print(agent.run(input=question))
            except Exception as e:
                print(e.args[0].split(':', 1)[-1].strip())
