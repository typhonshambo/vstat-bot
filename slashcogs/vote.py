import discord
from discord.ext import commands
from discord.commands import Option, slash_command

	

class slash_vote(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="💖")
	async def vote(
		self,
		ctx,
	):
		embed = discord.Embed(
			color=discord.Colour.random(),
			description="> 💖 Thanks for choosing Vstat. You can vote for the BOT by clicking the BIG BUTTON below. It would really motivate us to keep this BOT alive."
		)
		view = discord.ui.View()
		view.add_item(discord.ui.Button(label='♥ Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
		await ctx.respond(embed=embed, view=view)

def setup(bot):
	bot.add_cog(slash_vote(bot))