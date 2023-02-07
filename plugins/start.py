import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command('start'))
async def start(bot, message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/c00e382dd811616cdaa56.jpg",
        caption="Bu bot ile güncel Dolar, Euro, Altın, Bitcoin, Ethereum bilgisini alabilirsin.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Beni Oluşturan", url="https://t.me/mmagneto")]]))
