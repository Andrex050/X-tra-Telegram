from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.utils import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils
import heroku3
from userbot import BRAIN_CHECKER
from userbot.modules import ALL_MODULES

DB = connect("learning-data-root.check")

CURSOR = DB.cursor()

CURSOR.execute("""SELECT * FROM BRAIN1""")

ALL_ROWS = CURSOR.fetchall()

INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \

             '\n  Tip: Use Country Code along with No.' \

             '\n       Recheck your Phone Number'

for i in ALL_ROWS:

    BRAIN_CHECKER.append(i[0])

connect("learning-data-root.check").close()

try:

    bot.start()

except PhoneNumberInvalidError:

    print(INVALID_PH)

    exit(1)

for module_name in ALL_MODULES:

    imported_module = import_module("userbot.modules." + module_name)

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Sto avviando il bot inline...")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Avvio completato. Non ci sono stati errori!")
        print("Sto avviando l'userbot...")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        if Var.HEROKU_APP_NAME and Var.HEROKU_API_KEY is not None:
            Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
            app = Heroku.app(Var.HEROKU_APP_NAME)
            heroku_var = app.config()
            variable = "SUDO_USERS"
            if variable in heroku_var:
                del heroku_var[variable]
            else:
                print("Sta procedendo tutto bene!")
        print("Avvio completato!")
    else:
        bot.start()
    

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print("Avvio completato! Userbot Funzionante!")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
