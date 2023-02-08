# Coded by :d
import pyrogram
import math
from pyrogram import Client, filters
from unidecode import unidecode

dovizurl = "https://api.genelpara.com/embed/doviz.json"


@Client.on_message(filters.command('doviz'))
async def dovizcek(bot, message):
    try:
        msg = unidecode(message.text).lower().split()
        doviz = yer[1]
        sayi = yer[2] 
        distek = requests.get(dovizurl)
        dveri = distek.json()
        kur = dveri[doviz]
        fiyat = kur * sayi
        message.reply_text(f"{sayi} {doviz} = {fiyat} TL"
    except Exception as e:
        bot.send_message(message.chat.id, f"{e}")
