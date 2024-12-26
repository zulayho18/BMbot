from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers import start_func, message_handler, inline_messages

token = "7966288738:AAFXn_sUf0vnfg8vqCplHRvkFZ-5hPglFQs"


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_messages))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()