import discord
from discord.ext import commands
import os 

TOKEN = os.environ['BOT_TOKEN']
intents = discord.Intents.all() 
intents.members = True
client = commands.Bot(command_prefix=['!', '/', '?'], intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')
    try:
        synced = await client.app_commands.sync_commands()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.application_command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!")

@client.application_command(name="say")
@commands.app_commands.description("What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str): 
    await interaction.response.send_message(f"{interaction.user.name} said: {thing_to_say}")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.command()
async def ping(ctx): 
    await ctx.send(f'Pong! {round(client.latency*1000)} ms')

@client.command()
async def quit(ctx): 
    await ctx.send('No, you first!')

@client.command()
async def boo(ctx): 
    await ctx.send('aahhh!')

client.run(TOKEN)


