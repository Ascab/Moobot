import discord
from discord.ext import commands
import os
import time
from datetime import datetime
import sys
import asyncio

os.chdir("/home/ascab/Documents/Moobot")
with open('token.txt', 'r') as tokenfile:
	TOKEN = (tokenfile.read()).strip("\n")
	
description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)
    
@bot.event
async def on_ready():
	timestamp = time.time()
	utctime = datetime.utcfromtimestamp(timestamp)
	print('Logged in as at '+ str(utctime) + 'UTC')
	print(bot.user.name)	
	print(bot.user.id)
	print (discord.__version__)
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
	
async def del_msgs(msg, l) :
	if l == 1 :
		await bot.delete_message(msg.pop())
	elif l >= 2 :
		await bot.delete_messages(msg)
@bot.command(pass_context=True)
async def purge(ctx, n: int, usr=None):
	"""?purge <n> [usr] : Supprime number messages. Si un utilisateur est mentionné 
	supprime nomber message de user"""
	channel=ctx.message.channel
	timestamp = time.time()
	utctime = datetime.utcfromtimestamp(timestamp-(12*3600))
	msg = []
	if usr!=None :
		target = ctx.message.mentions.pop().id
		print(target)
		async for x in bot.logs_from(channel, limit = int(n), before=ctx.message ,after=utctime, around=None) : 
			if x.author.id == target :
				msg.append(x)
	else :
		async for x in bot.logs_from(channel, limit=int(n), before=ctx.message ,after=utctime, around=None) :
		 	msg.append(x)
	length=len(msg)	 	
	await del_msgs(msg, length)
	await bot.say('Deleted {} message(s)'.format(length))
	print('Deleted {} message(s) at {} :'.format(length, datetime.utcfromtimestamp(timestamp)))
@bot.command()
async def exit():
	"""Deconnecte le bot et coupe le programme"""
	await bot.say('Au revoir')
	await bot.close() 
@bot.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)
@bot.command(pass_context=True)
async def robin(ctx) :
	await bot.send_message(discord.Object(id='524866929085775872'), 'Bon anniversaire'+ ctx.message.server.get_member('184685136372039680').mention + 'fait peter le champagne !')
@bot.command(pass_context=True)
async def kick(ctx) :
	for target in ctx.message.mentions :
		await bot.kick(target)
bot.run(TOKEN)
