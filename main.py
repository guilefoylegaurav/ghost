from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import ShellTool
from dotenv import find_dotenv, load_dotenv
import warnings
warnings.filterwarnings("ignore")
load_dotenv(find_dotenv())
from langchain.callbacks import HumanApprovalCallbackHandler

def _should_check(serialized_obj: dict) -> bool:
    # Only require approval on ShellTool.
    return serialized_obj.get("name") == "terminal"


def _approve(_input: str) -> bool:
    if _input == "echo 'Hello World'":
        return True
    msg = (
        "Approve (y\Y)?"
    )
    msg += "\n\n" + _input + "\n"
    resp = input(msg)
    return resp.lower() in ("yes", "y")


callbacks = [HumanApprovalCallbackHandler(should_check=_should_check, approve=_approve)]

shell_tool = ShellTool(callbacks=callbacks)
llm = ChatOpenAI(temperature=0)

shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
    "{", "{{"
).replace("}", "}}")

self_ask_with_search = initialize_agent(
    [shell_tool], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

print(self_ask_with_search.run(
    "List all processes running in port 3010"
))