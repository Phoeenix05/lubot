import os, dotenv, discord
from discord.ext import commands

# Setup
os.system('clear')   # Clear terminal window
dotenv.load_dotenv() # Load .env

TOKEN = os.getenv('TOKEN') # Get token from enviroment variables
client = commands.Bot(command_prefix=('/', '!'))  # Create discord bot client

@client.event
async def on_ready():
  # get_channel() # Get general channel
  # await channel.send('Lubot connected!')
  print(f'[Connected] {client.user}')

@client.command()
async def ping(ctx: commands.Context):
  if (ctx.prefix != '!'): return
  await ctx.reply('pong', mention_author=False)

@client.command()
async def stop(ctx: commands.Context):
  await ctx.send(f'Shutting down {client.user.name}')
  await client.close()

client.run(TOKEN) # Run bot