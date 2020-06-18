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

# role on message
    if message.content.startswith('buzzword1'):
        if message.channel.id == 378488703703711745:
            guild = message.author.guild
            role = discord.utils.find(lambda r: r.name == 'rolename', guild.roles)
            await message.author.remove_roles(role)

    if message.content.startswith('buzzword2'):
        if message.channel.id == 378488703703711745:
            guild = message.author.guild
            role = discord.utils.find(lambda r: r.name == 'rolename', guild.roles)
            await message.author.add_roles(role)


# role on status
@ bot.event
async def on_member_update(before, after):

    guild = after.guild
    var = discord.utils.find(lambda r: r.name == 'mute', guild.roles)
    prereq = discord.utils.find(lambda r: r.name == 'prereq', guild.roles)

    if not before.bot:
        if prereq in before.roles:
            if str(before.status) == "online":
                if str(after.status) == "offline":
                    await after.add_roles(var)
            if str(before.status) == "idle":
                if str(after.status) == "offline":
                    await after.add_roles(var)            
            if str(before.status) == "dnd":
                if str(after.status) == "offline":
                    await after.add_roles(var)           
            if str(before.status) == "offline":
                if str(after.status) == "online":
                    await after.remove_roles(var)
            else:
                return
    else: 
        return
        
bot.run(TOKEN)
