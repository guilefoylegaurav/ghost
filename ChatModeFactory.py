from ChatModes import ShortChatMode, ProlongedChatMode


class ChatModeFactory:
    def get_chat_mode(self, mode, seed=''):
        if mode == "short":
            return ShortChatMode()
        if mode == "long":
            return ProlongedChatMode()
