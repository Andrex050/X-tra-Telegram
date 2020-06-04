
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


@command(outgoing=True, pattern=".on$")
async def amireallyalive(alive):
    await alive.edit("**💭 Userbot Online.**\n"
		     "**📟 Python:** `3.7.3`\n"
	             "__⌨️ Created by @zNotASH.__")

