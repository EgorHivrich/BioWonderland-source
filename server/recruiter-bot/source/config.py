from telebot.types import (InlineKeyboardMarkup,
                          InlineKeyboardButton,
                          JsonSerializable, JsonDeserializable)
from dataclasses import dataclass, field
from json import dumps, loads

TOKEN: str = "8738837682:AAHRka74Olp0_dCqG9btSyktThkn79yjr8Y"

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
    _RESERVED = ['.', ',', '!', '-']

@dataclass
class Config(JsonSerializable, JsonDeserializable):
    token: str = ""
    objects: dict[str, list[object]] = field(default_factory = list)


CONFIG: Config = Config (
    token = TOKEN,
    objects = {
        "/start": [MarkdownV2Text("""
*Привет 👋✨*
Сейчас мы находимся в поисках разработчиков для нашего проекта DreamToy Fabric. 🌌🧬

> *👇 Кого мы берём в наш проект?*
>
>   • Программистов 💻👨‍💻
>   • 3D‑моделлеров, аниматоров 🖥️🎬
>   • Композиторов 🎵
>   • Сценаристов и актёров озвучки 📜🎤

Если ты умеешь что‑то из этого списка, то мы будем тебе рады! 
🔎 __Дополнительная информация:__ /info 
"""), InlineKeyboardMarkup().add( InlineKeyboardButton(text = "Вступить в разработку", url = "https://t.me/+Syx_PZhJ5rVlODEy") )],

        "/info": [MarkdownV2Text("""Выберите вопрос для обсуждения ✨"""),
                InlineKeyboardMarkup(row_width = 1).add( InlineKeyboardButton("Зарплата", callback_data = "0"), InlineKeyboardButton("Если у меня мало опыта", callback_data = "1") ) ]
    }
)

QUESTIONS_ANSWERS: dict[str, MarkdownV2Text] = {
    "0": MarkdownV2Text("""
*Answer* 📜
> Зарплаты пока нет, пока. Но если с игрой всё будет в порядке и она выстрелит, то появятся и деньги, зарплата соответственное тоже.
*Cheers lads 🍺🐪*
"""),

    "1": MarkdownV2Text("""
*Answer* 📜
> Новичёк в разработке игр? Если ты умеешь хоть что-то, то ты нам уже подходишь, на вступление ограничений почти нет.
*Cheers lads 🍺🐪*
""")
}