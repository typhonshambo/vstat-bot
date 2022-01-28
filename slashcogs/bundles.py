import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import urllib.request as urllib
import json 
import difflib

def bundle_list(link):
	url = urllib.urlopen(link)
	bundles_list = []
	j = json.loads(url.read())
	for i in range(len(j["data"])):
		data = (j["data"][i]["displayName"])
		bundles_list.append(data)
	return bundles_list

def bundle_get_image(link, i):
	url = urllib.urlopen(link)
	bundles_img = ""
	j = json.loads(url.read())
	data = (j["data"][i]["displayIcon"])
	bundles_img += data 
	return bundles_img



class slash_bundles(commands.Cog):
		def __init__(self, bot):
			self.bot = bot
	
		@commands.slash_command(description="Get info. about bundle")
		async def bundles(
			self,
			ctx,
			search: Option(str, "Enter bundle name", required=False)
		):
			await ctx.response.defer()
			if search == None:
					
				r = bundle_list("https://valorant-api.com/v1/bundles")
				result_str = "▫"+"""\n▫""".join(str(e) for e in r)
				embed = discord.Embed(
					colour = discord.Colour.green()
				)            
				embed.add_field(name ="Bundles",value=result_str)
				view = discord.ui.View()
				view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
				view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
				await ctx.respond(embed=embed, view=view)
				
			elif search != None:
				r = bundle_list("https://valorant-api.com/v1/bundles")
				if search not in r :
					result_list = difflib.get_close_matches(search, r)
					result_str = "▫"+"""\n▫""".join(str(e) for e in result_list)

					embed = discord.Embed(
						color= 0x0AECFF
					)
					embed.add_field(name ="NO BUNDLE FOUND!", value=f"""
					make sure you type the `first letter capital` and `spell` it correcly
					To get the list of Bundles use `/bundle`
					""")
					embed.add_field(name ="SIMILAR BUNDLES",value=result_str, inline=False)
					
					view = discord.ui.View()
					view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
					view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
				
					await ctx.respond(embed=embed, view=view)

				try:
					index_value = r.index(f'{search}')
					img = bundle_get_image("https://valorant-api.com/v1/bundles", index_value)
					embed = discord.Embed(
						color = 0x0AECFF,
						title=f"{search}"
					)
					embed.set_image(url=f"{img}")
					await ctx.respond(embed=embed)
				except:
					pass

def setup(bot):
	bot.add_cog(slash_bundles(bot))