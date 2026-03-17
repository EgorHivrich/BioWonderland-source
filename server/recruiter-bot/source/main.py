from telebot import TeleBot
from config import Config, MarkdownV2Text, JsonConfigDeserializer

from telebot.types import InlineKeyboardMarkup, Message

class ConfigDeserializer:
    
	@staticmethod
	def deserialize(filePath: str,
				   decoder: object
	) -> Config:

		with open(filePath, "r+") as file:
			deserializedConfig: Config = decoder.decode(file.read())

		return deserializedConfig

config: Config = ConfigDeserializer.deserialize("../config.json", JsonConfigDeserializer())
context: TeleBot = TeleBot(config.token)

def send_callback_on_message(message: Message, id: int) -> None:

	print(message.text)
	callback: list[MarkdownV2Text, InlineKeyboardMarkup] = None

	for command in config.objects.keys():
		if message.text.removesuffix(" ") == command: callback = config.objects[command]; break

	context.send_message(message.chat.id, MarkdownV2Text(callback[0]).fixed, "MarkdownV2", reply_markup = callback[1])


@context.message_handler (
	func = lambda message: True
)
def handle_text_messages(message: Message) -> None:
	send_callback_on_message(message, message.chat.id)


@context.callback_query_handler (
	func = lambda message: True
)
def handle_questions(message: Message) -> None:
	send_callback_on_message(message, message.from_user.id)

if __name__ == "__main__": context.infinity_polling()