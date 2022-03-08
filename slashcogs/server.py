import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import json 

with open ('././config/api.json', 'r') as f:
	api_heads = json.load(f)
	headers = api_heads["user_agent"]

def get_erros(region):
	r  = requests.get(f"https://api.henrikdev.xyz/valorant/v1/status/{region}", headers=headers)

	data = r.json()

	if len(data["data"]["incidents"]) == 0:
		return "No error has occured"

	else:
		
		return data["data"]["incidents"][0]["updates"][0]["translations"][0]["content"]
		

class slash_server(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(description="Get server status info.")
	async def server(
			self,
			ctx,
			region: Option(str, "Provide region", required=True)
	):
		try:
			await ctx.response.defer()
			statement = get_erros(region)
			embed = discord.Embed(
				color = discord.Color.random(),
				timestamp=discord.utils.utcnow()
			)
			embed.add_field(name=f"Server Status : {region}", value="`Statement` : "+str(statement))
			await ctx.respond(embed=embed)
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
	bot.add_cog(slash_server(bot))