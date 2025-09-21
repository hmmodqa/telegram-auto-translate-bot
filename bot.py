import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from googletrans import Translator

TOKEN = os.getenv("7458639531:AAG-Rc5Jzux0AEtBPM5_E9xqD48KpVMnjkg")
translator = Translator()

async def auto_translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if not text:
        return
    
    detected = translator.detect(text).lang
    if detected != "ar":
        translated = translator.translate(text, dest="ar").text
        await update.message.reply_text(translated)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_translate))
    app.run_polling()

if __name__ == "__main__":
    main()
