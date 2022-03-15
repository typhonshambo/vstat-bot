import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import json
import psutil
import sys
import requests

with open ('./././extension/emoji.json', 'r') as f:
	emojidata = json.load(f)

with open ('./././config/config.json', 'r') as f:
	topgg_data = json.load(f)
	topgg_botid = topgg_data["topgg_botid"]
	togg_token = topgg_data["topgg_token"]

def getVotes(topgg_botid):
	Authorization = {
		"Authorization" : togg_token
	}
	r = requests.get(f"https://top.gg/api/bots/{topgg_botid}/votes", headers=Authorization)
	data = r.json()
	
	return len(data)



class slash_botInfo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(guild_ids=[864779702554984458,556197206147727391],description="BOT info.")
	async def info(
		self,
		ctx
	):
		cpuEmote = emojidata["cpu"]
		ramEmote = emojidata["ram"]
		storageEmote = emojidata["storage"]
		pythonEmote = emojidata["python"]
		voteEmote = emojidata["vote"]
		codeEmote = emojidata["code"]

		await ctx.response.defer()
		
		embed = discord.Embed(
			color = discord.Color.random(),
			description=f"""
			> {codeEmote} `PYCORD Version` - {discord.__version__}
			> {pythonEmote} `Py Version` - {sys.version_info[0]}
			> {cpuEmote} `CPU` -  {psutil.cpu_percent()}%
			> {storageEmote} `Storage` - {psutil.disk_usage('/')[3]}%
			> {ramEmote} `RAM` - {psutil.virtual_memory()[2]}%
			> {voteEmote} `Votes` - {getVotes(topgg_botid)}
			"""
		)
		await ctx.respond(embed=embed)

def setup(bot):
	bot.add_cog(slash_botInfo(bot))