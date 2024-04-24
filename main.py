from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, CHANNEL_USERNAME

app = Client("my_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")]
    ])
    message.reply_text("Welcome to the bot!", reply_markup=keyboard)

@app.on_message(filters.chat(CHANNEL_USERNAME) & filters.incoming)
def channel_join_check(client, message):
    if message.from_user and not client.get_chat_member(CHANNEL_USERNAME, message.from_user.id).user.is_member:
        message.reply_text("Please join the channel to use this bot.")

@app.on_callback_query()
def button_click(client, callback_query):
    if callback_query.data == "join_channel":
        if not client.get_chat_member(CHANNEL_USERNAME, callback_query.from_user.id).user.is_member:
            callback_query.answer("Please join the channel first.", show_alert=True)
        else:
            callback_query.answer("You have successfully joined the channel!")

if __name__ == "__main__":
    app.run()
                                      
