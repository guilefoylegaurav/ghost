import platform
import distro
import os
import sys

from ChatModeFactory import ChatModeFactory
from shell import Shell

if __name__ == "__main__":
    os_name = platform.system()
    if os_name == 'Windows':
        os.environ["OS_NAME"] = 'Windows'
    elif os_name == 'Darwin':
        os.environ["OS_NAME"] = 'Apple macOS'
    elif os_name == 'Linux':
        os.environ["OS_NAME"] = distro.name(pretty=True)
    else:
        os.environ["OS_NAME"] = 'Linux'

    if os.name == 'nt':
        os.environ["SHELL_NAME"] = os.environ.get('COMSPEC', 'Unknown shell')
    elif os.name == 'posix':
        os.environ["SHELL_NAME"] = os.environ.get('SHELL', 'Unknown shell')
    else:
        os.environ["SHELL_NAME"] = 'Bash'

    PROMPT_TEMPLATE = """If someone asks you to perform a task, your job is to come up with a series of shell 
    commands that will perform the task. Ensure the commands are for the OS {os_name} and the shell {shell_name} Make 
    sure to reason step by step, using this format: Question: "copy the files in the directory named 'target' into a 
    new directory at the same level as target called 'myNewDirectory'" I need to take the following actions: - List 
    all files in the directory - Create a new directory - Copy the files from the first directory into the second 
    directory ```ComPmand: ls mkdir myNewDirectory cp -r target/* myNewDirectory ``` That is the format. Begin! {
    chat_history} Question: {question}"""

    arguments = sys.argv
    chat_mode_flag = "long"
    chat_mode_factory = ChatModeFactory()
    response_strategy = chat_mode_factory.get_chat_mode(chat_mode_flag)
    shell = Shell(response_strategy)
    shell.repl()
