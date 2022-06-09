import os, dotenv, discord

# Setup
os.system('clear')   # Clear terminal window
dotenv.load_dotenv() # Load .env

TOKEN = os.getenv('TOKEN') # Get token from enviroment variables
client = discord.Client()  # Create discord bot client
channel: discord.TextChannel = None

def get_channel() -> None:
  global channel
  channel = client.get_channel(953569962486816791)

def startswith_lower(msg: str, prefix: str) -> bool:
  return msg.lower().startswith(prefix)

@client.event
async def on_ready():
  get_channel() # Get general channel
  await channel.send('Lubot connected!')
  print(f'[Connected] {client.user}')

@client.event
async def on_message(message: discord.Message):
  if message.author.id == client.user.id: return
  
  if startswith_lower(message.content, '!ping'):
    await message.reply('pong')
  
  if startswith_lower(message.content, '/stop'):
    # Send message to channel
    await channel.send(f'Shutting down {client.user.name}')
    await client.close() # Close bot client

client.run(TOKEN) # Run bot