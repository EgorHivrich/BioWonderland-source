from telebot import TeleBot
from telebot.types import Message

from config import *

context: TeleBot = TeleBot(CONFIG.token)

@context.message_handler (
	func = lambda message: True
)
def handle_text_messages(message: Message) -> None:
	print(message.text)
	callback: list[MarkdownV2Text, InlineKeyboardMarkup] = None

	for command in CONFIG.objects.keys():
		if message.text.removesuffix(" ") == command: callback = CONFIG.objects[command]; break

	context.send_message(message.chat.id, callback[0].fixed, "MarkdownV2", reply_markup = callback[1])


@context.callback_query_handler (
	func = lambda message: True
)
def handle_questions(message: Message) -> None:
	print(message.data, "Hello world")
	context.send_message(message.from_user.id, QUESTIONS_ANSWERS[message.data].fixed, "MarkdownV2")


if __name__ == "__main__": context.infinity_polling()