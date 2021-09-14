import discord
from discord.ext import commands
from .utils.leaderboard_api import getleaderboard
from discord.ext.commands.errors import MissingRequiredArgument
from discord_components import *
import json

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class leaderboard(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(aliases=['lb'])
    async def leaderboard(self, ctx, region, amount:int):
        if amount <= 50:
        
            await ctx.send("loading...")

            data = getleaderboard(region , amount)

            i = 0
            
            playerNameList = []
            numberOfWins = []
            rankedRating = []
            for i in range(0, amount):
                name = data[i]['name']
                tagline = data[i]['tagLine']
                fullname = name+'#'+tagline
                noOfWins = data[i]['numberOfWins']
                rank_rating = data[i]['rankedRating']

                playerNameList.append(fullname)
                numberOfWins.append(noOfWins)
                rankedRating.append(rank_rating)
            
            leaderboard = "• "+"""\n• """.join(str(e) for e in playerNameList)  
            wins ="""\n""".join(str(e) for e in numberOfWins)
            rr = """\n""".join(str(e) for e in rankedRating)

            embed = discord.Embed(
                color = 0x33FFD1
            )
            embed.add_field(name = "LEADERBOARD", value =leaderboard)
            embed.add_field(name = "WINS", value=wins)
            embed.add_field(name = "RR", value=rr)
            embed.set_thumbnail(url="https://media.valorant-api.com/competitivetiers/e4e9a692-288f-63ca-7835-16fbf6234fda/24/largeicon.png")
            await ctx.send(
                embed=embed,
                components=[
                    [
                        Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
                        Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote")
                    ]
                ]
            )

        else:
            embed = discord.Embed(
                color = 0x33FFD1,
                description = "Please make sure you give a amount which is less than or equal to `50`!"
            )
            await ctx.send(
                embed=embed,
                components=[
                    [
                        Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
                        Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote")
                    ]
                ]
            )
    
    @leaderboard.error
    async def leaderboard_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):

            text = discord.Embed(
                description = f'Sorry {ctx.message.author.mention}, You need to give the `region` and `amount`!',
                color = discord.Color.red(),
                title = f"Something missing..."
            )
            text.add_field(name ="USAGE", value = f"`{prefix}lb <region> <amount>`\n e.g. `{prefix}lb ap 5`", inline=False)
            text.add_field(name ="REGIONS AVAILABLE", value = """
            :white_small_square: `na` - North America
            :white_small_square: `eu` - Europe
            :white_small_square: `br` - Brazil
            :white_small_square: `ap` - Asia Pacific
            :white_small_square: `kr` - Korea
            :white_small_square: `latam` - Latin America
            """)
            text.add_field(name = "NOTE!",value="""
            Make sure that the region you provided is in lower case.
            It's not `AP` it's `ap`
            """)
            text.set_thumbnail(url="https://media.valorant-api.com/competitivetiers/e4e9a692-288f-63ca-7835-16fbf6234fda/24/largeicon.png")
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
    client.add_cog(leaderboard(client))
    print("leaderboard  | Imported")