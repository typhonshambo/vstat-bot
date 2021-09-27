from re import split
import discord
from discord.ext import commands
from discord_components import *
from .utils.acclink_utils import accountData
from discord.ext.commands.errors import MissingRequiredArgument
import json

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class aceSound(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def link(self, ctx, * ,name:str):
		try:
			author_id = str(ctx.author.id)
			user = await self.client.pg_con.fetchrow("SELECT * FROM acclink WHERE userid = $1", author_id)

			username = name.split('#')
			if not user:
				puuid , region = accountData(username[0], username[1])
				await self.client.pg_con.execute("INSERT INTO acclink (userid, name, tagline, puuid, region) VALUES ($1, $2, $3, $4, $5)", author_id, username[0], username[1], str(puuid), str(region))
				embed = discord.Embed(
					color = discord.Color.green(),
					description="Successfully linked"
				)
				await ctx.reply(embed=embed)

			if user:
				puuid , region = accountData(username[0], username[1])
				await self.client.pg_con.execute("UPDATE acclink SET name = $1, tagline = $2, puuid=$3, region=$4  WHERE userid = $5",username[0], username[1],str(puuid), str(region), author_id)
				embed = discord.Embed(
					color = discord.Color.green(),
					description="Successfully linked"
				)
				await ctx.reply(embed=embed)
		except:
			embed = discord.Embed(
				color = discord.Color.red(),
				description="Some error occured"
			)
			await ctx.send(
				embed=embed,
				components=[
					[
						Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
						Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote")
					]
				]
			)
	@link.error
	async def link_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):

			text = discord.Embed(
				description = f'Sorry {ctx.message.author.mention}, You need to give `name` and `tagline` both!',
				color = discord.Color.red(),
				title = f"What?"
			)
			text.add_field(name ="USAGE", value = f"`{prefix}link <name>#<tagline>`\n e.g. `{prefix}link TYshambo#0001` ")
			await ctx.send(
				embed=text,
				components=[
					[
						Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
						Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote")
					]
				]
			)


			
def setup(client):
	client.add_cog(aceSound(client))
	print("link         | Imported")   