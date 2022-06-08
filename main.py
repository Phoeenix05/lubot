import os, dotenv, discord

# Setup
os.system('clear')   # Clear terminal window
dotenv.load_dotenv() # Load .env

TOKEN = os.getenv('TOKEN') # Get token from enviroment variables
client = discord.Client()  # Create discord bot client

@client.event
async def on_ready() -> None:
  print(f'[Connected] {client.user}')

client.run(TOKEN) # Run bot