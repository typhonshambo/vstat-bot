import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import json

with open ('./././extension/emoji.json', 'r') as f:
	emojidata = json.load(f)


class slash_serverlist(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(guild_ids=[864779702554984458,556197206147727391],description="Number of Server")
	async def servercount(
		self,
		ctx
	):
		await ctx.response.defer()
		servercount = str(len(self.bot.guilds))
		embed = discord.Embed(
			color = discord.Color.random(),
			description= f"> `Server Count` : {emojidata['support']} {servercount}"
		)
		await ctx.respond(embed=embed)
		
def setup(bot):
	bot.add_cog(slash_serverlist(bot))