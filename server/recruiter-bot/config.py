from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

WELCOME_TEXT: str = """
Привет! Сейчас мы находимся в поисках разработкиков для нашего проекта BioWonderland.

**Кого мы берём в наш проект?**
    • Программистов
    • 3D моделеров, аниматоров
    • Композиторов
    • Сценаристов и актёров озвучки

Если ты умеешь что-то из этого списка, то мы будем тебе рады.
Дополнительная информация: /info
"""

WELCOME_TEXT_MARKUP: InlineKeyboardMarkup = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text = "Вступить в разработку", url = "https://t.me/+Syx_PZhJ5rVlODEy")
)