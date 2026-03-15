from telebot import TeleBot
from telebot.types import Message

context: TeleBot = TeleBot("8738837682:AAHRka74Olp0_dCqG9btSyktThkn79yjr8Y")

@context.message_handler (
	commands = ['start', 'help']
)
def handle_start_message(message : Message) -> None:
	context.send_message(chat_id = message.chat.id, text = "Howdy, how are you doing?")

if __name__ == "__main__": context.infinity_polling()