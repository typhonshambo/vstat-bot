import discord
from discord.ext import commands
import requests
import json 
from .utils.profile_utils import profile_stats, username_to_data, getingamename
from discord_components import *
import traceback
from datetime import datetime


with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def profile(self, ctx):
        author_id = str(ctx.author.id)
        try:
            
            user = await self.client.pg_con.fetchrow("SELECT * FROM riotpwd WHERE user_id = $1", author_id)
            username = user['username']
            password = user['password']
            region   = user['region']

            try:
                if user:
                    await ctx.send("Loading profile...")
                    user_data = username_to_data(username, password)
                    user_id = user_data[2]
                    raw_ingame_user = getingamename(region, user_id)

                    ingame_username = raw_ingame_user['data']['name']
                    ingame_tag = raw_ingame_user['data']['tag']
                    player_name = ingame_username+ingame_tag
                    ranking_in_tier = raw_ingame_user['data']['current_data']['ranking_in_tier']

                    profile = await profile_stats(ingame_username,ingame_tag)
                    rank = profile["rank"]

                    win_square = int(round(float(profile["win_pct"].rstrip("%")) / 10, 1))
                    loss_square = 10 - win_square
                    bar = win_square * "🟩" + loss_square * "🟥"

                    description = f"{profile['wins']} W {bar} {profile['losses']} L\nWinrate: {profile['win_pct']}"
                    if user:
                
                        rr = f"**{ranking_in_tier} / 100** RR\n"

                    embed = discord.Embed(
                        title=rank,
                        description=description, 
                        timestamp=datetime.utcnow(), 
                        color = 0x02FCCF
                    )
                    embed.set_thumbnail(url=profile["rankIconUrl"])
                    embed.set_author(name=player_name, icon_url=profile["avatarUrl"],url=profile["avatarUrl"])
                    embed.add_field(name="Rank Rating",value=rr,inline=False)
                    embed.add_field(name="K/D Ratio", value=profile["kd_ratio"])
                    embed.add_field(name="ADR", value=profile["damagePerRound"])
                    embed.add_field(name="Headshots %", value=profile["hs_pct"])
                    embed.add_field(name="Time Played", value=profile["time_played"], inline=False)

                    footer = (
                        "🟢 Powered by Tracker.gg"
                    )
                    embed.set_footer(text=footer)
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
            """,inline=False)
            embed.add_field(name="ALSO MAKE SURE THAT..",value="""
            you are logged in into tracker.gg, because profile command is powered by tracker.gg
            to login [click here](https://cutt.ly/kQAIcX1)
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


def setup(client):
    client.add_cog(profile(client))
    print("profile      | Imported")   