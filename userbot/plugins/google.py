import os
import time
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from re import findall
from search_engine_parser import GoogleSearch
from asyncio import sleep
from userbot.utils import register
from telethon.tl.types import DocumentAttributeAudio

@register(outgoing=True, pattern=r"^\.gs (.*)")
async def gsearch(q_event):
    """ For .google command, do a Google search. """
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"\n• [{title}]({link})\n"
        except IndexError:
            break
    await q_event.edit("**💭 Cercando su Google:**` " + match + ".`\n\n**🔗 Risultati:** \n" +
                       msg,
                       link_preview=False)
