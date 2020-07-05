import asyncio
from telethon.sync import TelegramClient
from telethon import functions, types
from userbot.events import register

message = "**          ⛔️ AL MOMENTO SONO OFFLINE.** **\nQUINDI NON SPAMMATE NELLA CHAT, GRAZIE 🌈** **\nRISPONDERO APPENA SONO DISPONIBILE!** \n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n**         ⛔️ AT THE MOMENT I'M OFFLINE.**\n**SO PLEASE DON'T SPAM IN MY CHAT, THANKS 🌈** \n**I'LL AWNSER AS SOON AS POSIBLE!**"
exempt = []
mutedList = []
autoNiceText = True
exempted = []
e = [] 

@register(outgoing=True)
async def niceText(e):
  if e.text[0].isalpha() and not e.text == "Canali":
    global autoNiceText
    if autoNiceText:
      mex = ""
      for i in range(len(e.text)):
        if e.text[i] == " ":
          mex = mex + ' '
        else:
          mex = mex + e.text[i]
        await asyncio.wait([e.edit("`" + mex + " |`")])
        await asyncio.sleep(0.1)
        await asyncio.wait([e.edit("`" + mex + "  ‏‏‎ `")])
        await asyncio.sleep(0.1)
        if i == len(e.text) - 1:
          await asyncio.wait([e.edit("`" + e.text + "`")])

@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("__» Animazione Testo Disattivata! ❌__")
    else:
      autoNiceText = True
      await e.edit("__» Animazione Testo Attivata! ✅__ ")