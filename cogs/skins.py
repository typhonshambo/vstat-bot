import discord
from discord.ext import commands
from .valinfo import getValorantInfo
from discord.ext.commands import MissingRequiredArgument
import json

with open ('./config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']




class skin(commands.Cog):
    def __init__(self, client):
        self.client = client




    @commands.command()
    async def patch(self, message):
        await message.channel.send("Find the patch notes for the recent patch here: https://playvalorant.com/en-us/news/game-updates/valorant-patch-notes-1-03/")

    @commands.command(aliases=['gun'])
    async def guns(self, ctx, message:str):
 
        valorantGuns = ["classic", "shorty", "frenzy", "ghost", "sheriff", "stinger", "spectre", "bucky", "judge", "bulldog",
                        "guardian", "vandal", "phantom", "marshall", "operator", "odin", "ares"]
        response = ""
        responseJSON = getValorantInfo()
        gun = message
        print(gun)

        try:

            if gun.lower() in valorantGuns:

                for i in range(0, len(responseJSON['skins'])):

                    if gun.lower() in responseJSON['skins'][i]['name'].lower():
                        print(responseJSON['skins'][i]['name'])
                        response = response + "\n" + "•"+responseJSON['skins'][i]['name']



            embed = discord.Embed(
                colour=discord.Colour.green()
            )
            embed.add_field(name =f"Gun skins for: {gun}", value = response)
            await ctx.channel.send(embed=embed)
            return
        except:
            await ctx.channel.send("Gun does not exist")        

    @guns.error
    async def guns_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
                description='',
                color=discord.Color.orange()
            )
            embed.add_field(name ="❌Your need to give name of the gun",value=f"`{prefix}guns <item>`", inline=False)
            embed.add_field(name = "GUN LIST", value =f"use `{prefix}gunlist` or `{prefix}gunl`")
            await ctx.send(embed=embed)



    @commands.command(aliases=['gunl'])
    async def gunlist(self, ctx):

        embed = discord.Embed(
            color = discord.Color.green()
        )
        embed.add_field(name ="GUN LIST", value = """
        classic 
        shorty
        frenzy
        ghost
        sheriff 
        stinger
        spectre 
        bucky 
        judge
        bulldog
        guardian
        vandal 
        phantom
        marshall 
        operator 
        odin
        ares
        """)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(skin(client))
    print("skins        | Imported")        