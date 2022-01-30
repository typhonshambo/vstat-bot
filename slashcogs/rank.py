import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import json
import asyncio

with open ('././config/config.json', 'r') as f:
	config = json.load(f)
	prefix = config['prefix']


def getRank(region, puuid):
	req_data = requests.get(f"https://api.henrikdev.xyz/valorant/v2/by-puuid/mmr/{region}/{puuid}") 
	whole_data = req_data.json()
	
	RANK_DATA = {
		'currenttierpatched' : whole_data['data']['current_data']['currenttierpatched'],
		'currenttier': whole_data['data']['current_data']['currenttier'],
		'ranking_in_tier' : whole_data['data']['current_data']['ranking_in_tier'], 
		'mmr_change_to_last_game' : whole_data['data']['current_data']['mmr_change_to_last_game'], 
		'elo' : whole_data['data']['current_data']['elo'],
		'games_needed_for_rating' : whole_data['data']['current_data']['games_needed_for_rating']
	}

	return RANK_DATA

class slash_rank(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="Get your rank")
	async def rank(
		self,
		ctx
	):
		await ctx.response.defer()

		author_id = str(ctx.author.id)
		
		try:
			user = await self.bot.pg_con.fetchrow("SELECT * FROM acclink WHERE userid = $1", author_id)
			puuid = user['puuid']
			region = user['region']

			try: 
				if user:
		
					RANK_DATA = getRank(region,puuid)


					embed = discord.Embed(
						color=discord.Colour.random(),
						title="RANK",
						timestamp=discord.utils.utcnow()
					)
					embed.add_field(name ="Current Rank",value=f"{RANK_DATA['currenttierpatched']}",inline=False)
					embed.add_field(name ="Ranking in Tier",value=f"{RANK_DATA['ranking_in_tier']}",inline=False)
					embed.add_field(name ="MMR Change last game",value=f"{RANK_DATA['mmr_change_to_last_game']}",inline=False)
					embed.add_field(name ="Elo",value=f"{RANK_DATA['elo']}",inline=False)
					embed.add_field(name ="Games Needed for Rating",value=f"{RANK_DATA['games_needed_for_rating']}",inline=False)

					embed.set_thumbnail(url=f"https://raw.githubusercontent.com/typhonshambo/Valorant-server-stat-bot/main/assets/valorantRankImg/{RANK_DATA['currenttier']}.png")

					view = discord.ui.View()
					view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
					view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
					await ctx.respond(embed=embed, view=view)
			except:
				view = discord.ui.View()
				view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
				view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
				embed= discord.Embed(
					color=discord.Color.red()
				)
				embed.add_field(name ="SOME ERROR OCCURED...",value="""
				Please join our support server to report this error!
				just click on the button given below to continue.
				""",inline=False)
		
				embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
				await ctx.respond(
					embed=embed,
					view=view
				)

		except:
			embed = discord.Embed(
				color= discord.Color.red()
			)
			embed.add_field(name ="HOLD ON MAN !",value = f"""
			you need to link your account before you can use this command,
			use `{prefix}h link` to know more!
			""")
			await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(slash_rank(bot))