from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from userbot import bot
from userbot.events import register

@register(outgoing=True, pattern="^.sup$")
async def kk(event):
    await event.edit("\n**╔┓┏╦━━╦┓╔┓╔━━╗**"
		     "\n**║┗┛║┗━╣┃║┃║╯╰║**"
		     "\n**║┏┓║┏━╣┗╣┗╣╰╯║**"
		     "\n**╚┛┗╩━━╩━╩━╩━━╝**")