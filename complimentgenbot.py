from os import getenv
from random import choice

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler


OBJECTS = {
    "eyes": "твои глаза",
    "legs": "твои ноги",
    "figure": "твоя фигура",
    "hair": "твои волосы",
    "hands": "твои руки",
    "lips": "твои губы",
    "voice": "твой голос",
}
COMPARISONS = ["закат", "рассвет", "солнечный свет", "лунный свет",
               "небо", "облака", "волны", "метель", "снег", "солнечный зайчик", "роса", "бриз", "дуновение ветра", "шум прибоя",]
LOCATIONS = ["в пустыне", "в океане", "в лавандовом поле", "среди звёзд",
             "на небесах", "в бескрайнем космосе", "в густой траве", "на снегу", "в росе", "в облаках",]
EMOJIS = ["😍", "🥰", "😚", "💌", "😻", "💘"]


def generate_compliment(about: str) -> str:
    if about == "random":
        about = choice(list(OBJECTS.keys()))

    return f"{OBJECTS[about].capitalize()}... как {choice(COMPARISONS)} {choice(LOCATIONS)} {choice(EMOJIS)}"


def get_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("глаза", callback_data="eyes"),
                InlineKeyboardButton("губы", callback_data="lips"),
                InlineKeyboardButton("голос", callback_data="voice"),
                InlineKeyboardButton("волосы", callback_data="hair"),
            ],
            [
                InlineKeyboardButton("руки", callback_data="hands"),
                InlineKeyboardButton("ноги", callback_data="legs"),
                InlineKeyboardButton("фигуру", callback_data="figure"),
            ],
            [
                InlineKeyboardButton("что угодно", callback_data="random"),
            ]
        ]
    )


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Сгенерировать комплимент про...",
        reply_markup=get_keyboard()
    )


def handle_queries(update: Update, context: CallbackContext) -> None:
    update.callback_query.message.reply_text(
        f"""{generate_compliment(update.callback_query.data)}

Сгенерировать комплимент про...""",
        reply_markup=get_keyboard()
    )


if __name__ == "__main__":
    load_dotenv()

    updater = Updater(getenv("TELEGRAM_BOT_TOKEN"))

    updater.bot.set_my_commands(
        [
            BotCommand("/start", "Сделать комплимент 💌")
        ]
    )

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(handle_queries))

    updater.start_polling()
    updater.idle()

