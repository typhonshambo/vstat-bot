import discord
from discord.ext import commands
from discord.commands import Option, slash_command
from discord_components import *
import requests

def accountData(name, tagline):
	r  = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{name}/{tagline}')
	data = r.json()

	puuid = data['data']['puuid']
	region = data['data']['region']

	return puuid, region

class slash_acclink(commands.Cog):
	def __init__(self, bot):
			self.bot = bot

	@commands.slash_command(guild_ids=[864779702554984458], description="Link to your Valorant account")
	async def link(
		self,
		ctx,
		username: Option(str, "Enter your ingame username", required=True),
		tagline: Option(str, "Enter your ingame tag", required=True),
	):
		await ctx.response.defer()
		author_id = str(ctx.author.id)
		user = await self.bot.pg_con.fetchrow("SELECT * FROM acclink WHERE userid = $1", author_id)

		if not user:
			puuid , region = accountData(username, tagline)
			await self.bot.pg_con.execute("INSERT INTO acclink (userid, name, tagline, puuid, region) VALUES ($1, $2, $3, $4, $5)", author_id, username, tagline, str(puuid), str(region))
			embed = discord.Embed(
				color = discord.Color.random(),
				description="Successfully linked"
			)
			await ctx.respond(embed=embed)

		if user:
			puuid , region = accountData(username, tagline)
			await self.bot.pg_con.execute("UPDATE acclink SET name = $1, tagline = $2, puuid=$3, region=$4  WHERE userid = $5",username, tagline,str(puuid), str(region), author_id)
			embed = discord.Embed(
				color = discord.Color.random(),
				description="Successfully linked"
			)
			await ctx.respond(embed=embed)


	@commands.slash_command(guild_ids=[864779702554984458], description="UnLink to your Valorant account")
	async def unlink(
		self,
		ctx,
	):
		await ctx.response.defer()
		author_id = str(ctx.author.id)
		user = await self.bot.pg_con.fetchrow("SELECT * FROM acclink WHERE userid = $1", author_id)
		
		try: 
			if not user:
				embed = discord.Embed(
					color = discord.Colour.random(),
					description = f"""
					You have not linked your account yet. 
					please link your account first to unlink it.
					user `\help link` to know more 
					"""
				)
				await ctx.respond(embed=embed)

			if user:
				await self.bot.pg_con.fetchval(
					"DELETE FROM acclink WHERE userid = $1", 
					author_id
				)
				embed = discord.Embed(
						color = discord.Colour.random(),
						description="Successfully unlinked"
				)
				await ctx.respond(embed=embed)
		except:
			embed = discord.Embed(
				color = discord.Color.red(),
				description="Some error occured"
			)
			await ctx.respond(embed=embed)


def setup(bot):
	bot.add_cog(slash_acclink(bot))