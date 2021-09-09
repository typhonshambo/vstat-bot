import discord
from discord.ext import commands
import psutil
import os

class botProfiler(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command()
	async def ping(self, ctx):

		
		
		memoryAvailablePercent = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 0)

		#cpu usage 
		cpuUsagePercent = psutil.cpu_percent()
		
		embed = discord.Embed(
			color = discord.Color.green(),
			description = f"""
```css
RAM usage : {memoryAvailablePercent} / 100%
```
```css
CPU Usage : {cpuUsagePercent} / 100%
```
			"""
		)
		await ctx.send(embed=embed)
	
def setup(client):
	client.add_cog(botProfiler(client))
	print("profiler     | Imported")