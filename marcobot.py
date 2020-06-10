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
        await message.channel.send('Good.')

# roles on message
    if message.content.startswith('adhesive'):
        if message.channel.id == 378488703703711745:
            guild = message.author.guild
            role = discord.utils.find(lambda r: r.name == 'swolebois', guild.roles)
            await message.author.remove_roles(role)

    if message.content.startswith('quixotic'):
        if message.channel.id == 378488703703711745:
            guild = message.author.guild
            role = discord.utils.find(lambda r: r.name == 'swolebois', guild.roles)
            await message.author.add_roles(role)

# role on status
@ bot.event
async def on_member_update(before, after):

    guild = after.guild
    role = discord.utils.find(lambda r: r.name == 'swolebois', guild.roles)

    if before.bot:
        return
    
    if str(before.status) == "online":
        if str(after.status) == "offline":
            await after.remove_roles(role)
    
    if str(before.status) == "idle":
        if str(after.status) == "offline":
            await after.remove_roles(role)
    
    if str(before.status) == "dnd":
        if str(after.status) == "offline":
            await after.remove_roles(role)
    
    if str(before.status) == "offline":
        if str(after.status) == "online":
            await after.add_roles(role)
        
bot.run(TOKEN)
