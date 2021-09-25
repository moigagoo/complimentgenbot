from os import getenv
from random import choice

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler


OBJECTS = ["твои глаза", "твои ноги", "твоя фигура",
           "твои волосы", "твои руки", "твои губы", "твой голос", ]
COMPARISONS = ["закат", "рассвет", "солнечный свет", "лунный свет",
               "небо", "облака", "волны", "метель", "снег", "солнечный зайчик"]
LOCATIONS = ["в Бомбее", "посреди океана", "в широком поле", "среди звёзд",
             "на небесах", "в космосе", "в бескрайней тьме", "в траве", ]
EMOJIS = ["😍", "🥰", "😚", "💌", "😻", "💘"]
COMPLIMENT_COMMAND = "compliment"


def generate_compliment() -> str:
    return f"{choice(OBJECTS).capitalize()}... как {choice(COMPARISONS)} {choice(LOCATIONS)} {choice(EMOJIS)}"


def get_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Другой", callback_data=COMPLIMENT_COMMAND)
            ]
        ]
    )


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(generate_compliment(),
                              reply_markup=get_keyboard())


def compliment(update: Update, context: CallbackContext) -> None:
    update.callback_query.answer("Готово!")

    if update.callback_query.data == COMPLIMENT_COMMAND:
        update.callback_query.edit_message_text(
            generate_compliment(), reply_markup=get_keyboard())

    else:
        update.callback_query.answer("А?")


if __name__ == "__main__":
    load_dotenv()

    updater = Updater(getenv("TELEGRAM_BOT_TOKEN"))

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(compliment))

    updater.start_polling()
    updater.idle()

