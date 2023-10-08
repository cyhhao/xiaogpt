from __future__ import annotations

from xiaogpt.bot.base_bot import BaseBot
from xiaogpt.bot.chatgptapi_bot import ChatGPTBot
from xiaogpt.config import Config

BOTS: dict[str, type[BaseBot]] = {
    "chatgptapi": ChatGPTBot,
}


def get_bot(config: Config) -> BaseBot:
    try:
        return BOTS[config.bot].from_config(config)
    except KeyError:
        raise ValueError(f"Unsupported bot {config.bot}, must be one of {list(BOTS)}")


__all__ = [ "ChatGPTBot", "get_bot"]
