import asyncio
import importlib
from pyrogram import idle
from Zuli.modules import ALL_MODULES
from Zuli.modules.Games import GAMES_MODULES

 

loop = asyncio.get_event_loop()


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module(f"Zuli.modules.{all_module}")

    for games_module in GAMES_MODULES:
        importlib.import_module(f"Zuli.modules.Games.{games_module}")

    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ. ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())



