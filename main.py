import os, dotenv, nextcord
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
  print(f'[Connected] {client.user} (id: {client.user.id})')
  await client.get_channel(984803238211637318).send('Lubot is back!')

@client.slash_command('ping')
async def ping(interaction: Interaction):
  await interaction.response.send_message('pong')

@client.slash_command('stop', 'Stops Lubot')
async def stop(interaction: Interaction):
  await interaction.response.send_message('Lubot stopped!')
  await client.close()


# Setup
if __name__ == '__main__':
  os.system('clear')   # Clear terminal window
  dotenv.load_dotenv() # Load .env
  
  TOKEN = os.getenv('TOKEN') # Get token from enviroment variables
  client.run(TOKEN)