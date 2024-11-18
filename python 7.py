import ptbot
import os
from telegram import message
from pytimeparse import parse
from dotenv import load_dotenv


def reply(chat_id, text):
    message_id = bot.send_message(chat_id, text)
    bot.create_countdown(parse(text), notify, chat_id=chat_id, message_id=message_id, text=text)
    bot.create_timer(parse(text), final_notify, chat_id=chat_id)


def notify(secs_left, chat_id, message_id, text):
    counter = parse(text) - secs_left
    bot.update_message(chat_id, message_id, f"Осталось {secs_left} секунд!\n{render_progressbar(parse(text), counter)}")


def final_notify(chat_id):
    bot.send_message(chat_id, "Время вышло!")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    bot = ptbot.Bot(token)
    bot.reply_on_message(reply)
    bot.run_bot()
