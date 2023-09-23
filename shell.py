from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import ShellTool
from langchain.callbacks import HumanApprovalCallbackHandler
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from dotenv import find_dotenv, load_dotenv
from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.utilities import GoogleSearchAPIWrapper
import warnings

warnings.filterwarnings("ignore")
load_dotenv(find_dotenv())


def _get_agent():
    llm = ChatOpenAI(callbacks=[StreamingStdOutCallbackHandler()], temperature=0.5)

    def _approve(_input: str) -> bool:
        tokens = _input.split(' ')
        if len(tokens) > 0 and tokens[0] == 'echo':
            return True
        msg = (
            "Approve (y/Y)?"
        )
        msg += "\n\n" + _input + "\n"
        resp = input(msg)
        return resp.lower() in ("yes", "y")

    callbacks = [HumanApprovalCallbackHandler(approve=_approve)]
    shell_tool = ShellTool(callbacks=callbacks, handle_tool_error=True)
    shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
        "{", "{{"
    ).replace("}", "}}")

    return initialize_agent(
        [shell_tool], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=False
    )


class Shell:
    def __init__(self, response_strategy) -> None:
        self.agent = _get_agent()
        self.response_strategy = response_strategy

    def repl(self):
        self.response_strategy.respond(self.agent)
