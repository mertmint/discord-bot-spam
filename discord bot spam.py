import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = 'enter your bot token here'
CHANNEL_ID = enter your channel id here
MESSAGE = "enter message"

async def send_spam():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("Error: Could not find channel.")
        return
    
    while not client.is_closed():
        await channel.send(MESSAGE)
        await asyncio.sleep(0.5)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    client.loop.create_task(send_spam())

client.run(TOKEN)
