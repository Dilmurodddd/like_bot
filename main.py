from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from telegram.ext import Updater
import os
likes = 0
dislikes = 0

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum\nmen faqat like va deslikeni sanaydigan botman\nmenga faqat like va deslike emojisini yuboring\nfaqat bir dona yuboring")
def handle_message(update: Updater, context: CallbackContext):
    global likes, dislikes
    if update.message.text in "👍👍🏻👍🏼👍🏽👍🏾👍🏿":
        likes += 1
        update.message.reply_text(f"Like: {likes}\n"f"Dislike: {dislikes}")
        
    elif update.message.text in "👎👎🏻👎🏼👎🏽👎🏾👎🏿":
        dislikes += 1
        update.message.reply_text(f"Like: {likes}\n"f"Dislike: {dislikes}")
        
    else:
        update.message.reply_text("Ming bora uzur so'rayman menga faqat 👎👎🏻👎🏼👎🏽👎🏾👎🏿 va 👍👍🏻👍🏼👍🏽👍🏾👍🏿 emojilarni qabul qilaman")
def main():
    TOKEN = os.getenv("TOKEN")  
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main() 