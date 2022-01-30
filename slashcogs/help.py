from unicodedata import name
import discord
from discord.ext import commands
from discord.commands import Option, slash_command, SlashCommandGroup
from discord_components import *
import requests
import json

with open ('././extension/help.json', 'r') as f:
	helpdata = json.load(f)
	

class slash_help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	command_list = []
	for keys in helpdata.keys():
		command_list.append(str(keys))		


	@commands.slash_command(guild_ids=[864779702554984458],description="Get help regarding Vstat")
	async def help(
		self,
		ctx,
		helpcommands: Option(str, "Help regarding a specific command", choices=command_list, required=False)
	):
		if helpcommands == None:
			embed = discord.Embed(
				color=0x0AFF4D,
				description="""
				**USER**
				> <:slashcommand:934362483290943598>  `link` - Link Vstat with you valorant account.
				> <:slashcommand:934362483290943598>  `unlink` - Unlinked Linked account.

				**GAME INFO**
				> <:slashcommand:934362483290943598>  `agents` - Get info. about any agent.
				> <:slashcommand:934362483290943598>  `maps` - get info about any map.
				> <:slashcommand:934362483290943598>  `bundles` - Show list of bundles and allows search also.
				> <:slashcommand:934362483290943598>  `weapon` - Show stats and info. of any weapon.
				
				**PLAYER STATS**
				> <:slashcommand:934362483290943598>  `profile` - Show data related to your in-game profile.
				> <:slashcommand:934362483290943598>  `recent` - get you recent competitive match leaderboard.
				> <:slashcommand:934362483290943598>  `leaderboard` - get leaderbord for a region.
				"""
			)
			embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")

			view = discord.ui.View()
			view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
			view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
			await ctx.respond(embed=embed, view=view)


		elif helpcommands != None:
				
			view = discord.ui.View()	
			view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
			view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))

			embed = discord.Embed(
				color = discord.Color.random(), 
			)
			embed.add_field(name="<:slashcommand:934362483290943598> " + helpcommands, value=f"> "+ helpdata[helpcommands]["usage"])
			embed.add_field(name="options", value="> " + helpdata[helpcommands]["options"] + "\n" + "> " + "Required = " + helpdata[helpcommands]["options_req"], inline=False)
			embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
			await ctx.respond(embed=embed, view=view)

def setup(bot): 
	bot.add_cog(slash_help(bot))