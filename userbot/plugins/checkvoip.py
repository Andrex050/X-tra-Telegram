import asyncio

from userbot.events import register
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

@register(outgoing=True, pattern="^[.]checkvoip")
async def checkVoip(e):
  if e.is_reply:
    msg = await e.get_reply_message()
    try:
      user = await e.client(GetFullUserRequest(msg.sender_id))
      dc_id, location = get_input_location(user.profile_photo)
      if user.user.username != None:
        name = "@" + user.user.username
      else:
        name = user.user.first_name
      if dc_id == 4:
        await e.edit(f"**L'Utente » {name}\nnon è un voip ✔️**")
      else:
        await e.edit(f"**L'Utente » {name}\nÈ UN VOIP ⚠️**")
    except:
      await e.edit("**❌ L'Utente deve avere un immagine di profilo ❌**")
  else:
    get = e.text.split(" ", 1)[1]
    try:
      usr = await e.client.get_entity(get)
      user = await e.client(GetFullUserRequest(usr.id))
      dc_id, location = get_input_location(user.profile_photo)
      if user.user.username != None:
        name = "@" + user.user.username
      else:
        name = user.user.first_name
      if dc_id == 4:
        await e.edit(f"**✅ {name} non è un voip ✅**")
      else:
        await e.edit(f"**⚠️ {name} È UN VOIP ⚠️**")
    except:
      await e.edit("**❌ Utente Non Trovato ❌**")