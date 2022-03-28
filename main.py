import disnake
import discord
import discord_slash
import os
import random
import time
import disnake.ext
from disnake.utils import get
from disnake.ext import commands, tasks
from disnake.ext.commands import has_permissions,  CheckFailure, check

# Unreal Bot developers are not allowed to use this

# Unreal Bot developers are not allowed to use this

# Unreal Bot developers are not allowed to use this

client = disnake.Client()

intents.members = True
intents.presences = True
intents.guild_reactions = True
intents.reactions = True

client = commands.InteractionBot(test_guilds=[GUILD_ID])

client = commands.Bot(command_prefix = '?') #replace the ? to your own prefix

@client.event
async def on_ready():
  print("your bot is online")
  
@client.slash_command()
async def say(inter, text):
  await inter.send(text)

@client.slash_command()
@commands.has_permissions(ban_members = True)
async def ban(inter, user : discord.User, *, reason=None):
  try:
    await user.ban(reason=reason)
    embed = disnake.Embed(title="User has been Banned", description=f"{inter.mention} has been banned by {inter.author.mention}")
    await inter.send(embed=embed)
  except:
    embed = disnake.Embed(title="User cannot be Banned", description=f"cannot ban {inter.mention}!")
    await inter.send(embed=embed)

@ban.error
async def clear_error(inter, error):
    if isinstance(error, commands.MissingPermissions):
        await inter.send(f"{inter.author.mention} You do not have Permissions to use this Command!")

@client.command(name="unban")
@commands.has_permissions(administrator = True)
async def unban(inter, member_id: int):
  try:
    await inter.guild.unban(discord.Object(id=member_id))
    embed = disnake.Embed(title="Unbanned User", description="Specific user has been Unbanned")
    await inter.send(embed=embed)
  except:
    embed = disnake.Embed(title="Cannot unban User!", description="Cannot unban the specific User!")
    await inter.send(embed=embed)

@unban.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")
 
@client.command(description="purges messages")
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def purge(inter, limit: int):
        await inter.channel.purge(limit=limit)
    
        embed = disnake.Embed(title="Purge Alert!", description=f"Messages Purged by {inter.author}", color=2552230) 
      
        await inter.channel.send(embed=embed)

@client.event
async def on_command_error(inter, error):
    await inter.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await inter.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@clean.error
async def clear_error(inter, error):
    if isinstance(error, commands.MissingPermissions):
      await inter.send(f"{inter.author.mention} You do not have Permissions to use this Command!")

@client.slash_command(description="membercount of a server")
async def membercount(inter):
  embed = disnake.Embed(title=f"Members in {inter.guild.name}", description=f"{inter.guild.member_count}", color=2552230)
  await inter.send(embed=embed)

#@client.command(name="mute")
#@commands.has_permissions(administrator=True)
#async def mute(ctx, user : discord.Member,*, reason=None):
  
    #guild = ctx.guild
    #role = ctx.guild.get_role(MUTE_ROLE)
    
    #await user.add_roles(role)

    #embedVar = discord.Embed(title="User Muted", description=f"{user.mention} has been muted by {ctx.author.mention} with the reason: {reason}")                                      
    #await ctx.send(embed=embedVar)
    #try:
      #await user.send(f"you have been muted in {ctx.guild.name} with the Reason: {reason}")
  
    #except:
      #await ctx.send(f"unable to dm {user.mention}")

#@mute.error
#async def clear_error(ctx, error):
    #if isinstance(error, commands.MissingPermissions):
        #await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

#@client.command(name="unmute")
#@commands.has_permissions(administrator=True)
#async def unmute(ctx, user : discord.Member):
  #guild = ctx.guild
  #role = ctx.guild.get_role(MUTE_ROLE)

  #await user.remove_roles(role)

  #embedVar = discord.Embed(title="User Unmuted", description=f"{user.mention} has been unmuted by {ctx.author.mention}")                                      
  #await ctx.send(embed=embedVar)

#@unmute.error
#async def clear_error(ctx, error):
    #if isinstance(error, commands.MissingPermissions):
        #await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")   
                  
# will test out 2 more commands in the next update     
      
from config import TOKEN
client.run(TOKEN) # does not hide your token in replit
