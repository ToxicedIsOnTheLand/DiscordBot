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

@client.command(name="ban")
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *, reason=None):
  try:
    await user.ban(reason=reason)
    embed = discord.Embed(title="User has been Banned", description=f"{ctx.mention} has been banned by {ctx.author.mention}")
    await ctx.send(embed=embed)
  except:
    embed = discord.Embed(title="User cannot be Banned", description=f"cannot ban {ctx.mention}!")
    await ctx.reply(embed=embed)

@ban.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="unban")
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member_id: int):
  try:
    await ctx.guild.unban(discord.Object(id=member_id))
    embed = discord.Embed(title="Unbanned User", description="Specific user has been Unbanned
    await ctx.reply(embed=embed)
  except:
    embed = discord.Embed(title="Cannot unban User!", description="Cannot unban the specific User!")
    await ctx.reply(embed=embed)

@unban.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")
  
client.run('TOKEN') #use client.run(os.getenv('ENV_TOKEN') for replit dotenv
