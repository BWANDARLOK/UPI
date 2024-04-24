from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, CHANNEL_USERNAME

app = Client("my_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("show_buttons"))
def show_buttons(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")]
    ])
    message.reply_text("Here are the buttons:", reply_markup=keyboard)

if __name__ == "__main__":
    app.run()
  
