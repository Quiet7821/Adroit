import discord
from discord.ext import commands
import os 

TOKEN = os.environ['BOT_TOKEN']
intents = discord.Intents.all() 
intents.members = True
client = commands.Bot (command_prefix = '!', intents = intents)


@client.event
async def on_ready ():
	print('Bot is ready.')

@client.event
async def on_member_join (member):
	print (f'{member} has joined a server.')
  
@client.command ()
async def ping (ctx): 
	await ctx.send(f'Pong! {round (client.latency*1000)} ms')

client.run (TOKEN)