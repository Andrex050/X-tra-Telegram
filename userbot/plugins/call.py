"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Chiamata a telegram in corso...`",
            "`Chiamata connessa.`",
            "`Telegram: Ciao, di cosa hai bisogno?`",
            "`Io: Yo, sono `@zNotASH`. Senti, mi potresti passare Pavel Durov?`",
            "`Utente Autorizzato!.`",
            "`Chiamata in corso a Pavel Durov...`  `N. +916969696969`",
            "`Chiamata connessa.`",
            "`Io: Yo Durov, potresti bannare questo account Telegram?`
            "`Pavel: Uhm? Posso sapere chi sei?`
            "`Io: Bro? Sono @zNotASH",
            "`Pavel: OMG!!! Da quanto tempo! Ciao ASH!...\nMi assicurerò che quell'account verrà bannato entro 24 ore!`",
            "`Io: Grazie, ci vediamo fratello.`",
            "`Pavel: Non ringraziarmi! Fatti sentire quando sarai libero!`",
            "`Io: Certo, sarà fatto! Ci sentiamo!`",
            "`Pavel: Me lo auguro! Ciao!`",
            "`Chiamata terminata.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
