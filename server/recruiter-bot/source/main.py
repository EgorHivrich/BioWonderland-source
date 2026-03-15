from telebot import TeleBot
from telebot.types import Message

from config import *

context: TeleBot = TeleBot("8738837682:AAHRka74Olp0_dCqG9btSyktThkn79yjr8Y")

@context.message_handler (
	commands = ['start', 'help']
)
def handle_start_message(message : Message) -> None:
	context.send_message(message.chat.id, WELCOME_TEXT.fixed, reply_markup = WELCOME_TEXT_MARKUP)

if __name__ == "__main__": context.infinity_polling()