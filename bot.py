import os
import logging
import asyncio
from telethon import TelegramClient, events, Button
from telethon.tl.functions.users import GetFullUserRequest

print("Starting deployment...")
try:
    api_id = int(os.environ["API_ID"])
    api_hash = os.environ["API_HASH"]
    bot_token = os.environ["BOT_TOKEN"]
    from_channel = int(os.environ["FROM_CHANNEL"])
    to_channel = int(os.environ["TO_CHANNEL"])
    
    bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
except:
    print("Mandatory vars are missing! Kindly check again.")
    print("Bot is quiting...")
    exit()


@bot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await bot(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hi `{ok.user.first_name}`!\n\nI am a channel post forwarder bot!! Read /help to know more!\n\nI can be used in only two channels (one user) at a time. Kindly deploy your own bot.", buttons=[Button.url("Updates Channel", url="https://t.me/roBots_Hub"),Button.url("Repo", url="https://github.com/stark-Prince/PostForwarderBot"), Button.url("Dev", url="https://t.me/its_Prince")], link_preview=False)


@bot.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("**Help menu**\n\nThis bot will send all new posts in one channel to the other channel. (without forwarded tag)!\nIt can be used only in two channels at a time, so kindly deploy your own bot from [here](https://github.com/stark-Prince/PostForwarderBot).\n\nAdd me to both the channels and make me an admin in both, and all new messages would be autoposted on the linked channel!!")

@bot.on(events.NewMessage(incoming=True, chats=from_channel)) 
async def _(event): 
    if not event.is_private:
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                await bot.send_file(to_channel, photo, caption = event.text, link_preview = False)
            elif event.media:
                try:
                    if event.media.webpage:
                        await bot.send_message(to_channel, event.text, link_preview = False)
                        return
                except:
                    media = event.media.document
                    await bot.send_file(to_channel, media, caption = event.text, link_preview = False)
                    return
            else:
                await bot.send_message(to_channel, event.text, link_preview = False)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has been deployed.")
bot.run_until_disconnected()
