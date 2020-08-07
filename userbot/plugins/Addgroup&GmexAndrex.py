#Copyright by @Andrex050 on telegram

import os
if 1 == 1:
    try:
        from userbot.plugins.sql_helper import SESSION, BASE
    except ImportError:
        raise Exception("Ciao!")

    from sqlalchemy import Column, String, UnicodeText


    class Chat(BASE):
        __tablename__ = "chatmsg"
        chat = Column(String(14), primary_key=True)

        def __init__(self, chat):
            self.chat = str(chat)


    Chat.__table__.create(checkfirst=True)


    def all_chat():
        try:
            return SESSION.query(Chat).all()
        except:
            return None
        finally:
            SESSION.close()


    def is_chat(chat_id):
        try:
            return True if SESSION.query(Chat).get(str(chat_id)) else None
        except:
            return False
        finally:
            SESSION.close()


    def add_chat(chat_id):
        adder = Chat(str(chat_id))
        SESSION.add(adder)
        SESSION.commit()


    def del_chat(chat_id):
        rem = SESSION.query(Chat).get((str(chat_id)))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()

    @command(pattern=r"^.gmex ?(.*)")
    async def msg(event):
    	chats = all_chat()
    	text = event.pattern_match.group(1)
    	chats = chats if chats is not None else []
    	counter = 0
    	for chat in chats:
    		await bot.send_message(int(chat.chat), text)
    		counter += 1
    	await event.edit(f"✅ Messaggio inviato correttamente in {counter} chat")
    
    @command(pattern=r"^.addgroup ?(.*)")
    async def addchat(event):
        chat = event.chat_id if event.pattern_match.group(1) == "" else event.pattern_match.group(1)
        if is_chat(chat):
            await event.edit("❌ Questa chat è già stata aggiunta.")
            return
        add_chat(chat)
        await event.edit(f"✅ » Chat {chat} è stata aggiunta con successo.")

    @command(pattern=r"^.remgroup ?(.*)")
    async def removechat(event):
        chat = event.chat_id if event.pattern_match.group(1) == "" else event.pattern_match.group(1)
        if not is_chat(chat):
            await event.edit("❌ Questa chat non è stata aggiunta.")
            return
        del_chat(chat)
        await event.edit(f"✅ » Chat {chat} è stata rimossa con successo.")
    
    @command(pattern=r"^.listagruppi")
    async def chatlist(event):
        chats = all_chat()
        chats = chats if chats is not None else []
        chatlist = "\n".join([f"`{x.chat}`" for x in chats])
        await event.edit(f"📜 Hai {len(chats)} chat in lista per il gmex.\n🖋️ Elenco:\n{chatlist}")
