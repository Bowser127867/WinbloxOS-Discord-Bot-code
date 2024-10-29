#!!!IMPOTANT!!!
#Before you activate the code,make sure to make a .env file then insert the code below this text.
# DISCORD_TOKEN = [your token here]<-------------------------------------------\
#then install the discord libraries if you didnt downloaded them               |
#To install discord open terminal then enter "pip install discord"             |
#then once you are done installing the libraries enter the token right here  __/

import os
from dotenv import load_dotenv
load_dotenv(override=True)

#THE TOKEN GETS THE DISCORD TOKEN IN THE .env FILE!!!
TOKEN = os.environ.get("DISCORD_TOKEN")

import discord
import time
import random
from discord.ext import commands

izinler = discord.Intents.default()
izinler.message_content = True

bot = commands.Bot(command_prefix="!",intents= izinler)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has been started...Installing the codes from the WinbloxOS Servers...")
    time.sleep(1)
    print("Done!")
    

@bot.event
async def on_message(message):
    if message.author.name == bot.user.name:
        return
    if message.content.startswith("hello"):
        await message.channel.send(f"hello there!")
    if message.content.startswith("winbloxOS"):
        await message.channel.send(f"what?")
    if message.content.startswith("boo"):
        await message.channel.send(f"not loud enough.")
    elif message.content.startswith("BOO!") or message.content.startswith("boo!"):
        await message.channel.send(f"AAAAA---*dies*")
    elif message.content.startswith('$coin'):

bot.run(TOKEN)
