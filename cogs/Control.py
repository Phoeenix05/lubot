import os, sys, nextcord
from nextcord import Interaction
from nextcord.ext import commands
from util import log


class Control(commands.Cog):
  def __init__(self, client: commands.Bot) -> None:
    super().__init__()
    self.client = client

  @nextcord.slash_command('ping', 'Lubot latency info')
  async def ping(self, interaction: Interaction):
    # Create embeded message
    embed = nextcord.Embed()
    embed.color = nextcord.Color.from_rgb(150, 255, 0) # Set message color
    # Add fields to message
    embed.add_field(
      name =  'Latency',
      value = f'Ping {self.client.latency * 1000:.0f} ms'
    )
    await interaction.response.send_message(embed=embed)

  @nextcord.slash_command('stop', 'Stops Lubot')
  async def stop(self, interaction: Interaction):
    log(f'Lubot stopped by {interaction.user}')
    await interaction.response.send_message('Lubot stopped!')
    # Close bot client
    await self.client.close()

  @nextcord.slash_command('restart', 'Restart Lubot')
  async def restart(self, interaction: Interaction):
    await interaction.response.send_message('Restarting!')
    log('Restarting')
    # Restart the program by replacing the process
    os.execv(sys.executable, ['python3'] + sys.argv)


def setup(client: commands.Bot) -> None:
  client.add_cog(Control(client))