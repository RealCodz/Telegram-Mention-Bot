from telethon import TelegramClient, events
import asyncio
import random

ID = ''
HS = ''
TK = ''

bt = TelegramClient('bot', ID, HS).start(bot_token=TK)
t = False
a = False

def ld_txt():
    with open('texts.txt', 'r', encoding='utf-8') as f:
        return [l.strip() for l in f]

txt = ld_txt()

@bt.on(events.NewMessage)
async def hdl_msg(e):
    global t, a
    
    if e.raw_text == '/on' or e.raw_text == 'تفعيل':
        a = True
        return await e.reply('✅ Bot activated. You can use the bot now.')
    
    if not a:
        return

    if e.raw_text == '/tag' or e.raw_text == 'تاك':
        if not t:
            t = True
            await e.reply('✅ Started tagging members.')
            await st_tag(e.chat_id)
        else:
            await e.reply('Already running.')
            
    elif e.raw_text == '/off' or e.raw_text == 'ايقاف':
        if t:
            t = False
            await e.reply('🚫 Stopped tagging members.')
        else:
            await e.reply('Already stopped.')
            
    elif e.raw_text == '/contact' or e.raw_text == 'تواصل':
        await e.reply(
            "[Channel](https://t.me/RealCodz) [Account](https://t.me/xqxxqqxq)",
            parse_mode='markdown'
        )

async def st_tag(c_id):
    while t:
        try:
            async for u in bt.iter_participants(c_id):
                m = f'<a href="tg://user?id={u.id}">{u.first_name or "Unknown"}</a>'
                await bt.send_message(
                    c_id,
                    f'{m} {random.choice(txt)}',
                    parse_mode='html'
                )
                await asyncio.sleep(60)
        except Exception:
            await asyncio.sleep(60)

bt.run_until_disconnected()
