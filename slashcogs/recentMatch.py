import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import json

with open ('././config/api.json', 'r') as f:
	api_heads = json.load(f)
	headers = api_heads["user_agent"]

agent_icons = {
	'Jett' : '<:displayiconsmall:875404905563697184>',
	'Breach' : '<:displayiconsmall14:875404905916039178>',
	'Brimstone' : '<:displayiconsmall5:875404905421090846>',
	'Sage' : '<:displayiconsmall3:875404906641641482>',
	'Cypher' : '<:displayiconsmall10:875404906289311754>',
	'Phoenix' : '<:displayiconsmall6:875404905756627014>',
	'Omen' : '<:displayiconsmall1:875404903273619506>',
	'Viper' : '<:displayiconsmall7:875404906813620234>',
	'Sova' : '<:displayiconsmall9:875404905060368445>',
	'Raze' : '<:displayiconsmall13:875404905781796914>',
	'Reyna' : '<:displayiconsmall2:875404904460595220>',
	'Killjoy' : '<:displayiconsmall8:875404906570321920>',
	'Skye' : '<:displayiconsmall11:875404907052666920>',
	'Yoru' : '<:displayiconsmall15:875404902862569552>',
	'Astra': '<:displayiconsmall4:875404906993954826>',
	'KAY/O': '<:displayiconsmall12:875404906171875369>',
	'Chamber': '<:displayiconsmall20:931574499814539364>',
	'Neon': '<:displayiconsmall21:931575512692822056>',
	'Fade' : '<:fade:997156964989677668>'
}


rank_icons = {
	'Unrated' : '<:Unranked:875258466325909565>',
	'Iron 1' : '<:Iron1:875258466321698816> ',
	'Iron 2' : '<:Iron2:875258467416428555> ',
	'Iron 3' : '<:Iron3:875258469383561256>',
	'Bronze 1' : '<:Bronze1:875258467978461194>',
	'Bronze 2' : '<:Bronze2:875258469433888798> ',
	'Bronze 3' : '<:Bronze3:875258469341618216> ',
	'Silver 1' : '<:Silver1:875258467634536479> ',
	'Silver 2' : '<:Silver2:875258468896997417> ',
	'Silver 3' : '<:Silver3:875258469186420796>',
	'Gold 1' : '<:Gold1:875258468934774794> ',
	'Gold 2' : '<:Gold2:875258470029484102> ',
	'Gold 3' : '<:Gold3:875258470583111680>',
	'Platinum 1' : '<:Platinum1:875258468746002444> ',
	'Platinum 2' : '<:Platinum2:875258469664587776> ',
	'Platinum 3' : '<:Platinum3:875258469735878748> ',
	'Diamond 1' : '<:Diamond1:875258468263661568>',
	'Diamond 2' : '<:Diamond2:875258469731668028> ',
	'Diamond 3' : '<:Diamond3:875258469492617256> ',
	'Immortal 1' : '<:Immortal:875258469303853056>',
	'Immortal 2' : '<:Immortal2:875258469756862494>',
	'Immortal 3' : '<:Immortal3:875258469035438091>',
	'Radiant': '<:Radiant:875258469970759680> '
}


