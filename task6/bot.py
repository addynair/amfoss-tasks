import discord
import os
import random
from dotenv import load_dotenv 
import requests
from discord.ext import commands

load_dotenv()

intents=discord.Intents.default()
client = discord.Client(intents = intents)
intents.message_content = True
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hello'):
        print("ACTIVE")
        # await client.process_commands('hello')
        await message.channel.send('Hello!')



    
#discord_bot = commands.Bot(command_prefix='!')
#@discord_bot.command(name='livescore')
#async def msg(ctx):
#     quotes="be positive"

#     response = random.choice(quotes)
#     await ctx.send(response)
client.run(token)

    

    

