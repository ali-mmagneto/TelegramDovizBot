# Coded By :d

from pyrogram import Client, filters
import requests

dovizurl = "https://api.genelpara.com/embed/doviz.json"

@Client.on_message(filters.command('doviz'))
async def dovizcek(bot, message):
    try:
        distek = requests.get(dovizurl)
        dveri = distek.json()
        dsonuc = dveri['USD']
        eistek = requests.get(dovizurl)
        everi = eistek.json()
        esonuc = everi['EUR']
        dyön = f"{dsonuc['d_yon']}"
        eyön = f"{esonuc['d_yon']}"
        artis = "caret-up"
        azalis = "caret-down"
        if dyön == azalis:
            demoji = "📉" 
        else:
            demoji = "📈"
        if eyön == azalis:
            eemoji = "📉" 
        else:
            eemoji = "📈"
        text = f"{demoji} Dolar:\nAlış: `₺{dsonuc['alis']}`\nSatış: `₺{dsonuc['satis']}`\nDeğişim: `{dsonuc['d_oran']}%`\n\n{eemoji} Euro:\nAlış: `₺{esonuc['alis']}`\nSatış: `₺{esonuc['satis']}`\nDeğişim: `{esonuc['d_oran']}%`"
        await bot.send_message(
            chat_id=message.chat.id,
            text=text)
    except Exception as e:
        print(e)
        await bot.send_message(
        chat_id=message.chat.id,
        text=f"`{e}`") 
