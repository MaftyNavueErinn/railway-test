from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text('봇 가동 완료. 섹스킹 마스터님👑')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
