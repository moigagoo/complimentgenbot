from os import getenv
from random import choice

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler


OBJECTS = ["твои глаза", "твои ноги", "твоя фигура",
           "твои волосы", "твои руки", "твои губы", "твой голос", ]
COMPARISONS = ["закат", "рассвет", "солнечный свет", "лунный свет",
               "небо", "облака", "волны", "метель", "снег", "солнечный зайчик", "роса", "бриз", "дуновение ветра", "шум прибоя",]
LOCATIONS = ["в пустыне", "в океане", "в лавандовом поле", "среди звёзд",
             "на небесах", "в бескрайнем космосе", "в густой траве", "на снегу", "в росе", "в облаках",]
EMOJIS = ["😍", "🥰", "😚", "💌", "😻", "💘"]


def generate_compliment() -> str:
    return f"{choice(OBJECTS).capitalize()}... как {choice(COMPARISONS)} {choice(LOCATIONS)} {choice(EMOJIS)}"


def compliment(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(generate_compliment())


if __name__ == "__main__":
    load_dotenv()

    updater = Updater(getenv("TELEGRAM_BOT_TOKEN"))

    updater.bot.set_my_commands(
        [
            BotCommand("/compliment", "Сделать комплимент 💌")
        ]
    )

    updater.dispatcher.add_handler(CommandHandler("start", compliment))
    updater.dispatcher.add_handler(CommandHandler("compliment", compliment))

    updater.start_polling()
    updater.idle()

