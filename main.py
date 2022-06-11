import os, dotenv, nextcord
from nextcord.ext import commands
from util import log

# Load dotnev
dotenv.load_dotenv()

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
  log(f'[Connected] {client.user} (id: {client.user.id})')
  await client.get_channel(984803238211637318).send('Lubot is back!')

initial_extensions = []

for file in os.listdir('./cogs'):
  if file.endswith('.py'):
    initial_extensions.append(f'cogs.{file[:-3]}')

if __name__ == '__main__':
  for extension in initial_extensions:
    client.load_extension(extension)

  client.run(os.getenv('TOKEN'))