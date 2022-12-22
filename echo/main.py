from subprocess import Popen, PIPE

from telegram import Bot, Update
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

from config import load_config


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Привет, жду сообщения!"
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Учебный бот.\n Вся информация есть в меню."
    )


def do_time(bot: Bot, update: Update):
    process = Popen(["date"], stdout=PIPE)
    text, error = process.communicate()
    if error:
        text = "Произошла ошибка, время неизвестно!"
    else:
        text = text.decode("utf-8")

    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )



def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Ваш ID = {} \n\n{}".format(chat_id, update.message.text)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )


def main():
    config = load_config()
    bot = Bot(
        token=config.TG_TOKEN,
    )
    updater =Updater(
        bot=bot,
    )

    start_handler = CommandHandler("start",do_start)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    massage_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(massage_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


