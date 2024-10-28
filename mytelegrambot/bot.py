from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Salom!')

async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    # ApplicationBuilder orqali Application yaratamiz
    application = ApplicationBuilder().token("7726165015:AAFez1wYx5PPCYagT5UDl7pcRDQnuzqmuZs").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == '__main__':
    main()



