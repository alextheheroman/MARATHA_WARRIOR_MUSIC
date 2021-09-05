from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/316f773f02cf2c6c118a1.jpg")
    await message.reply_text(
        f"""**Hey, I'm HEAVEN MUSIC BOT🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [Mᴀɴᴀᴠ](https://t.me/aloneness24)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ", url="https://t.me/aloneness24")
                  ],[
                    InlineKeyboardButton(
                        "🚑 SUPPORT GROUP 🚑", url="https://t.me/HEAVEN_MUSIC_SUPPORT"
                    ),
                    InlineKeyboardButton(
                        "🚨UPDATE CHANNEL 🚨", url="https://t.me/HEAVEN_MUSIC_NEWS"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "GROUP ME LEJAO 😆", url="https://t.me/HAEVEN_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**#HEAVEN_MUSIC_ON_FIRE**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚨 UPDATE CHANNEL 🚨", url="https://t.me/HEAVEN_MUSIC_NEWS")
                ]
            ]
        )
   )


