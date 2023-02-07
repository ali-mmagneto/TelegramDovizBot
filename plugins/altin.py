# Coded by :d

from pyrogram import Client, filters
import requests

dovizurl = "https://api.genelpara.com/embed/doviz.json"

@Client.on_message(filters.command('altin'))
async def altincek(bot, message):
    try:
        aistek = requests.get(dovizurl)
        averi = aistek.json()
        asonuc = averi['C']
        gistek = requests.get(dovizurl)
        gveri = gistek.json()
        gsonuc = gveri['GA']
        artis = "caret-up"
        azalis = "caret-down"
        gyön = f"{gsonuc['alis']}"
        ayön = f"{asonuc['alis']}"
        if ayön == azalis:
            aemoji = "📉" 
        else:
            aemoji = "📈"
        if gyön == azalis:
            gemoji = "📉" 
        else:
            gemoji = "📈"
        text = f"{aemoji} Çeyrek Altın:\nAlış: `₺{asonuc['alis']}`\nSatış: `₺{asonuc['satis']}`\nDeğişim: `{asonuc['d_oran']}%`\n\n{gemoji} Gram Altın:\nAlış: `₺{gsonuc['alis']}`\nSatış: `₺{gsonuc['satis']}`\nDeğişim: `{gsonuc['d_oran']}%`"
        await bot.send_message(
            chat_id=message.chat.id,
            text=text)
    except Exception as e:
        print(e)
        await bot.send_message(
        chat_id=message.chat.id,
        text=f"`{e}`")
