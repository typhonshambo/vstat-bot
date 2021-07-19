import discord
from discord.ext import commands
from discord_components import *


class weapon(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['wp','wplist'], invoke_without_command=True)
    async def weapon(self, ctx):

        embed = discord.Embed(
            color = discord.Color.green()
        )
        embed.add_field(name ="GUN LIST", value = """
        :white_small_square: classic 
        :white_small_square: shorty
        :white_small_square: frenzy
        :white_small_square: ghost
        :white_small_square: sheriff 
        :white_small_square: stinger
        :white_small_square: spectre 
        :white_small_square: bucky 
        :white_small_square: judge
        :white_small_square: Bulldog
        :white_small_square: guardian
        :white_small_square: vandal 
        :white_small_square: phantom
        :white_small_square: marshal 
        :white_small_square: operator 
        :white_small_square: odin
        :white_small_square: ares
        """)
        await ctx.send(embed=embed)


    @weapon.command(aliases=['Classic'])
    async def classic(self,ctx):
        classic_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Classic - Sidearm"
        )
        classic_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-Automatic
        :small_blue_diamond: Fire Rate: 6.75 rounds/sec
        """)
        classic_embed.add_field(name="Cost", value ="Free")
        classic_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: 3-Round Burst, spread increase
        :small_blue_diamond: Fire Rate: 2.22 rounds/sec
        """,inline=False)
        classic_embed.add_field(name="Damage",value="""
        Body 26 | Head 78 | Leg 22 - **0-30m**
        Body 22 | Head 66 | Leg 18 - **30-50m**
        """,inline=False)
        classic_embed.add_field(name="Magazine Capacity", value="12")
        classic_embed.add_field(name="Wall Penetration",value="Low")
        classic_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        classic_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/57/Classic.png/revision/latest?cb=20200404154125")
        await ctx.send(
        embed=classic_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/classic")]
        )

    @weapon.command(aliases=['Shorty'])
    async def shorty(self, ctx):
        shorty_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Shorty - Sidearm"
        )
        shorty_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-Automatic
        :small_blue_diamond: Fire Rate: 3.3 rounds/sec
        """)
        shorty_embed.add_field(name="Cost", value ="150")

        shorty_embed.add_field(name="Damage",value="""
        Body 12 | Head 24 | Leg 10 - **0-7m**
        Body 8  | Head 16 | Leg 6  - **7-15m**
        Body 3  | Head 6  | Leg 2  - **15-50m**
        """,inline=False)
        shorty_embed.add_field(name="Magazine Capacity", value="2")
        shorty_embed.add_field(name="Wall Penetration",value="Low")
        shorty_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        shorty_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/7/77/Shorty.png/revision/latest?cb=20200404154222")
        await ctx.send(
        embed=shorty_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/shorty")]
        )


    @weapon.command(aliases=['Frenzy'])
    async def frenzy(self, ctx):
        frenzy_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Frenzy - Sidearm"
        )
        frenzy_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Full-Automatic
        :small_blue_diamond: Fire Rate: 3.3 rounds/sec
        """)
        frenzy_embed.add_field(name="Cost", value ="450")

        frenzy_embed.add_field(name="Damage",value="""
        Body 26 | Head 78 | Leg 22 - **0-20m**
        Body 8  | Head 24 | Leg 6  - **20-50m**
        """,inline=False)
        frenzy_embed.add_field(name="Magazine Capacity", value="13")
        frenzy_embed.add_field(name="Wall Penetration",value="Low")
        frenzy_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        frenzy_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/f1/Frenzy.png/revision/latest?cb=20200404154617")
        await ctx.send(
        embed=frenzy_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/frenzy")]
        )



    @weapon.command(aliases=['Ghost'])
    async def ghost(self, ctx):
        ghost_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Ghost - Sidearm"
        )
        ghost_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-Automatic
        :small_blue_diamond: Fire Rate: 6.75 rounds/sec
        """)
        ghost_embed.add_field(name="Cost", value ="500")

        ghost_embed.add_field(name="Damage",value="""
        Body 30 | Head 105 | Leg 25 - **0-30m**
        Body 25 | Head 87  | Leg 21  - **30-50m**
        """,inline=False)
        ghost_embed.add_field(name="Magazine Capacity", value="15")
        ghost_embed.add_field(name="Wall Penetration",value="Medium")
        ghost_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        ghost_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/a/ab/Ghost.png/revision/latest?cb=20200404154731")
        await ctx.send(
        embed=ghost_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Ghost")]
        )




    @weapon.command(aliases=['Sheriff'])
    async def sheriff(self, ctx):
        sheriff_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Sheriff - Sidearm"
        )
        sheriff_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-Automatic
        :small_blue_diamond: Fire Rate: 4 rounds/sec
        """)
        sheriff_embed.add_field(name="Cost", value ="500")

        sheriff_embed.add_field(name="Damage",value="""
        Body 59 | Head 159 | Leg 46 - **0-30m**
        Body 40 | Head 155  | Leg 42  - **30-50m**
        """,inline=False)
        sheriff_embed.add_field(name="Magazine Capacity", value="6")
        sheriff_embed.add_field(name="Wall Penetration",value="High")
        sheriff_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        sheriff_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/3/3e/Sheriff.png/revision/latest?cb=20200404154438")
        await ctx.send(
        embed=sheriff_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Sheriff")]
        )

    @weapon.command(aliases=['Stinger'])
    async def stinger(self, ctx):
        stinger_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Stinger - SMG"
        )
        stinger_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-Automatic
        :small_blue_diamond: Fire Rate: 16 rounds/sec
        """)
        stinger_embed.add_field(name="Cost", value ="950")
        stinger_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: 4-Round Burst, Aim down sights
        :small_blue_diamond: Fire Rate: 8.471 rounds/sec
        """,inline=False)
        stinger_embed.add_field(name="Damage",value="""
        Body 27 | Head 67 | Leg 22 - **0-20m**
        Body 25 | Head 62  | Leg 21  - **20-50m**
        """,inline=False)
        stinger_embed.add_field(name="Magazine Capacity", value="20")
        stinger_embed.add_field(name="Wall Penetration",value="Low")
        stinger_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        stinger_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/b/b6/Stinger.png/revision/latest?cb=20200404170849")
        await ctx.send(
        embed=stinger_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Stinger")]
        )
   


    @weapon.command(aliases=['Spectre'])
    async def spectre(self, ctx):
        spectre_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Spectre - SMG"
        )
        spectre_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-Automatic
        :small_blue_diamond: Fire Rate: 13.33 rounds/sec
        """)
        spectre_embed.add_field(name="Cost", value ="1,600")
        spectre_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Zoom Mode(1.15x), Aim down sights
        :small_blue_diamond: Fire Rate: 12 rounds/sec
        """,inline=False)
        spectre_embed.add_field(name="Damage",value="""
        Body 26 | Head 78 | Leg 22 - **0-20m**
        Body 22 | Head 66  | Leg 18  - **20-50m**
        """,inline=False)
        spectre_embed.add_field(name="Magazine Capacity", value="30")
        spectre_embed.add_field(name="Wall Penetration",value="Medium")
        spectre_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        spectre_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/9/90/Spectre.png/revision/latest?cb=20200404170922")
        await ctx.send(
        embed=spectre_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Spectre")]
        )

    @weapon.command(aliases=['Bucky'])
    async def bucky(self, ctx):
        bucky_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Bucky - Shotgun"
        )
        bucky_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-Automatic
        :small_blue_diamond: Fire Rate: 1.1 rounds/sec
        """)
        bucky_embed.add_field(name="Cost", value ="850")
        bucky_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Fire a canister that detonates after a short distance, spraying pellets
        :small_blue_diamond: Fire Rate: 1.1 rounds/sec
        """,inline=False)
        bucky_embed.add_field(name="Damage",value="""
        Body 20 | Head 40 | Leg 17 - **0-8m**
        Body 13 | Head 26  | Leg 11  - **8-12m**
        Body 9 | Head 18  | Leg 7  - **12-50m**
        """,inline=False)
        bucky_embed.add_field(name="Magazine Capacity", value="5")
        bucky_embed.add_field(name="Wall Penetration",value="Low")
        bucky_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        bucky_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/e/eb/Bucky.png/revision/latest?cb=20200404171832")
        await ctx.send(
        embed=bucky_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Bucky")]
        )


    @weapon.command(aliases=['Judge'])
    async def judge(self, ctx):
        judge_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Judge - Shotgun"
        )
        judge_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-Automatic
        :small_blue_diamond: Fire Rate: 3.5 rounds/sec
        """)
        judge_embed.add_field(name="Cost", value ="1,850")

        judge_embed.add_field(name="Damage",value="""
        Body 17 | Head 34 | Leg 14 - **0-10m**
        Body 10 | Head 20  | Leg 8  - **10-15m**
        Body 6 | Head 14  | Leg 7  - **15-50m**
        """,inline=False)
        judge_embed.add_field(name="Magazine Capacity", value="7")
        judge_embed.add_field(name="Wall Penetration",value="Low")
        judge_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        judge_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/8/8a/Judge.png/revision/latest?cb=20200404171858")
        await ctx.send(
        embed=judge_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Judge")]
        )

    @weapon.command(aliases=['Bulldog'])
    async def bulldog(self, ctx):
        bulldog_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Bulldog - Rifle"
        )
        bulldog_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-Automatic
        :small_blue_diamond: Fire Rate: 9.5 rounds/sec
        """)
        bulldog_embed.add_field(name="Cost", value ="2,050")
        bulldog_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: (6.555 rounds/sec)2.185 bursts/sec
        """,inline=False)
        bulldog_embed.add_field(name="Damage",value="""
        Body 35 | Head 115  | Leg 29  - **0-50m**
        """,inline=False)
        bulldog_embed.add_field(name="Magazine Capacity", value="24")
        bulldog_embed.add_field(name="Wall Penetration",value="Medium")
        bulldog_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        bulldog_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/0/07/Bulldog.png/revision/latest?cb=20200404171103")
        await ctx.send(
        embed=bulldog_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Bulldog")]
        )


    @weapon.command(aliases=['Guardian'])
    async def guardian(self, ctx):
        guardian_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Guardian - Rifle"
        )
        guardian_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-automatic
        :small_blue_diamond: Fire Rate: 5.25 rounds/sec
        """)
        guardian_embed.add_field(name="Cost", value ="2,250")
        guardian_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 4.275 rounds/sec
        """,inline=False)
        guardian_embed.add_field(name="Damage",value="""
        Body 65 | Head 195  | Leg 49  - **0-50m**
        """,inline=False)
        guardian_embed.add_field(name="Magazine Capacity", value="12")
        guardian_embed.add_field(name="Wall Penetration",value="High")
        guardian_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        guardian_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/fd/Guardian.png/revision/latest?cb=20200404171224")
        await ctx.send(
        embed=guardian_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Guardian")]
        )


    @weapon.command(aliases=['Vandal'])
    async def vandal(self, ctx):
        vandal_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Vandal - Rifle"
        )
        vandal_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-automatic
        :small_blue_diamond: Fire Rate: 9.75 rounds/sec
        """)
        vandal_embed.add_field(name="Cost", value ="2,900")
        vandal_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 8.775 rounds/sec
        """,inline=False)
        vandal_embed.add_field(name="Damage",value="""
        Body 40 | Head 160  | Leg 34  - **0-50m**
        """,inline=False)
        vandal_embed.add_field(name="Magazine Capacity", value="25")
        vandal_embed.add_field(name="Wall Penetration",value="Medium")
        vandal_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        vandal_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/56/Vandal.png/revision/latest?cb=20200404171348")
        await ctx.send(
        embed=vandal_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Vandal")]
        )

    @weapon.command(aliases=['Phantom'])
    async def phantom(self, ctx):
        phantom_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Phantom - Rifle"
        )
        phantom_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-automatic
        :small_blue_diamond: Fire Rate: 11 rounds/sec
        """)
        phantom_embed.add_field(name="Cost", value ="2,900")
        phantom_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 9.9 rounds/sec
        """,inline=False)
        phantom_embed.add_field(name="Damage",value="""
        Body 39 | Head 156  | Leg 33  - **0-15m**
        Body 35 | Head 140  | Leg 29  - **15-30m**
        Body 34 | Head 124  | Leg 26  - **30-50m**
        """,inline=False)
        phantom_embed.add_field(name="Magazine Capacity", value="30")
        phantom_embed.add_field(name="Wall Penetration",value="Medium")
        phantom_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        phantom_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/e/ec/Phantom.png/revision/latest?cb=20200404171302")
        await ctx.send(
        embed=phantom_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Phantom")]
        )

    @weapon.command(aliases=['Marshal'])
    async def marshal(self, ctx):
        marshall_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Marshal - Sniper rifle"
        )
        marshall_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-automatic
        :small_blue_diamond: Fire Rate: 1.5 rounds/sec
        """)
        marshall_embed.add_field(name="Cost", value ="950")
        marshall_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 1.2 rounds/sec
        """,inline=False)
        marshall_embed.add_field(name="Damage",value="""
        Body 101 | Head 202  | Leg 85  - **0-50m**
        """,inline=False)
        marshall_embed.add_field(name="Magazine Capacity", value="5")
        marshall_embed.add_field(name="Wall Penetration",value="Medium")
        marshall_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        marshall_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/b/b9/Marshal.png/revision/latest?cb=20200404172126")
        await ctx.send(
        embed=marshall_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Marshal")]
        )



    @weapon.command(aliases=['Operator'])
    async def operator(self, ctx):
        operator_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Operator - Sniper rifle"
        )
        operator_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Semi-automatic
        :small_blue_diamond: Fire Rate: 0.6 rounds/sec
        """)
        operator_embed.add_field(name="Cost", value ="4,700")
        operator_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 0.75 rounds/sec
        """,inline=False)
        operator_embed.add_field(name="Damage",value="""
        Body 150 | Head 255  | Leg 120  - **0-50m**
        """,inline=False)
        operator_embed.add_field(name="Magazine Capacity", value="5")
        operator_embed.add_field(name="Wall Penetration",value="High")
        operator_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        operator_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/1/17/Operator.png/revision/latest?cb=20200404172152")
        await ctx.send(
        embed=operator_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Operator")]
        )
    


    @weapon.command(aliases=['Odin'])
    async def odin(self, ctx):
        odin_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Odin - Machine gun"
        )
        odin_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-automatic
        :small_blue_diamond: Fire Rate: 12-15.6 rounds/sec
        """)
        odin_embed.add_field(name="Cost", value ="3,200")
        odin_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 15.6 rounds/sec
        """,inline=False)
        odin_embed.add_field(name="Damage",value="""
        Body 38 | Head 95  | Leg 32  - **0-30m**
        Body 31 | Head 77  | Leg 26  - **30-50m**
        """,inline=False)
        odin_embed.add_field(name="Magazine Capacity", value="100")
        odin_embed.add_field(name="Wall Penetration",value="High")
        odin_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        odin_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/58/Odin.png/revision/latest?cb=20200404172022")
        await ctx.send(
        embed=odin_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Odin")]
        )

    @weapon.command(aliases=['Ares'])
    async def ares(self, ctx):
        area_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Ares - Machine gun"
        )
        area_embed.add_field(name="Primary Fire",value="""
        :small_blue_diamond: Fully-automatic
        :small_blue_diamond: Fire Rate: 10 rounds/sec
        """)
        area_embed.add_field(name="Cost", value ="1,550")
        area_embed.add_field(name="Alt. Fire",value="""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 10 rounds/sec
        """,inline=False)
        area_embed.add_field(name="Damage",value="""
        Body 30 | Head 72  | Leg 25  - **0-30m**
        Body 28 | Head 67  | Leg 23  - **30-50m**
        """,inline=False)
        area_embed.add_field(name="Magazine Capacity", value="50")
        area_embed.add_field(name="Wall Penetration",value="High")
        area_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        area_embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/0/05/Ares.png/revision/latest?cb=20200404171957")
        await ctx.send(
        embed=area_embed,
        components=[Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Ares")]
        )

def setup(client):
    client.add_cog(weapon(client))
    print("Weapon       | Imported")