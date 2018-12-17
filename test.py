import discord
from discord.ext import commands

TOKEN = 'NTIzOTk5MzY1Mzc5OTE1ODE2.DvhsKg.LwPsafPJ1gqL5gfJqjzAZLCG1Nw'
idpatarotage='374187578846347264'
description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)
server = discord.Client.get_server(idpatarotage)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello():
    """Says Hello World"""
    await bot.say("Hellod")
@bot.command()
async def tg(usr: discord.Member ):
	await bot.say('TG' + usr.mention )	

@bot.command()
async def dududu():
	await bot.say("https://www.youtube.com/watch?v=y6120QOlsfU")
	
def is_me(m):
    return m.author == bot.user
def is_he(m, usr: discord.Member):
	return m.author == usr 
@bot.command()
async def purge(usr=None):
	channel=discord.utils.get(server.channels, name='bip-boup-bip', type=ChannelType.text)	
	deleted = await bot.purge_from(channel, limit=100, check=is_he(usr))
	await bot.send_message(m.channel, 'Deleted {} message(s)'.format(len(deleted)))

bot.run(TOKEN)
