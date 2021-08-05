import discord
from discord.ext import commands
import requests
from .utils.bundles_utils import bundle_list , bundle_list_img, bundle_get_image
import json
from discord_components import *
from discord.ext.commands.errors import MissingRequiredArgument

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']


class bundles(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['bunl'])
    async def bundlelist(self, ctx):
        r = bundle_list("https://valorant-api.com/v1/bundles")

        embed = discord.Embed(
            colour = discord.Colour.green()
        )            
        embed.add_field(name ="Bundles",value=r)
        await ctx.send(embed=embed)


    @commands.command()
    async def bundle(self, ctx, name:str):


        r = bundle_list_img("https://valorant-api.com/v1/bundles")
        if name not in r :
            embed = discord.Embed(
                color= 0x0AECFF
            )
            embed.add_field(name ="NO BUNDLE FOUND!", value=f"""
            make sure you type the `first letter capital` and `spell` it correcly
            
            To get the list of embed use `{prefix}bunl`
            """)
            await ctx.send(
                embed=embed,
                components=[
                    [
                        Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
                        Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote")
                    ]
                ]
            )
        
        try:
            index_value = r.index(f'{name}')
            img = bundle_get_image("https://valorant-api.com/v1/bundles", index_value)
            embed = discord.Embed(
                color = 0x0AECFF,
                title=f"{name}"
            )
            embed.set_image(url=f"{img}")
            await ctx.send(
                embed=embed,
                components=[
                    [
                        Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
                        Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote")
                    ]
                ]
            )
        
        except:
            pass
            
    @bundle.error
    async def bundle_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):

            text = discord.Embed(
                description = f'Sorry {ctx.message.author.mention}, You need to give the name of the bundle!',
                color = discord.Color.red(),
                title = f"What?"
            )
            text.add_field(name ="USAGE", value = f"`{prefix}bundle <name>`\n e.g. `{prefix}bundle Origin` \n use `{prefix}bunl` to show all bundles available")
            await ctx.send(
                embed=text,
                components=[
                    [
                        Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
                        Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote")
                    ]
                ]
            )
        



def setup(client):
	client.add_cog(bundles(client))
	print("bundles      | Imported")   