agent_img={
"Breach":"https://media.valorant-api.com/agents/5f8d3a7f-467b-97f3-062c-13acf203c006/displayicon.png",
"Raze":"https://media.valorant-api.com/agents/f94c3b30-42be-e959-889c-5aa313dba261/displayicon.png",
"KAY/O":"https://media.valorant-api.com/agents/601dbbe7-43ce-be57-2a40-4abd24953621/displayicon.png",
"Skye":"https://media.valorant-api.com/agents/6f2a04ca-43e0-be17-7f36-b3908627744d/displayicon.png",
"Cypher":"https://media.valorant-api.com/agents/117ed9e3-49f3-6512-3ccf-0cada7e3823b/displayicon.png",
"Sova":"https://media.valorant-api.com/agents/ded3520f-4264-bfed-162d-b080e2abccf9/displayicon.png",
"Killjoy":"https://media.valorant-api.com/agents/1e58de9c-4950-5125-93e9-a0aee9f98746/displayicon.png",
"Viper":"https://media.valorant-api.com/agents/707eab51-4836-f488-046a-cda6bf494859/displayicon.png",
"Phoenix":"https://media.valorant-api.com/agents/eb93336a-449b-9c1b-0a54-a891f7921d69/displayicon.png",
"Astra":"https://media.valorant-api.com/agents/41fb69c1-4189-7b37-f117-bcaf1e96f1bf/displayicon.png",
"Brimstone":"https://media.valorant-api.com/agents/9f0d8ba9-4140-b941-57d3-a7ad57c6b417/displayicon.png",
"Yoru":"https://media.valorant-api.com/agents/7f94d92c-4234-0a36-9646-3a87eb8b5c89/displayicon.png",
"Sage":"https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/displayicon.png",
"Reyna":"https://media.valorant-api.com/agents/a3bfb853-43b2-7238-a4f1-ad90e9e46bcc/displayicon.png",
"Omen":"https://media.valorant-api.com/agents/8e253930-4c05-31dd-1b6c-968525494517/displayicon.png",
"Jett":"https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/displayicon.png",
"Chamber" : "https://media.valorant-api.com/agents/22697a3d-45bf-8dd7-4fec-84a9e28c69d7/displayicon.png",
"Neon" : "https://media.valorant-api.com/agents/bb2a4828-46eb-8cd1-e765-15848195d751/displayicon.png",
"Fade" : "https://media.valorant-api.com/agents/dade69b4-4f5a-8528-247b-219e5a1facd6/displayicon.png"
}


