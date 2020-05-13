# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# The entire source code is OSSRPL except 'whois' which is MPL
# License: MPL and OSSRPL
""" Userbot module for getiing info
    about any user on Telegram(including you!). """

import os

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot import CMD_HELP
from userbot.events import register, errors_handler

TMP_DOWNLOAD_DIRECTORY = "./"


@register(pattern=".whois(?: |$)(.*)", outgoing=True)
@errors_handler
async def who(event):
    """ For .whois command, get info about a user. """
    if event.fwd_from:
        return

    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user(event)

    photo, caption = await fetch_info(replied_user, event)

    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.client.send_file(event.chat_id,
                                     photo,
                                     caption=caption,
                                     link_preview=False,
                                     force_document=False,
                                     reply_to=message_id_to_reply,
                                     parse_mode="html")

        if not photo.startswith("http"):
            os.remove(photo)
        await event.delete()

    except TypeError:
        await event.edit(caption, parse_mode="html")


async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(
                GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return replied_user


async def fetch_info(replied_user, event):
    """ Get details from the User object. """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(user_id,
                                                      TMP_DOWNLOAD_DIRECTORY +
                                                      str(user_id) + ".jpg",
                                                      download_big=True)
    first_name = first_name.replace(
        "\u2060", "") if first_name else ("Questo utente non ha nome.")
    last_name = last_name.replace(
        "\u2060", "") if last_name else ("Questo utente non ha cognome.")
    username = "@{}".format(username) if username else (
        "Questo utente non ha un Username.")
    user_bio = "Questo utente non ha una descrizione." if not user_bio else user_bio

    caption = "<b>ℹ️ INFO UTENTE</b> \n\n"
    caption += f"• 💭 <b>Nome:</b> <code>{first_name}</code> \n"
    caption += f"• 💭 <b>Cognome:</b> <code>{last_name}</code> \n"
    caption += f"• 🖇 <b>Username:</b> {username} \n"
    caption += f"• 🤖 <b>Bot:</b> <code>{is_bot}</code> \n"
    caption += f"• 🔑 <b>Limitato:</b> <code>{restricted}</code> \n"
    caption += f"• ✅ <b>Verificato:</b> <code>{verified}</code> \n"
    caption += f"• 🆔 <b>ID:</b> <code>{user_id}</code> \n"
    caption += f"• 📝 <b>Bio:</b> <code>{user_bio}</code> \n"
    caption += f"• 💡 <b>Gruppi in comune:</b> <code>{common_chat}</code> \n"
    caption += f"• 🔗 <b>Link permanente:</b> "
    caption += f"<a href=\"tg://user?id={user_id}\">{first_name}</a>"

    return photo, caption


CMD_HELP.update({
    "whois":
    ".whois <username>(o reply)"
})
