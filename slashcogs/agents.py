import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import asyncio
import json

with open ('././config/api.json', 'r') as f:
	api_heads = json.load(f)
	headers = api_heads["user_agent"]

def agent_data(agentUuid):
	req_data = requests.get(f"https://valorant-api.com/v1/agents/{agentUuid}", headers=headers) 
	whole_data = req_data.json()

	data = {
		"description" : whole_data['data']['description'],
		"displayIcon" : whole_data['data']['displayIcon'],
		"bustPortrait" : whole_data['data']['bustPortrait'], 
		"abilities" : whole_data['data']['abilities']
	}
	
	return data

 
class slash_agent(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		

		
	agent_list = ['Breach', 'Raze', 'KAY/O', 'Skye', 'Cypher', 'Sova', 'Killjoy', 'Viper', 'Phoenix', 'Astra', 'Brimstone', 'Yoru', 'Sage', 'Reyna', 'Omen', 'Jett', 'Chamber','Neon','Fade']
	
	

	@commands.slash_command(
		description="Get info. about agents")
	async def agents(
		self,
		ctx,
		agent: Option(str, "Choose the agent", choices=agent_list, required=True)
	):
			agent_puuid = {
				"Breach" : "5f8d3a7f-467b-97f3-062c-13acf203c006",
				"Raze" : "f94c3b30-42be-e959-889c-5aa313dba261",
				"KAY/O" : "601dbbe7-43ce-be57-2a40-4abd24953621",
				"Skye" : "6f2a04ca-43e0-be17-7f36-b3908627744d",
				"Cypher" : "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
				"Sova" : "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
				"Killjoy" : "1e58de9c-4950-5125-93e9-a0aee9f98746",
				"Viper" : "707eab51-4836-f488-046a-cda6bf494859",
				"Astra" : "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
				"Phoenix" : "eb93336a-449b-9c1b-0a54-a891f7921d69",
				"Brimstone" : "9f0d8ba9-4140-b941-57d3-a7ad57c6b417", 
				"Yoru" : "7f94d92c-4234-0a36-9646-3a87eb8b5c89"	,
				"Sage" : "569fdd95-4d10-43ab-ca70-79becc718b46",
				"Reyna" : "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
				"Omen" : "8e253930-4c05-31dd-1b6c-968525494517",
				"Jett" : "add6443a-41bd-e414-f6ad-e58d267f4e95",
				"Chamber" : "22697a3d-45bf-8dd7-4fec-84a9e28c69d7",
				"Neon" : "bb2a4828-46eb-8cd1-e765-15848195d751",
				"Fade" : "dade69b4-4f5a-8528-247b-219e5a1facd6"
			}

			values = agent_data(agent_puuid[f'{agent}'])

			agent_embed = discord.Embed(
				color = discord.Colour.random(),
				title = agent,
				description = values['description']
			)
			agent_embed.set_image(url=values['bustPortrait'])
			agent_embed.set_thumbnail(url=values['displayIcon'])
			agent_embed.add_field(name = f"{values['abilities'][0]['displayName']}", value = f"{values['abilities'][0]['description']}", inline=False)
			agent_embed.add_field(name = f"{values['abilities'][1]['displayName']}", value = f"{values['abilities'][1]['description']}",inline=False)
			agent_embed.add_field(name = f"{values['abilities'][2]['displayName']}", value = f"{values['abilities'][2]['description']}", inline=False)
			agent_embed.add_field(name = f"{values['abilities'][3]['displayName']}", value = f"{values['abilities'][3]['description']}", inline=False)
			await ctx.respond(embed=agent_embed)


def setup(bot):
	bot.add_cog(slash_agent(bot))