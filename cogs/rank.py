import discord
from discord.ext import commands
import requests
import json 
from .utils.rank_utils import username_to_data,getrank
from discord_components import *

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class rank(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rank(self, ctx):
        author_id = str(ctx.author.id)
        
        try:
            user = await self.client.pg_con.fetchrow("SELECT * FROM riotpwd WHERE user_id = $1", author_id)
            username = user['username']
            password = user['password']
            region   = user['region']

            try: 
                if user:
                    await ctx.send("Loading rank...")
                    user_data = username_to_data(username, password)
                    user_id = user_data[2]
                    current_rank = getrank(region,user_id)


                    player_rank = current_rank['data']['current_data']['currenttierpatched']
                    current_tier = current_rank['data']['current_data']['currenttier']
                    ranking_in_tier = current_rank['data']['current_data']['ranking_in_tier']
                    mmr_change_to_last_game = current_rank['data']['current_data']['mmr_change_to_last_game']
                    games_needed_for_rating = current_rank['data']['current_data']['games_needed_for_rating']

                    embed = discord.Embed(
                        color=0xFF9B0A,
                        title="RANK"
                    )
                    embed.add_field(name ="Current Rank",value=f"{player_rank}",inline=False)
                    embed.add_field(name ="Ranking in Tier",value=f"{ranking_in_tier}",inline=False)
                    embed.add_field(name ="Games needed for rating",value=f"{games_needed_for_rating}",inline=False)
                    embed.set_thumbnail(url=f"https://raw.githubusercontent.com/typhonshambo/Valorant-server-stat-bot/main/assets/valorantRankImg/{current_tier}.png")



                    await ctx.send(embed=embed)
            except:
                embed= discord.Embed(
                    color=discord.Color.red()
                )
                embed.add_field(name ="SOME ERROR OCCURED...",value="""
                Either your `username` \nor your `password` \nor your `region` is incorrect.
                """,inline=False)
        
                embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
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
            embed = discord.Embed(
                color= discord.Color.red()
            )
            embed.add_field(name ="HOLD ON MAN !",value = f"""
            you need to login to your account before you can use this command,
            use `{prefix}login` to login to your account
            """)
            await ctx.send(embed=embed)
def setup(client):
    client.add_cog(rank(client))
    print("rank         | Imported")   