import discord
from discord import app_commands
from discord.ext import commands
import os 

TOKEN = os.environ['BOT_TOKEN']
intents = discord.Intents.all() 
intents.members = True
client = commands.Bot (command_prefix = ['','!', '/', '?'], intents = intents)


@client.event
async def on_ready ():
	print('Bot is ready.')

@client.event
async def on_member_join (member):
	print (f'{member} has joined a server.')
  
@client.command ()
async def ping (ctx): 
	await ctx.send(f'Pong! {round (client.latency*1000)} ms')

@client.command ()
async def quit (ctx): 
	await ctx.send('No, you first!')

@client.command ()
async def boo (ctx): 
	await ctx.send('aahhh!')

@client.event
async def on_message (message): 
  if message.content == "boo":
    channel = client.get_channel(message.channel)
    await channel.send('aahhh!') 

  cyclist =  '🚴'
  if ("prof") in message.content:
    await message.add_reaction ( 
cyclist)
  
client.run (TOKEN)


@client.tree.command(name="ping", description="Shows the bot's latency in ms")
async def ping1 (interaction: discord.Interaction): 
	bot_latency = round (client.latency * 1000)
	await interaction.response.send_message (f"Pong! {bot_latency} ms")