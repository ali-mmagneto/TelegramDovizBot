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
        text = f"Bitcoin:\nAlış: `{bsonuc['alis']}`\nSatış: `{bsonuc['satis']}`\n\nEthereum:\nAlış: `{etsonuc['alis']}`\nSatış: `{etsonuc['satis']}`"
        await bot.send_message(
            chat_id=message.chat.id,
            text=text)
    except Exception as e:
        print(e)
        await bot.send_message(
        chat_id=message.chat.id,
        text=f"`{e}`")
