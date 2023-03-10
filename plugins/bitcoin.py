# Coded by :d

from pyrogram import Client, filters
import requests

dovizurl = "https://api.genelpara.com/embed/doviz.json"

@Client.on_message(filters.command('bitcoin'))
async def bitcoincek(bot, message):
    try:
        bistek = requests.get(dovizurl)
        bveri = bistek.json()
        bsonuc = bveri['BTC']
        etistek = requests.get(dovizurl)
        etveri = etistek.json()
        etsonuc = etveri['ETH']
        byön = f"{bsonuc['d_yon']}"
        etyön = f"{etsonuc['d_yon']}"
        artis = "caret-up"
        azalis = "caret-down"
        if byön == azalis:
            bemoji = "📉" 
        else:
            bemoji = "📈"
        if etyön == azalis:
            etemoji = "📉" 
        else:
            etemoji = "📈"
        text = f"{bemoji} Bitcoin:\nAlış: `₺{bsonuc['alis']}`\nSatış: `₺{bsonuc['satis']}`\nDeğişim: `{bsonuc['d_oran']}%`\n\n{etemoji} Ethereum:\nAlış: `₺{etsonuc['alis']}`\nSatış: `₺{etsonuc['satis']}`\nDeğişim: `{etsonuc['d_oran']}%`"
        await bot.send_message(
            chat_id=message.chat.id,
            text=text)
    except Exception as e:
        print(e)
        await bot.send_message(
        chat_id=message.chat.id,
        text=f"`{e}`")
