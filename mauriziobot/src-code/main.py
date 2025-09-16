import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
import datetime

load_dotenv(dotenv_path="C:/Users/ricca/OneDrive/mauriziobot/src-code/.env") # Qua dovrete inserire il vostro percorso, in questo caso ho messo il mio.

api_key = os.getenv("API_KEY")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connesso come {bot.user}")
    await bot.change_presence(activity=discord.Game(name="con i comandi !help"))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"Hai tirato un **{numero}**!")

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao {ctx.author.mention}! Sei bellissimo!")

@bot.command()
async def info(ctx):
    await ctx.send(f"Ciao sono Maurizio e sono un Bot creato da **{ctx.author.name}**!")

@bot.command()
async def ora(ctx):
    adesso = datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.send(f"Ora attuale: **{adesso}**")

bot.run(api_key)

