import discord
from discord.ext import commands
from discord_components import *

class aceSound(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command(aliases = ['as','ace'])
	async def acesound(self, ctx):
		await ctx.send("Select a collection",
			components=[
				Select(placeholder='bundles',
				options=[
					SelectOption(label="BlastX",value="blastX"),
					SelectOption(label="Enderflame",value="Enderflame"),
					SelectOption(label="Glitchpop",value="glitchpop"),
					SelectOption(label="Ion",value="Ion"),
					SelectOption(label="Oni",value="Oni"),
					SelectOption(label="Prime",value="Prime"),
					SelectOption(label="Prime 2.0",value="Prime 2.0"),
					SelectOption(label="Reaver",value="Reaver"),
					SelectOption(label="Sovereign",value="Sovereign")
					])
			]
		)
		_res = await self.client.wait_for("select_option", check=lambda i: i.component[0])

		if _res.user == ctx.author:
			if _res.component[0].value=="blastX":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="BlastX"
				)
				embed.set_image(url="https://cdn.oneesports.gg/cdn-data/wp-content/uploads/sites/2/2020/12/BlastX_Graphic-1024x576.jpg")
				embed.set_author(name="blastX",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/blastX.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928149554077726/blastX.mp3")])

		if _res.user == ctx.author:
			if _res.component[0].value=="Enderflame":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Enderflame"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2020/07/Valorant-Elderflame-Collection-HD.jpg")
				embed.set_author(name="Enderflame",icon_url="https://cdn.discordapp.com/attachments/868928100048728136/868928149663146044/Enderflame.mp3")
				
				file = discord.File("././assets/acesound/Enderflame.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928149554077726/blastX.mp3")])
		if _res.user == ctx.author:
			if _res.component[0].value=="glitchpop":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Glitchpop"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2020/08/Valorant-Glitchpop-Collection-HD-1024x576.jpg")
				embed.set_author(name="Glitchpop",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/glitchpop.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928150787215421/glitchpop.mp3")])

		if _res.user == ctx.author:
			if _res.component[0].value=="Ion":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Ion"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2020/11/Valorant-Ion-Collection-HD.jpg")
				embed.set_author(name="Ion",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/Ion.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928151898689556/Ion.mp3")])
		
		if _res.user == ctx.author:
			if _res.component[0].value=="Oni":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Oni"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2020/07/Valorant-Oni-Collection-HD.jpg")
				embed.set_author(name="Oni",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/oni.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928135318630441/oni.mp3")])
		
		if _res.user == ctx.author:
			if _res.component[0].value=="Prime":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Prime"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2020/06/Valorant-Prime-Collection.jpg")
				embed.set_author(name="Prime",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/prime.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928140578259005/prime.mp3")])

		if _res.user == ctx.author:
			if _res.component[0].value=="Prime 2.0":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Prime 2.0"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2021/03/Valorant-Prime-2-Collection-HD.jpg")
				embed.set_author(name="Prime 2.0",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/Prime 2.0.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928139156406333/Prime_2.0.mp3")])

		if _res.user == ctx.author:
			if _res.component[0].value=="Reaver":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Reaver"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2020/10/Valorant-Reaver-Collection-HD.jpg")
				embed.set_author(name="Reaver",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/Reaver.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928143010975744/Reaver.mp3")])

	
		if _res.user == ctx.author:
			if _res.component[0].value=="Sovereign":
				embed = discord.Embed(
					color=0x0AFFE9,
					title="Sovereign"
				)
				embed.set_image(url="https://valorantstrike.com/wp-content/uploads/2020/06/Valorant-Sovereign-Collection-HD.jpg")
				embed.set_author(name="Sovereign",icon_url="https://raw.githubusercontent.com/SudhanPlayz/Discord-MusicBot/master/assets/logo.gif")
				
				file = discord.File("././assets/acesound/Sovereign.mp3")
				
				await ctx.send(embed=embed)
				await ctx.send(file=file, components=[Button(label="Download", style=5, url="https://cdn.discordapp.com/attachments/868928100048728136/868928146706137098/Sovereign.mp3")])

	
	
def setup(client):
	client.add_cog(aceSound(client))
	print("ace          | Imported")   