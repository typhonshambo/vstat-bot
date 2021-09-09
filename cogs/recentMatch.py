import discord
from discord.ext import commands
from discord_components import *
import json
from .utils.recentMatch_utils import username_to_data, getingamename, GetMatchData, matchStat
from .utils import match_resource as res 
from datetime import datetime

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']


class recentMatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

            


    @commands.command()
    async def recent(self, ctx):
        author_id = str(ctx.author.id)
        

        try:
            user = await self.bot.pg_con.fetchrow("SELECT * FROM riotpwd WHERE user_id = $1", author_id)
            username = user['username']
            password = user['password']
            region   = user['region']

            try:
                await ctx.send('loading...')
                login = username_to_data(username,password)
                user_id = login[2]
                
                ingamename = getingamename(region,user_id)
                user_name = ingamename['data']['name']
                tagline = ingamename['data']['tag']

                match_data = await GetMatchData(region,user_id)

                if match_data == None:
                    embed = discord.Embed(
                        color = discord.Color.red(),
                        description = """
                        You haven't played any Competitive Match !!
                        """
                    )
                    await ctx.send(embed=embed)

                else:
                    match_id = match_data
                    
                    mch_data , plr_data = matchStat(match_id)
                    

                    match_map = mch_data['match_info']['map_name']
                    match_date = mch_data["match_info"]["start"]
                    
                    plyr_list = plr_data.keys()

                    full_name = f'{user_name}'+f'{tagline}'
                    if full_name in list(plyr_list):
                        plyr_agent_img = plr_data[f'{full_name}']['agent_image_url']
                        plyr_team_name = plr_data[f'{full_name}']['team']
                        
                        match_result = mch_data[f'{plyr_team_name}']['won']


                        red_team_result = mch_data[f'Red']['won']
                        blue_team_result = mch_data[f'Blue']['won']
                        
                    

                        if red_team_result == False and blue_team_result == False:
                            match_fnl_result = "Draw"
                            avatr_img = "https://raw.githubusercontent.com/picklejason/ValorantRankedPointsBot/main/Resources/stable.png"
                        
                        elif match_result == True:
                            match_fnl_result = "VICTORY"
                            avatr_img = "https://i.imgur.com/X6yADlO.png"
                        elif match_result == False:
                            match_fnl_result = "DEFEAT"
                            avatr_img = "https://i.imgur.com/KOiVrrZ.png"

                    sorted_players = sorted(plr_data, key=lambda x: int(plr_data[x]["score"]), reverse=True)
                    team1 = "**Team 1**\n"
                    team2 = "**Team 2**\n"
                    for p in sorted_players:

                        if plr_data[p]["team"] == "Red":
                            team1 += f"{res.agent_icons[plr_data[p]['agent']]} | {res.rank_icons[plr_data[p]['rank']]} | {p} | **{plr_data[p]['kills']}**/**{plr_data[p]['deaths']}**/**{plr_data[p]['assists']}** | **{plr_data[p]['kd_ratio']}** K/D | **{plr_data[p]['score']}** ACS\n"
                        elif plr_data[p]["team"] == "Blue":
                            team2 += f"{res.agent_icons[plr_data[p]['agent']]} | {res.rank_icons[plr_data[p]['rank']]} | {p} | **{plr_data[p]['kills']}**/**{plr_data[p]['deaths']}**/**{plr_data[p]['assists']}** | **{plr_data[p]['kd_ratio']}** K/D | **{plr_data[p]['score']}** ACS\n"




                    embed = discord.Embed(
                        color = 0x00FFFF,
                    
                        description = team1+'\n'+team2,
                    )
                    # embed.set_image(url=f"{map_image_url}")
                    embed.set_author(name=match_map +' | '+match_fnl_result,icon_url=avatr_img)
                    embed.set_footer(text=f"🟢 {match_date} UTC")
                    embed.set_thumbnail(url=f"{plyr_agent_img}")
                    



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



def setup(bot):
    bot.add_cog(recentMatch(bot))
    print("recentMatch  | Imported")   