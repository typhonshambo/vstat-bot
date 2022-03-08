import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import difflib
import string
import json

with open ('././config/api.json', 'r') as f:
	api_heads = json.load(f)
	headers = api_heads["user_agent"]

def skin_list():
    r = requests.get("https://valorant-api.com/v1/weapons/skins",headers=headers)
    data = r.json()

    SKIN_LIST = []
    SKIN_PUUIDS  = {}

    for i in range(len(data["data"])):
        keys = data["data"][i]["displayName"]
        values = data["data"][i]["uuid"]
        SKIN_LIST.append(keys) 
        SKIN_PUUIDS[keys] = values
    
    return SKIN_LIST, SKIN_PUUIDS

def skin_data(puuid):
    r = requests.get(f"https://valorant-api.com/v1/weapons/skins/{puuid}",headers=headers)
    data = r.json()

    return data


class slash_skins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description="Get Skin info.")
    async def skin(
        self,
        ctx,
        name: Option(str, "Enter name of the skin", required=True),
        level: Option(int, "Enter Skin level", required=True),
        
    ):  
        await ctx.response.defer()
        
        skin_lst, skin_uuid  = skin_list()
        
        try:
            if name in skin_lst:

                uuid = skin_uuid[name]
                DATA = skin_data(str(uuid))
                skin_levels_count  = len(DATA["data"]["levels"])



                #level amount filter
                if level > skin_levels_count:
                    embed = discord.Embed(
                        color = discord.Colour.random(),
                        description = f"The level of this skin cannot go above {skin_levels_count}"
                    )
                    await ctx.respond(embed=embed)

                else: 
                    level -= 1 

                    displayIcon = DATA["data"]["displayIcon"]
                    skin_image = DATA["data"]["levels"][level]["displayIcon"]
                    steam_video = DATA["data"]["levels"][level]["streamedVideo"]
                    
                    #Display Icon FIlder
                    if displayIcon == "null" or displayIcon == None:
                        #steam Video filter
                        if steam_video == "null" or steam_video == None:
                            embed = discord.Embed(
                                color = discord.Color.random(),

                            )
                            embed.set_image(url=skin_image)
                            await ctx.respond(embed=embed)
                        
                        elif steam_video != "null" or steam_video == None:         
                            embed = discord.Embed(
                                color = discord.Color.random(),

                            )
                            embed.set_image(url=skin_image)
                            view = discord.ui.View()
                            view.add_item(discord.ui.Button(label='Video', url=steam_video, style=discord.ButtonStyle.url, emoji='<:video:943457758559211551>'))
                            
                                
                            await ctx.respond(embed=embed,view=view)
                            
                    else:
                        if steam_video == "null" or steam_video == None:
                            embed = discord.Embed(
                                color = discord.Color.random(),

                            )
                            embed.set_image(url=displayIcon)
                            await ctx.respond(embed=embed)
                        
                        elif steam_video != "null" or steam_video == None:         
                            embed = discord.Embed(
                                color = discord.Color.random(),

                            )
                            embed.set_image(url=displayIcon)
                            view = discord.ui.View()
                            view.add_item(discord.ui.Button(label='Video', url=steam_video, style=discord.ButtonStyle.url, emoji='<:video:943457758559211551>'))
                            
                                
                            await ctx.respond(embed=embed,view=view)
            
            if name not in skin_lst:
                result_list = difflib.get_close_matches(name, skin_lst)
                result_str = "▫"+"""\n▫""".join(str(e) for e in result_list)

                embed = discord.Embed(
                    color = discord.Color.random(),
                    title = "No Skins Found - Some similar results",
                    description = result_str
                )
                embed.set_footer(text="Make sure of those capital letters also!")
                await ctx.respond(embed=embed)

        except:
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
            view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
			
            embed = discord.Embed(
                    color = discord.Color.random(),
                    description = "No data found for that skin",
            )
            await ctx.respond(embed=embed, view=view)


		

def setup(bot):
	bot.add_cog(slash_skins(bot))