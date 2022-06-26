import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import asyncio
import json

with open ('././config/api.json', 'r') as f:
	api_heads = json.load(f)
	headers = api_heads["user_agent"]

def agentData():
    requestData = requests.get("https://valorant-api.com/v1/agents?isPlayableCharacter=true")
    rawData = requestData.json()

    i = 0
    agent_list = []
    agent_full_values = {}

    for i in range(len(rawData["data"])):
        agent_list.append(rawData["data"][i]["displayName"])
        map_name = rawData["data"][i]["displayName"]
        agent_full_values[f"{map_name}"] = rawData["data"][i]["uuid"]

        i += 1

    return agent_list, agent_full_values

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
		

	agent_list, agent_puuid = agentData()
	

	@commands.slash_command(
		description="Get info. about agents")
	async def agents(
		self,
		ctx,
		agent: Option(str, "Choose the agent", choices=agent_list, required=True)
	):

			agent_list, agent_puuid = agentData()
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