from pyrogram import Client, Filters, Message
from pyrogram.errors import FloodWait
import asyncio
import random

sudo_user = "your_sudo_user"
RAID = ["spam1", "spam2", "spam3"]


@Client.on_message(Filters.user(sudo_user) & Filters.command(["raid"], [".", "!", "/"]))
async def raid(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    quantity = message.command[1]
    text_ = get_text(message)
    spam_text = ' '.join(message.command[2:])
    user, reason = get_user(message, spam_text)
    failed = 0 
    try:
        userz = await client.get_users(user)
    except:
        await sex.edit(f"`404: User Doesn't Exist in This Chat!`")
        return            
    if not text_:
        await sex.edit("`Who should I raid? You?`")
        return
    raid = random.choice(RAID) 
    blaze = f"[{userz.first_name}](tg://user?id={userz.id}) {raid}"
    quantity = int(quantity)

    for _ in range(quantity):
        await asyncio.sleep(2)
        try:
            await client.send_message(message.chat.id, blaze)            
        except FloodWait as e:
            await asyncio.sleep(e.x)
