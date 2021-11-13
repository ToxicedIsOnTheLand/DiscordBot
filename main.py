import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

client = discord.Client()

client = commands.Bot(command_prefix = '?') #replace the ? to your own prefix

@client.event
async def on_ready():
  print("your bot is online")
  
@client.command(name="say")
@commands.has_permissions(administrator=True)
async def say(ctx, *, text):
  await ctx.send("{text}")

client.run('TOKEN') #use client.run(os.getenv('ENV_TOKEN') for replit dotenv
