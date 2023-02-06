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
        text = f"Çeyrek Altın:\nAlış: `{asonuc['alis']}`\nSatış: `{asonuc['satis']}`\n\nGram Altın:\nAlış: `{gsonuc['alis']}`\nSatış: `{gsonuc['satis']}`"
        await bot.send_message(
            chat_id=message.chat.id,
            text=text)
    except Exception as e:
        print(e)
        await bot.send_message(
        chat_id=message.chat.id,
        text=f"`{e}`")
