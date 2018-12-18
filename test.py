import discord
from discord.ext import commands
import os

os.chdir("/home/ascab/Documents/BotSondage")
with open('token.txt', 'r') as tokenfile:
	TOKEN = (tokenfile.read()).strip("\n")
	print(TOKEN)
	
idpatarotage="374187578846347264"
description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)
Client = Bot('!')
#~ serv = serv.get_server(idpatarotage)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)	
    print(bot.user.id)
    print (discord.__version__)
    #~ print(serv.servers)
    print(type(bot))
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
async def purge(n: int):
	channel=discord.utils.get(bot.channels, name='bip-boup-bip', type=ChannelType.text)	
	deleted = await Client.purge_from(channel, limit=100, check=is_he(usr))
	await bot.send_message(m.channel, 'Deleted {} message(s)'.format(len(deleted)))
@bot.command()
async def exit():
	bot.close()
	
bot.run(TOKEN)
