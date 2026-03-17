from telebot.types import (JsonSerializable,
                          JsonDeserializable)
from dataclasses import dataclass, field

class MarkdownV2Text:

    def __init__(self,
                string: str
    ) -> None:
        
        for character in string:
            if character in self._RESERVED: self._fixed += "\\"
            self._fixed += character

        print(f"fixed string: {self.fixed}")

    @property
    def fixed(self) -> str: return self._fixed

    _fixed: str = ""
    _RESERVED: list[str] = ['.', ',', '!', '-']

@dataclass
class Config(JsonSerializable, JsonDeserializable):
    token: str = ""
    objects: dict[str, list[object]] = field(default_factory = list)