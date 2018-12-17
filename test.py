import discord
from discord.ext import commands

TOKEN = 'NTIzOTk5MzY1Mzc5OTE1ODE2.DvhsKg.LwPsafPJ1gqL5gfJqjzAZLCG1Nw'

description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)

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
bot.run(TOKEN)
@bot.command()
async def purge(usr: discord.Member):
	await purge_from(
