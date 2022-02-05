import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
import requests

def getleaderboard(region , amount):
	raw_data = requests.get(f"https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}")
	data = raw_data.json()

	PLAYER_DATA = {}
	

	i = 0

	
	for i in range(0, amount):
		name = data[i]['gameName']
		tagLine = data[i]['tagLine']
		leaderboardRank = data[i]['leaderboardRank']
		numberOfWins = data[i]['numberOfWins']
		rankedRating = data[i]['rankedRating']
		
		PLAYER_DATA[i] = {}
		PLAYER_DATA[i]['name'] = name
		PLAYER_DATA[i]['tagLine'] = tagLine
		PLAYER_DATA[i]['leaderboard'] = leaderboardRank
		PLAYER_DATA[i]['numberOfWins'] = numberOfWins
		PLAYER_DATA[i]['rankedRating'] = rankedRating
		i += 1
	return PLAYER_DATA

class slash_leaderboard(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="Get Leaderboard of Top players")
	async def leaderboard(
		self,
		ctx,
		region: Option(str, "Get leaderboard for your region", required=True),
		amount: Option(int, "Number of players you want in leaderboard", default=10, required=False)
	):
		try:
			await ctx.response.defer()

			if amount <= 50:
				
				
				data = getleaderboard(region , amount)

				i = 0
				
				playerNameList = []
				numberOfWins = []
				rankedRating = []
				for i in range(0, amount):
					name = data[i]['name']
					tagline = data[i]['tagLine']
					fullname = name+'#'+tagline
					noOfWins = data[i]['numberOfWins']
					rank_rating = data[i]['rankedRating']

					playerNameList.append(fullname)
					numberOfWins.append(noOfWins)
					rankedRating.append(rank_rating)
				
				leaderboard = "• "+"""\n• """.join(str(e) for e in playerNameList)  
				wins ="""\n""".join(str(e) for e in numberOfWins)
				rr = """\n""".join(str(e) for e in rankedRating)

				embed = discord.Embed(
					color = 0x33FFD1
				)
				embed.add_field(name = "LEADERBOARD", value =leaderboard,inline=True)
				embed.add_field(name = "WINS", value=wins, inline=True)
				embed.add_field(name = "RR", value=rr, inline=True)
				embed.set_thumbnail(url="https://media.valorant-api.com/competitivetiers/e4e9a692-288f-63ca-7835-16fbf6234fda/24/largeicon.png")
				
				view = discord.ui.View()
				view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
				view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
				await ctx.respond(
					embed=embed,
					view=view
				)

			else:
				embed = discord.Embed(
					color = 0x33FFD1,
					description = "Please make sure you give a amount which is less than or equal to `50`!"
				)
							
				view = discord.ui.View()
				view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
				view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
				await ctx.respond(
					embed=embed,
					view=view
				)

		except:	
			embed = discord.Embed(
				color=discord.Color.random(),
				description="The provided region is invalid\nNot sure about your region?\nuse `/profile` to know your region"
			)
			view = discord.ui.View()
			view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
			view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
			await ctx.respond(embed=embed, view=view)


def setup(bot):
	bot.add_cog(slash_leaderboard(bot))