from lexica import Client
from pyrogram import filters
from Zuli import Zuli




def main(prompt: str) -> str:
    client = Client()
    response = client.palm(prompt)
    return response["content"].strip()

@Zuli.on_message(filters.regex(r"Yumi|yumi|baby|Baby"))
async def deepchat(zuli: Zuli, message):
    query = message.text.split(' ', 1)[1]
    x = main(query)
    await message.reply(x)
