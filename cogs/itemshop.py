import requests
import re
import discord
import asyncio
from discord.ext import commands
import json 
from .utils.shop_utils import username_to_data,getVersion,priceconvert,skins,check_item_shop

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class itemshop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        author_id = str(message.author.id)
        user = await self.client.pg_con.fetchrow("SELECT * FROM riotpwd WHERE user_id = $1", author_id)
            
        if message.author != message.author.bot:
            if not message.guild:
                if message.content.startswith('username='):
                    username = message.content.split('=')
                    
                    if not user:
                        await self.client.pg_con.execute("INSERT INTO riotpwd (user_id, username) VALUES ($1, $2)", author_id, username[1])
                        await message.channel.send("Successfully updated your username")
                    if user:
                        await self.client.pg_con.execute("UPDATE riotpwd SET username = $1 WHERE user_id = $2",username[1], author_id)
                        await message.channel.send("Successfully updated your username")
                if message.content.startswith('password='):
                    password = message.content.split('=')
                    
                    await self.client.pg_con.execute("UPDATE riotpwd SET password = $1 WHERE user_id = $2",password[1], author_id)
                    await message.channel.send("Successfully updated your password")
    
    @commands.command()
    async def login(self, ctx):
        embed = discord.Embed(
            color = discord.Color.blue(),
            description = "Check you DM"
        )
        await ctx.send(embed=embed)

        dm_embed = discord.Embed(
            color=0xA6FF0A,
            title="LOGIN PAGE"
        )
        dm_embed.add_field(name ="**username**",value="Enter you valorant username\nfor example \n`username=typhonshambo` if you username is typhonshambo",inline=False)
        dm_embed.add_field(name ="**password**",value="Enter you valorant password\nfor example \n`password=123` if you username is 123",inline=False)
        dm_embed.add_field(name="NOTE",value ="You need to enter you `username` **first** if you are new here!!\nAnd if you write the username or password incorrect \ntype again the same thing to change it")

        await ctx.author.send(embed=dm_embed)
        


    REGION="NA"






    @commands.command()
    async def shop(self, ctx):
        author_id = str(ctx.author.id)
        
        try:
            user = await self.client.pg_con.fetchrow("SELECT * FROM riotpwd WHERE user_id = $1", author_id)
            username = user['username']
            password = user['password']
        except:
            embed = discord.Embed(
                color= discord.Color.red()
            )
            embed.add_field(name ="HOLD ON MAN !",value = f"""
            you need to login to your account before you can use this command,
            use `{prefix}login` to login to your account
            """)
            await ctx.send(embed=embed)
        
        user_in_chat = False
        found = False

        not_user = await self.client.pg_con.fetch("SELECT * FROM riotpwd WHERE user_id = $1", author_id)
        
        if user:
            await ctx.send("Loading shop...")
            user_data = username_to_data(username, password)
            access_token = user_data[0]
            entitlements_token = user_data[1]
            user_id = user_data[2]
            skin_data = skins(entitlements_token, access_token, user_id)
            embed = discord.Embed(title=skin_data["bundle_name"])
            embed.set_image(url=skin_data["bundle_image"])
            await ctx.send(embed=embed)
            try:
                embed = discord.Embed(title=f"{skin_data['skin1_name']} costs {skin_data['skin1_price']}")
                embed.set_image(url=skin_data["skin1_image"])
                await ctx.send(embed=embed)
                embed = discord.Embed(title=f"{skin_data['skin2_name']} costs {skin_data['skin2_price']}")
                embed.set_image(url=skin_data["skin2_image"])
                await ctx.send(embed=embed)
                embed = discord.Embed(title=f"{skin_data['skin3_name']} costs {skin_data['skin3_price']}")
                embed.set_image(url=skin_data["skin3_image"])
                await ctx.send(embed=embed)
                embed = discord.Embed(title=f"{skin_data['skin4_name']} costs {skin_data['skin4_price']}")
                embed.set_image(url=skin_data["skin4_image"])
                await ctx.send(embed=embed)
            except TypeError:
                embed = discord.Embed(title=f"{skin_data['skin1_name']} costs {skin_data['skin1_price']}",)
                embed.set_image(url=skin_data["skin1_image"])
                await ctx.send(embed=embed)
                embed = discord.Embed(title=f"{skin_data['skin2_name']} costs {skin_data['skin2_price']}",)
                embed.set_image(url=skin_data["skin2_image"])
                await ctx.send(embed=embed)
                embed = discord.Embed(title=f"{skin_data['skin3_name']} costs {skin_data['skin3_price']}",)
                embed.set_image(url=skin_data["skin3_image"])
                await ctx.send(embed=embed)
                embed = discord.Embed(title=f"{skin_data['skin4_name']} costs {skin_data['skin4_price']}",)
                embed.set_image(url=skin_data["skin4_image"])
                await ctx.send(embed=embed)








def setup(client):
    client.add_cog(itemshop(client))
    print("itemshop     | Imported")