import os


class ChatMode:
    def respond(self, agent) -> None:
        pass


class ShortChatMode(ChatMode):

    def respond(self, agent) -> None:
        agent.run({"question": self.question, "shell_name": os.environ.get["SHELL_NAME"],
                   "os_name": os.environ.get["OS_NAME"]})


class ProlongedChatMode(ChatMode):
    def respond(self, agent) -> None:
        while True:
            question = input(">")
            try:
                print(agent.run(question))
            except Exception as e:
                print(e.args[0].split(':', 1)[-1].strip())
