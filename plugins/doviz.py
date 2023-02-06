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
        text = f"Dolar:\nAlış: `{dsonuc['alis']}`\nSatış: `{dsonuc['satis']}`\n\Euro:\nAlış: `{esonuc['alis']}`\nSatış: `{esonuc['satis']}`"
        await bot.send_message(
            chat_id=message.chat.id,
            text=text)
    except Exception as e:
        print(e)
        await bot.send_message(
        chat_id=message.chat.id,
        text=f"`{e}`") 