def GetMatchData(region, user_id):

	history_api = requests.get(f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{user_id}?filter=competitive",headers=headers)
	data = history_api.json()
	
	try:
		matches = data["data"][0]["metadata"]
		return matches["matchid"]
	except:
		return None


def matchStat(match_id):
	match_api = requests.get(f"https://api.henrikdev.xyz/valorant/v2/match/{match_id}",headers=headers)
	data = match_api.json()

	MATCH_DATA = {}
	PLAYER_DATA = {}

	red_team = data["data"]["teams"]["red"]
	blue_team =  data["data"]["teams"]["blue"]
	players = data["data"]["players"]["all_players"][0:10]
	i = 0 

	MATCH_DATA["match_info"] = {}
	MATCH_DATA["match_info"]["map_name"] = data["data"]["metadata"]["map"]
	MATCH_DATA["match_info"]["start"] = data["data"]["metadata"]["game_start_patched"]

	MATCH_DATA["Red"] = {}
	MATCH_DATA["Red"]["rounds_won"] = red_team["rounds_won"]
	MATCH_DATA["Red"]["won"] = red_team["has_won"]

	MATCH_DATA["Blue"] = {}
	MATCH_DATA["Blue"]["rounds_won"] = blue_team["rounds_won"]
	MATCH_DATA["Blue"]["won"] = blue_team["has_won"]
	
	for player in players:
		
		display_username = players[i]["name"]
		display_tag = players[i]["tag"]

		display_name = display_username + display_tag
		team = players[i]["team"]
		agent = players[i]["character"]
		agentImageUrl = agent_img[f"{agent}"]
		rank = players[i]["currenttier_patched"]

		stats = player["stats"]
		score = stats["score"]
		kills = stats["kills"]
		deaths = stats["deaths"]
		assists = stats["assists"]
		kdRatio_cal = kills/deaths
		kdRatio = round(kdRatio_cal , 2)
	   

		
		PLAYER_DATA[display_name] = {}
		PLAYER_DATA[display_name]["team"] = team
		PLAYER_DATA[display_name]["agent"] = agent
		PLAYER_DATA[display_name]["agent_image_url"] = agentImageUrl
		PLAYER_DATA[display_name]["rank"] = rank
		PLAYER_DATA[display_name]["score"] = score
		PLAYER_DATA[display_name]["kills"] = kills
		PLAYER_DATA[display_name]["deaths"] = deaths
		PLAYER_DATA[display_name]["assists"] = assists
		PLAYER_DATA[display_name]["kd_ratio"] = kdRatio

		i += 1
	
	return MATCH_DATA, PLAYER_DATA


class slash_recentmatch(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.slash_command(description="Show your recent competitive match data")
	async def recent(
		self,
		ctx,
	):
		await ctx.response.defer()
		author_id = str(ctx.author.id)
		
		try:

			user = await self.bot.pg_con.fetchrow("SELECT * FROM acclink WHERE userid = $1", author_id)
			userid = user['puuid']
			region   = user['region']
			user_name = user['name']
			tagline = user['tagline']

			try:
			
				match_data = GetMatchData(region,userid)
				
				if match_data == None:
					embed = discord.Embed(
						color = discord.Color.red(),
						description = """
						You haven't played any Competitive Match !!
						"""
					)
					await ctx.respond(embed=embed)

				else:
					match_id = match_data
					
					mch_data , plr_data = matchStat(match_id)
					

					match_map = mch_data['match_info']['map_name']
					match_date = mch_data["match_info"]["start"]
					
					plyr_list = plr_data.keys()

					full_name = f'{user_name}'+f'{tagline}'
					#if full_name in list(plyr_list):
					plyr_agent_img = plr_data[f'{full_name}']['agent_image_url']
					plyr_team_name = plr_data[f'{full_name}']['team']
					
					match_result = mch_data[f'{plyr_team_name}']['won']


					red_team_result = mch_data[f'Red']['won']
					blue_team_result = mch_data[f'Blue']['won']
						
					

					if red_team_result == False and blue_team_result == False:
						match_fnl_result = "Draw"
						avatr_img = "https://raw.githubusercontent.com/picklejason/ValorantRankedPointsBot/main/Resources/stable.png"
					
					elif match_result == True:
						match_fnl_result = "VICTORY"
						avatr_img = "https://i.imgur.com/X6yADlO.png"
					elif match_result == False:
						match_fnl_result = "DEFEAT"
						avatr_img = "https://i.imgur.com/KOiVrrZ.png"

					sorted_players = sorted(plr_data, key=lambda x: int(plr_data[x]["score"]), reverse=True)
					team1 = "**Team 1**\n"
					team2 = "**Team 2**\n"
					for p in sorted_players:

						if plr_data[p]["team"] == "Red":
							team1 += f"{agent_icons[plr_data[p]['agent']]} | {rank_icons[plr_data[p]['rank']]} | {p} | **{plr_data[p]['kills']}**/**{plr_data[p]['deaths']}**/**{plr_data[p]['assists']}** | **{plr_data[p]['kd_ratio']}** K/D | **{plr_data[p]['score']}** ACS\n"
						elif plr_data[p]["team"] == "Blue":
							team2 += f"{agent_icons[plr_data[p]['agent']]} | {rank_icons[plr_data[p]['rank']]} | {p} | **{plr_data[p]['kills']}**/**{plr_data[p]['deaths']}**/**{plr_data[p]['assists']}** | **{plr_data[p]['kd_ratio']}** K/D | **{plr_data[p]['score']}** ACS\n"




					embed = discord.Embed(
						color = 0x00FFFF,
					
						description = team1+'\n'+team2,
					)
					# embed.set_image(url=f"{map_image_url}")
					embed.set_author(name=match_map +' | '+match_fnl_result,icon_url=avatr_img)
					embed.set_footer(text=f"🟢 {match_date} UTC")
					embed.set_thumbnail(url=f"{plyr_agent_img}")

					await ctx.respond(embed=embed)


					
				
				
			except:
				embed= discord.Embed(
					color=discord.Color.red()
				)
				embed.add_field(name ="SOME ERROR OCCURED...",value="""
				Please join our support server to report this error!
				just click on the button given below to continue.
				""",inline=False)

				embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
				
				view = discord.ui.View()
				view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
				view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
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
			use `/h link` to know more!
			""")
			await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(slash_recentmatch(bot))
