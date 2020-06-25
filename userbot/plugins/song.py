from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
from userbot.utils import admin_cmd
from userbot import CMD_HELP
import glob
import os
try:
 import instantmusic , subprocess
except:
 os.system("pip install instantmusic")
 


os.system("rm -rf *.mp3")


def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    

@borg.on(admin_cmd(pattern="song ?(.*)"))
async def _(event):
    await event.edit("__**📶 Ricerca in corso...**__")
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply.text:
        query = reply.message
    else:
     await event.edit("__**🔄 Caricamento...**__ ")
     return
    
    bruh(str(query))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("__**⤵️ Sto inviando la canzone...**__")
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=("**✍️ Nome canzone: **"+ query + "\n**🗂️ Caricata da:** [Andrex](@Andrex050)\n"),
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
    
    
    
CMD_HELP.update({"getmusic": ['getmusic',
    " - .song query : finds the song you entered in query and sends it "
    " - .song <Name> or .song (replied message)"]
})