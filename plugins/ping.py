import time
from random import chocie
from pyrogram import Client, filters

STICKER_IDS = "CAACAgUAAxkBAAIBaWKGlZpP4wHeFOC1e9tNXxWUs2OCAALXBAAC9Q-oV8yJbf0Fb9C9JAQ",
              "CAACAgUAAxkBAAIBamKGlZoWkaI8sLTTBi0x3PbNAjUPAALRBgAC-7OoV_DwW_xcFC5fJAQ",
              "CAACAgUAAxkBAAIBa2KGlZoExzuAnEGjhEqEZw71xVmmAAKmBQACpSmoV8ufoK__mXe1JAQ",
              "CAACAgUAAxkBAAIBbGKGlZr4iuzVGWkwu1sy431DcKYCAAJqBAAC7nuxVzQ8Wb80s0UtJAQ"


@Client.on_message(filters.command("ping") & filters.private)
async def ping(bot: Client, message):
    start_ts=time.time()
    beep = await message.reply_text(".")
    sheep=await beep.edit("..")
    ded=await sheep.edit("...")
    end_ts=time.time()
    time_taken=(end_ts - start_ts) * 1000
    await beep.edit(f"Ping : {time_taken}")
