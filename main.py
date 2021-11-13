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
 
@client.command(name="purge", pass_context=True, aliases=['p'])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        message = ctx.message
        await message.delete()

  
        await ctx.channel.purge(limit=limit)
        embedVar = discord.Embed(title="Purge Alert!", description=f"Messages Purged by {ctx.message.author}", color=2552230)                                      
        await ctx.channel.send(embed=embedVar)

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="membercount", aliases=['mc'])
async def membercount(ctx):
  embedVar = discord.Embed(title=f"Members in {ctx.guild.name}", description=f"{ctx.guild.member_count}", color=2552230)
  await ctx.reply(embed=embedVar)
    
@client.command(name="mute")
@commands.has_permissions(administrator=True)
async def mute(ctx, user : discord.Member,*, reason=None):
  
    guild = ctx.guild
    role = ctx.guild.get_role(MUTE_ROLE)

    await user.add_roles(role)

    embedVar = discord.Embed(title="User Muted", description=f"{user.mention} has been muted by {ctx.author.mention} with the reason: {reason}")                                      
    await ctx.send(embed=embedVar)
    try:
      await user.send(f"you have been muted in {ctx.guild.name} with the Reason: {reason}")
  
    except:
      await ctx.send(f"unable to dm {user.mention}")

@mute.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="unmute")
@commands.has_permissions(administrator=True)
async def unmute(ctx, user : discord.Member):
  guild = ctx.guild
  role = ctx.guild.get_role(MUTE_ROLE)

  await user.remove_roles(role)

  embedVar = discord.Embed(title="User Unmuted", description=f"{user.mention} has been unmuted by {ctx.author.mention}")                                      
  await ctx.send(embed=embedVar)

@unmute.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")                       
                          
client.run('TOKEN') #use client.run(os.getenv('ENV_TOKEN') for replit dotenv
