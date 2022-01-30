from distutils import errors
import json
import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import json

def profile_info(username, tagline):
	api_Req = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{username}/{tagline}")
	data = api_Req.json()

	VALUE = {}

	VALUE["puuid"] = data["data"]["puuid"]
	VALUE["region"] = data["data"]["region"]
	VALUE["account_level"] = data["data"]["account_level"]
	VALUE["name"] = data["data"]["name"]
	VALUE["tag"] = data["data"]["tag"]
	VALUE["thumbnail"] = data["data"]["thumbnail"] = data["data"]["card"]["small"]
	VALUE["image"] = data["data"]["card"]["wide"]

	return VALUE

def getRank(region, puuid):
	req_data = requests.get(f"https://api.henrikdev.xyz/valorant/v2/by-puuid/mmr/{region}/{puuid}") 
	whole_data = req_data.json()
		
	currenttier =  whole_data['data']['current_data']['currenttier']


	return currenttier
	
class slash_profile(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command( description="Info about your valorant account")
	async def profile(
			self,
			ctx
		):

			await ctx.response.defer()
			author_id = str(ctx.author.id)
			
			try:
				user = await self.bot.pg_con.fetchrow("SELECT * FROM acclink WHERE userid = $1", author_id)
				user_name = user['name']
				tagline = user['tagline']

				data = profile_info(user_name, tagline)
				rank = getRank(data['region'], data['puuid'])

				embed = discord.Embed(
					color = discord.Colour.random(),
					timestamp=discord.utils.utcnow(),
					description= f"""
					:white_small_square: **REGION** - {data["region"]}
					:white_small_square: **ACCOUNT LEVEL** - {data["account_level"]}
					:white_small_square: **NAME** - {data["name"]}
					:white_small_square: **TAG** - {data["tag"]}
					:white_small_square: **PUUID** - {data["puuid"]}
					"""
				)
				embed.set_footer(text="🟢 Linked")
				embed.set_image(url=data["image"])
				embed.set_author(name=data["name"],icon_url=data["thumbnail"])
				embed.set_thumbnail(url=f"https://raw.githubusercontent.com/typhonshambo/Valorant-server-stat-bot/main/assets/valorantRankImg/{rank}.png")
				await ctx.respond(embed=embed)
			
			
			
			except:

				embed = discord.Embed(
					color = discord.Colour.random(),
					description = f"""
					You have not linked your account yet. 
					please link your account first to unlink it.
					user `/link` to do it now.
					"""
				)
				await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(slash_profile(bot))