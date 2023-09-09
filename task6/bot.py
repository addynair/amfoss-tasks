import discord
import os
from dotenv import load_dotenv 
import requests

load_dotenv()


client = discord.Client(intents=discord.Intents.default())

def get_score():
    response = requests.get("")


@client.event

async def on_ready():
    print('We have logged in as {0.user}'
          .format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'hello':
        print("said hello")
        await message.channel.send('Hello!')
    

client.run(os.getenv('TOKEN'))