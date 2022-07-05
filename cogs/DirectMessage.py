import nextcord
from nextcord.ext import commands
from util import log


class DirectMessage(commands.Cog):
  def __init__(self, client: commands.Bot) -> None:
    super().__init__()
    self.client = client
  
  @commands.Cog.listener()
  async def on_message(self, msg: nextcord.Message) -> None:
    if (msg.author.bot): return
  

def setup(client: commands.Bot) -> None:
  client.add_cog(DirectMessage(client))