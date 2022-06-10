import os, sys, dotenv, nextcord
from nextcord import Interaction
from nextcord.ext import commands
from time import time

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
  print(f'[Connected] {client.user} (id: {client.user.id})')
  await client.get_channel(984803238211637318).send('Lubot is back!')

@client.slash_command('ping')
async def ping(interaction: Interaction):
  await interaction.response.send_message(f'{client.latency  * 1000:.0f} ms')

@client.slash_command('stop', 'Stops Lubot')
async def stop(interaction: Interaction):
  await interaction.response.send_message('Lubot stopped!')
  await client.close()

@client.slash_command('restart', 'Restart Lubot')
async def restart(interaction: Interaction):
  await interaction.response.send_message('Restarting!')
  os.execv(sys.executable, ['python3'] + sys.argv)

# Setup
if __name__ == '__main__':
  dotenv.load_dotenv() # Load .env
  
  TOKEN = os.getenv('TOKEN') # Get token from enviroment variables
  client.run(TOKEN)