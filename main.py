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
from discord.ext import commands

izinler = discord.Intents.default()
izinler.message_content = True

bot = commands.Bot(command_prefix="!",intents= izinler)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has been started...Installing the codes from the WinbloxOS Servers...")
    time.sleep(1)
    print("[=           ]%25")
    time.sleep(1)
    print("[===         ]%50")
    time.sleep(1)
    print("[========    ]%75")
    time.sleep(1)
    print("[============]%100")
    time.sleep(0.1)
    print("Done!")
    

@bot.event
async def on_message(message):
    if message.author.name == bot.user.name:
        return
    if message.content.startswith("hello"):
        await message.channel.send(f"hello there!")
    if message.content.startswith("winbloxOS"):
        await message.channel.send(f"what?")
    if message.content.startswith("who are you winbloxOS?"):
        await message.channel.send(f"I am a bot created by WinbloxOS(a gaming group).They came here with one purpose...To serve quality.")
    if message.content.startswith("boo"):
        await message.channel.send(f"not loud enough.")
    elif message.content.startswith("BOO!"):
        await message.channel.send(f"AAAAA---*dies*")
    await bot.process_commands(message)

import random

@bot.command("dice")
async def zar_at(ctx):
    await ctx.send(str(random.randint(1,6)))

@bot.command("addition")
async def topla(ctx, sayi1,sayi2):
    sonuc = int(sayi1) + int(sayi2)
    await ctx.send(str(sonuc))

meme_list = os.listdir("./images")

@bot.command("meme")
async def meme(ctx):
    meme = random.choice(meme_list)
    meme_path = os.path.join("./images",meme)
    with open(meme_path, "rb") as img:
        picture = discord.File(img)
    await ctx.send(file = picture)

@bot.command("subtract")
async def subtract(ctx, sayi1,sayi2):
    sonuc = int(sayi1) - int(sayi2)
    await ctx.send(str(sonuc))

bot.run(TOKEN)
