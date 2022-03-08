import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import json

with open ('././config/api.json', 'r') as f:
	api_heads = json.load(f)
	headers = api_heads["user_agent"]

def map_data():
	req_data = requests.get("https://valorant-api.com/v1/maps", headers=headers)
	whole_data = req_data.json()

	i = 0
	map_list = []
	map_full_values = {}

	for i in range(len(whole_data["data"])):
		map_list.append(whole_data["data"][i]["displayName"])
		map_name = whole_data["data"][i]["displayName"]
		map_full_values[f"{map_name}"] = whole_data["data"][i]["uuid"]

		i += 1
		
	return map_list, map_full_values

def end_data(puuid):
	req_data = requests.get(f"https://valorant-api.com/v1/maps/{puuid}", headers=headers)
	whole_data = req_data.json()
	
	data = {}
	data['displayName'] = whole_data["data"]["displayName"]
	data['coordinates'] = whole_data["data"]["coordinates"]
	data['splash'] = whole_data["data"]["splash"]
	data['displayIcon'] = whole_data["data"]["displayIcon"]

	return data



class slash_maps(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	map_list, map_full_values = map_data()
	map_list.remove("The Range")
	
	@commands.slash_command(description="Get info. about maps")
	async def maps(
			self,
			ctx,
			map: Option(str, "Choose the agent", choices=map_list, required=True)
		):
			await ctx.response.defer()
			map_list, map_full_values = map_data()
			executive_data = end_data(map_full_values[f'{map}'])

			map_embed = discord.Embed(
				color = discord.Colour.random(),
				title = executive_data['displayName'],
				description = executive_data['coordinates']
			)
			map_embed.set_thumbnail(url=executive_data['splash'])
			map_embed.set_image(url=executive_data['displayIcon'])
			await ctx.respond(embed=map_embed)

def setup(bot):
	bot.add_cog(slash_maps(bot))