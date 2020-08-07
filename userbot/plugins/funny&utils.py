import asyncio
from telethon.sync import TelegramClient
from telethon import functions, types
from userbot.events import register

@register(outgoing=True, pattern="^[.]ficca$")
async def ficca(e):
  for i in range(5):
    await asyncio.wait([e.edit("👉🏻👌🏻 OHH")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("👉🏻 👌🏻OHHSSY ")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("👉🏻  👌🏻OOOOOOH ")])
    await asyncio.sleep(0.2)
  await asyncio.wait([e.edit("OHHSSYY💦!")])

@register(outgoing=True, pattern="^[.]TC$")
async def TC(e):
	await asyncio.wait([e.edit("**Trisomico Cerebroleso con la 104**♿")])

@register(outgoing=True, pattern="^[.]lcl$")
async def lcl(e):
	await asyncio.wait([e.edit("__**lavati con l'acido e fatti qualche shottino di cloroformio, retard del cazzo✨**__")])

@register(outgoing=True, pattern="^[.]MAM$")
async def MAM(e):
	await asyncio.wait([e.edit("**ma ammazzati coglione faccia di merda🤡**")])

@register(outgoing=True, pattern="^[.]niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("`Animazione Testo Disattivata!`")
    else:
      autoNiceText = True
      await e.edit("`Animazione Testo Attivata!`")
      

@register(outgoing=True, pattern="^[.]mex")
async def setMessage(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global message
    message = str(e.text[5:])
    await e.edit("`Messaggio impostato correttamente!`")

@register(outgoing=True, pattern="^[.]pp$")
async def dev(e):
  await asyncio.wait([e.edit("** paypal.me/Andrex90 👈  **")])

@register(outgoing=True, pattern="^[.]rep$")
async def dev(e):
  await asyncio.wait([e.edit("** @AndrexFeedback 👈 **")])

@register(outgoing=True, pattern="^[.]verify$")
async def Verify(e):
  global verify
  verify = e
  await e.client.send_message("@SpamBot", "/start")
 
@register(incoming=True)
async def checkVerify(e):
  global verify
  if verify != None:
    if e.chat_id == 178220800:
      if ":" in e.text:
        st = e.text.split(" ")
        for i in range(st.__len__()):
          if ":" in st[i]:
            fine = st[i - 3] + " " + st[i - 2] + " " + st[i - 1] + " Ore: " +st[i]
            break
        await verify.edit(f"**❌ Sei limitato fino al {fine} ❌**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
      else:
        await verify.edit("**✅ Non sei limitato ✅**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))

@register(incoming=True)
async def autoReply(e):
  if e.is_private and not (await e.get_sender()).bot:
    global mutedList
    if e.chat_id in mutedList:
      await e.delete()
    else:
      if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
        global exempt
        if not e.sender.id in exempt:
          exempt.append(e.sender.id)
          x = 0
          while True:
            if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
              await asyncio.sleep(1)
              x += 1
              if x >= 3:
                global message
                await e.respond(message)
                result = client(functions.account.UpdateProfileRequest(
                    last_name='- OFF',
                ))
                exempt.remove(e.sender.id)
                break
            else:
              exempt.remove(e.sender.id)
              break

