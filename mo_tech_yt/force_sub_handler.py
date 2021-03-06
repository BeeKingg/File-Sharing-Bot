# (c) @MRK_YT

from configs import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="**Sorry Sir๐**, **You are Banned to use me. Contact my** [Support Group](https://t.me/Mo_Tech_Group).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\n**Files เดตเตเดฃเดเตเดเดฟเตฝ เดเดคเตเดฏเด เดเดเตเดเดณเตเดเต Update Channelil เดเตเดฏเดฟเตป เดเตเดฏเตเดฏเดฃเด...!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("๐ ๐๐จ๐ข๐ง ๐๐ฉ๐๐๐ญ๐ ๐๐ก๐๐ง๐ง๐๐ฅ ๐", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("๐ ๐๐ฎ๐๐ฌ๐๐ซ๐ข๐๐๐ซ๐ฌ ๐๐ ๐๐ก๐๐ง๐ง๐๐ฅ ๐", url="https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ")
                    ],
                    [
                        InlineKeyboardButton("๐ ๐๐๐๐ซ๐๐ฌ๐ก ๐", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/Mo_Tech_Group).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
