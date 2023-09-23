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

    arguments = sys.argv
    chat_mode_flag = "long"
    chat_mode_factory = ChatModeFactory()
    response_strategy = chat_mode_factory.get_chat_mode(chat_mode_flag)
    shell = Shell(response_strategy)
    shell.repl()
