from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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

WELCOME_TEXT: MarkdownV2Text = MarkdownV2Text("""
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
""")

WELCOME_TEXT_MARKUP: InlineKeyboardMarkup = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text = "Вступить в разработку", url = "https://t.me/+Syx_PZhJ5rVlODEy")
)