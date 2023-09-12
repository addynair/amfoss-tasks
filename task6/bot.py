import discord
import os
from dotenv import load_dotenv 
import requests
from discord.ext import commands
from scraper import score
from datetime import date
import pandas as pd


load_dotenv()

intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
token = os.getenv('TOKEN')
today = date.today()

bot.remove_command('help')




@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    

    
@bot.command()
async def livescore(ctx):
    print("Taking in")
    await ctx.send('fetching scores')
    await ctx.send(score)
    await ctx.send(today)



@bot.command()
async def help(ctx):
    print("Loading")
    await ctx.send("Commands:")
    await ctx.send("!csv- get the csv file livescores are stored in")
    await ctx.send("!livescore- get the live scores")




bot.run(token)    

  
    
  


    

    

