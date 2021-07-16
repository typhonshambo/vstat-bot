import discord
from discord.ext import commands
import json

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class map(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.group(aliases=['maps'], invoke_without_command=True)
    async def map(self, ctx):
        map_list = discord.Embed(
            color=0x0AFF81
        )
        map_list.add_field(name ="MAPS", value ="""
        :white_small_square: Bind
        :white_small_square: Haven 
        :white_small_square: Split 
        :white_small_square: Ascent 
        :white_small_square: Icebox
        :white_small_square: Breeze
        """,inline=False)
        map_list.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        map_list.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif") 
        await ctx.send(embed=map_list)

    @map.command(aliases=['Ascent'])
    async def ascent(self, ctx):
        ascent_des = discord.Embed(
            color=0x0AFF81
        )
        ascent_des.add_field(name ="Ascent", value ="""
        Ascent was the first new map to be added since Valorant’s official release. It is a two site map that is located in Venice, Italy. Compared to the other maps, Ascent has the most open area with a large courtyard at the center of the map.
        \n[source](https://mobalytics.gg/blog/valorant-maps-overview/)
        """)
        ascent_des.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        ascent_des.set_image(url="https://mobalytics.gg/wp-content/uploads/2020/04/ascent.jpg")
        await ctx.send(embed=ascent_des)


    @map.command(aliases=['Bind'])
    async def bind(self, ctx):
        bind_des = discord.Embed(
            color=0x0AFF81
        )
        bind_des.add_field(name ="Bind", value ="""
        A unique aspect of this map is that there are two one-way teleporters. One teleporter takes you from long B to the attacker’s side of showers. The other takes you from short A to the attacker’s side of hookah.
        \n[source](https://mobalytics.gg/blog/valorant-maps-overview/)
        """)
        bind_des.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        bind_des.set_image(url="https://cdnportal.mobalytics.gg/production/2020/04/bind_map_callouts.jpg")
        await ctx.send(embed=bind_des)


    @map.command(aliases=['Haven'])
    async def haven(self, ctx):
        haven_des = discord.Embed(
            color=0x0AFF81
        )
        haven_des.add_field(name ="Haven", value ="""
        Haven is a three site map (A, B, C), which is also its unique aspect as most bomb/defusal maps in FPS games tend to be two sites.
        \n[source](https://mobalytics.gg/blog/valorant-maps-overview/)
        """)
        haven_des.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        haven_des.set_image(url="https://cdnportal.mobalytics.gg/production/2020/04/haven_callouts.jpg")
        await ctx.send(embed=haven_des)

    @map.command(aliases=['Icebox'])
    async def icebox(self, ctx):
        icebox_des = discord.Embed(
            color=0x0AFF81
        )
        icebox_des.add_field(name ="Icebox", value ="""
        Icebox was released at the beginning of Act III and takes place in a tundra climate. The map has a ton of verticality and angles to cover so it’s the most complex map released yet.
        \n[source](https://mobalytics.gg/blog/valorant-maps-overview/)
        """)
        icebox_des.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        icebox_des.set_image(url="https://storage.googleapis.com/usc-main-portal/production/2020/06/709cca30-icebox_callouts.jpg")
        await ctx.send(embed=icebox_des)


    @map.command(aliases=['Split'])
    async def split(self, ctx):
        split_des = discord.Embed(
            color=0x0AFF81
        )
        split_des.add_field(name ="Split", value ="""
        Split was added as of the first day of closed beta. Its two sites are on the far left and right sides of the map with a middle area that provides high ground dominance.
        \n[source](https://mobalytics.gg/blog/valorant-maps-overview/)
        """)
        split_des.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        split_des.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/865319463879442462/split_callouts.png")
        await ctx.send(embed=split_des)


    @map.command(aliases=['Breeze'])
    async def breeze(self, ctx):
        breeze_des = discord.Embed(
            color=0x0AFF81
        )
        breeze_des.add_field(name ="Breeze", value ="""
        Breeze was released during Episode 2 Act 3 at a tropical island location. It’s one of the largest maps in size and features some of the biggest sites in Valorant yet.
        \n[source](https://mobalytics.gg/blog/valorant-maps-overview/)
        """)
        breeze_des.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        breeze_des.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/865320255479873536/ea82cc2d-valorant-breeze-map-article-version.png")
        await ctx.send(embed=breeze_des)

def setup(client):
    client.add_cog(map(client))
    print("map          | Imported")   