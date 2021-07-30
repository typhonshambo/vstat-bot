import discord
from discord.ext import commands
from discord_components import *
import datetime


class spec(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['spec','specs'])
	async def specification(self, ctx):
		embed = discord.Embed(
			color=0xFF9B0A,
			title="PC SPECS REQUIRED FOR VALORANT",
			timestamp=datetime.datetime.utcnow()
		)
		embed.add_field(name="Minimum Specs - 30 fps", value="""
		   :small_blue_diamond:  CPU: Intel i3-370M
		   :small_blue_diamond:  GPU: Intel HD 3000
		""",inline=False)
		embed.add_field(name="Recommended Specs - 60 fps", value="""
		   :small_blue_diamond:  CPU: Intel Core i5-4460 3.2GHz
		   :small_blue_diamond:  GPU: GTX 1050 Ti or higher
		""",inline=False)
		embed.add_field(name="High-end Specs - 144+ fps", value="""
		   :small_blue_diamond:  CPU: Intel i3-4150
		   :small_blue_diamond:  GPU: Geforce GT 730
		""",inline=False)
		embed.add_field(name="PC hardware recommendations", value="""
		   :small_orange_diamond:  Windows 7/8/10 64-bit
		   :small_orange_diamond:  4GB RAM [minimum]
		   :small_orange_diamond:  1GB of VRAM [minimum]
		""",inline=False)
		embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
		await ctx.send(
			embed=embed,
			components=[
					[
						Button(label="Check", style=5, url="https://www.systemrequirementslab.com/cyri/requirements/valorant/19638"),
						Button(label="Support Server", style=5, url="https://cutt.ly/lQa3au0")
					]
				]
		)



def setup(client):
	client.add_cog(spec(client))
	print("specs        | Imported")