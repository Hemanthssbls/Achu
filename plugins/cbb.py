#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>⁕ Cʀᴇᴀᴛᴏʀ : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n⁕ Language : <code>Python3</code>\n⁕ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n⁕ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : <a href='https://google.com'>Click Here</a>\n⁕ Cʜᴀɴɴᴇʟ : <a href='https://t.me/FILMCORNERALL'>Click Here</a> \n⁕ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : <a href='https://t.me/FILMCORNEROFFICIALGROUP'>Click Here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
