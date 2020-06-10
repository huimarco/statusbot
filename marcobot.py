import discord
from discord.ext import commands
from discord.utils import get
from discord.utils import find

bot = commands.Bot('.')

@bot.event
async def on_ready():
    print('Logged in')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
# greeting
    if 'marcobot' in message.content:
        await message.channel.send('I am MarcoBot.')

# chat
    if 'how are you' in message.content:
        await message.channel.send('I am doing well. Thank you for asking.')

# invisible nazi (message)
    if message.content.startswith('skittles'):
        if message.channel.id == 378488703703711745:
            guild = message.author.guild
            role = discord.utils.find(lambda r: r.name == 'swolebois', guild.roles)
            await message.author.remove_roles(role)

    if 'jellybeans' in message.content:
        if message.channel.id == 378488703703711745:
            guild = message.author.guild
            role = discord.utils.find(lambda r: r.name == 'swolebois', guild.roles)
            await message.author.add_roles(role)

    

# invisible nazi (status)
@ bot.event
async def on_member_update(before, after):

    guild = after.guild
    role = discord.utils.find(lambda r: r.name == 'swolebois', guild.roles)

    if str(before.status) == "online":
        if str(after.status) == "offline":
            return
            #await after.remove_roles(role)
    
    if str(before.status) == "idle":
        if str(after.status) == "offline":
            return
            #await after.remove_roles(role)
    
    if str(before.status) == "dnd":
        if str(after.status) == "offline":
            return
            #await after.remove_roles(role)
    
    if str(before.status) == "offline":
        if str(after.status) == "online":
            await after.add_roles(role)
    
        
bot.run('NzE5MDEyNjIyNDE4MDUxMTE1.Xt02xg.OGthb0_mrGje75CQhvAId3rbNe4')