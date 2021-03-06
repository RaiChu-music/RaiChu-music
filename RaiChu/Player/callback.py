# Umm Null Coder

from Process.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from RaiChu.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**I แดแด ๐ฝ๐ค๐ฉ ๐ฟ๐ช๐ฃ๐๐ฎ๐ ๐๐ช๐จ๐๐   
สแดแด สแดษดแดสแด สส [Nikhil](https://t.me/Nikhil_Bots1)
Thanks to add me ๐**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Handle", url="https://t.me/pokemonmaster856"
                    ),
                    InlineKeyboardButton(
                        "๐๐จ๐ฆ๐ฆ๐๐ง๐ ๐๐ข๐ฌ๐ญ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "How to add me๐คท", callback_data="cbhowtouse"
                    ),
                  ],[
                    InlineKeyboardButton(
                       " ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ๐ฟ", url="https://t.me/Nikhil_Bots"
                    ),
                    InlineKeyboardButton(
                        "๐๐ฉ๐๐๐ญ๐๐ฌ", url="https://t.me/Nikhil_Bots"
                    )
                ],[
                    InlineKeyboardButton(
                        "โ ๐๐๐ ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉโ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**
        
โ https://te.legra.ph/file/1ca9f4ebebf50fd1d705a.jpg

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

๐ **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

**โจ แดแดแดกแดสแด สส  Nikhil** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ส แด แด แด", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

**โ Pแดแดกแดสแดแด ๐ Bส: Nikhil!** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป แดแดแดษชษด แดแดแด", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป ๊ฑแดแดแด แดแดแด", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ สแด๊ฑษชแด แดแดแด", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("ส แด แด แด", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โน๏ธ ๐๐จ๐ฆ๐ฆ๐๐ง๐ ๐๐ข๐ฌ๐ญ !

๐ฉ๐ปโ๐ผ ยป /play - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

๐ฉ๐ปโ๐ผ ยป /vplay - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

๐ฉ๐ปโ๐ผ ยป /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

๐คท ยป /skip - to Skip current song

๐ ยป /end - to end play song in vc

 **โ Pแดแดกแดสแดแด ๐ Bส: NIKHIL!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the admin commands:

โฏ /pause - pause the stream
โฏ /resume - resume the stream
โฏ /skip - switch to next stream
โฏ /stop - stop the streaming
โฏ /vmute - mute the userbot on voice chat
โฏ /vunmute - unmute the userbot on voice chat
โฏ /volume `1-200` - adjust the volume of music (userbot must be admin)
โฏ /reload - reload bot and refresh the admin data
โฏ /userbotjoin - invite the userbot to join group
โฏ /userbotleave - order userbot to leave from group

**โ Pแดแดกแดสแดแด ๐ Bส: Nikhil!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the sudo commands:

โฏ /rmw - clean all raw files
โฏ /rmd - clean all downloaded files
โฏ /sysinfo - show the system information
โฏ /update - update your bot to latest version
โฏ /restart - restart your bot
โฏ /leaveall - order userbot to leave from all group

**โ Pแดแดกแดสแดแด ๐ Bส: NIKHIL!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nยป revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **settings of** {query.message.chat.title}\n\nโธ : pause stream\nโถ๏ธ : resume stream\n๐ : mute userbot\n๐ : unmute userbot\nโน : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ nothing is currently streaming", show_alert=True)

# SETUP BUTTON OPEN......................................................................................................................................................................................

@Client.on_callback_query(filters.regex("cbsetup"))
async def cbsetup(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello !**
ยป **press the button below to read the explanation and see the help commands !**
**โ Pแดแดกแดสแดแด ๐ Bส: Nikhil!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("welcome", callback_data="noiwel"),
                    InlineKeyboardButton("Lyric", callback_data="noilyric"),
                    InlineKeyboardButton("voice", callback_data="noivoice"),
                ],
                [
                    InlineKeyboardButton("How To Add Me โ", callback_data="cbhowtouse"),
                ],
                [InlineKeyboardButton("๐ Go Back", callback_data="cbstart")],
            ]
        ),
    )
@Client.on_callback_query(filters.regex("noiwel"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ **HEAR THE WELCOME PLUGIN ( soon )**

โฏ /setwelcome for set welcome message.

โฏ /resetwelcome for reset welcome message.

**โ Pแดแดกแดสแดแด ๐ Bส: NIKHIL!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbsetup")]]
        ),
    )
@Client.on_callback_query(filters.regex("noilyric"))
async def noilyric(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ **HEAR THE LYRIC PLUGIN**

โฏ /lyric ( song name ) for the get lyric of song

**โ Pแดแดกแดสแดแด ๐ Bส: Nikhil!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbsetup")]]
        ),
    )
    
@Client.on_callback_query(filters.regex("noivoice"))
async def noivoice(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ **HEAR THE VOICE PLUGIN**

โฏ /tts fot get voice from text message

**โ Pแดแดกแดสแดแด ๐ Bส: Nikhil!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbsetup")]]
        ),
    )    

    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
