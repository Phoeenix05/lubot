import os, sys
from datetime import datetime

import dotenv, nextcord
from nextcord import Interaction
from nextcord.ext import commands
from rich import print

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)


def time() -> str: return datetime.now().strftime('%H:%M:%S')
def log(s: str) -> None: print(f'[{time()}] {s}')

@client.event
async def on_ready():
  log(f'[Connected] {client.user} (id: {client.user.id})')
  await client.get_channel(984803238211637318).send('Lubot is back!')

@client.slash_command('ping', 'Lubot latency info')
async def ping(interaction: Interaction):
  # Create embeded message
  embed = nextcord.Embed()
  embed.color = nextcord.Color.from_rgb(150, 255, 0) # Set message color
  # Add fields to message
  embed.add_field(
    name =  'Latency',
    value = f'Ping {client.latency * 1000:.0f} ms'
  )
  await interaction.response.send_message(embed=embed)

@client.slash_command('stop', 'Stops Lubot')
async def stop(interaction: Interaction):
  log(f'Lubot stopped by {interaction.user}')
  await interaction.response.send_message('Lubot stopped!')
  # Close bot client
  await client.close()

@client.slash_command('restart', 'Restart Lubot')
async def restart(interaction: Interaction):
  await interaction.response.send_message('Restarting!')
  log('Restarting')
  # Restart the program by replacing the process
  os.execv(sys.executable, ['python3'] + sys.argv)


# Setup
if __name__ == '__main__':
  dotenv.load_dotenv() # Load .env

  TOKEN = os.getenv('TOKEN') # Get token from enviroment variables
  client.run(TOKEN)
