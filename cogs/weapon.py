import discord
from discord.ext import commands
from discord_components import Button
from .utils.weapon_api import get_uuid, get_data

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
        uuid , display_name = get_uuid()

        index = display_name.index('Classic')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)

        classic_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Classic - Sidearm"
        )
        classic_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        classic_embed.add_field(name="Cost", value =f"{data['cost']}")
        classic_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: 3-Round Burst, spread increase
        :small_blue_diamond: Fire Rate: 2.22 rounds/sec
        """,inline=False)
        classic_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        classic_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        classic_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        classic_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        classic_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=classic_embed,
        components=[
                [
                    Button(label="More", style=5, url="https://valorant.fandom.com/wiki/classic"),
                    Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                    Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
                ]
            ]

        )
        

    @weapon.command(aliases=['Shorty'])
    async def shorty(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Shorty')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)

        shorty_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Shorty - Sidearm"
        )
        shorty_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        shorty_embed.add_field(name="Cost", value =f"{data['cost']}")

        shorty_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        Head {data['damageRange2'][2]} | Body {data['damageRange2'][3]} | Leg {data['damageRange2'][4]} - **{data['damageRange2'][0]}m-{data['damageRange2'][1]}m**
        """,inline=False)
        shorty_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        shorty_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        shorty_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        shorty_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=shorty_embed,
        components=[
            [
                    Button(label="More", style=5, url="https://valorant.fandom.com/wiki/shorty"),
                    Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                    Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
        


    @weapon.command(aliases=['Frenzy'])
    async def frenzy(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Frenzy')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)

        frenzy_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Frenzy - Sidearm"
        )
        frenzy_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        frenzy_embed.add_field(name="Cost", value =f"{data['cost']}")

        frenzy_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        frenzy_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        frenzy_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        frenzy_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        frenzy_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=frenzy_embed,
        components=[
                [
                    Button(label="More", style=5, url="https://valorant.fandom.com/wiki/frenzy"),
                    Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                    Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
                ]
            ]

        )
        



    @weapon.command(aliases=['Ghost'])
    async def ghost(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Ghost')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)

        ghost_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Ghost - Sidearm"
        )
        ghost_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        ghost_embed.add_field(name="Cost", value =f"{data['cost']}")

        ghost_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        ghost_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        ghost_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        ghost_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        ghost_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=ghost_embed,
        components=[
                [
                    Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Ghost"),
                    Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                    Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
                ]
            ]

        )
        




    @weapon.command(aliases=['Sheriff'])
    async def sheriff(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Sheriff')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)

        sheriff_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Sheriff - Sidearm"
        )
        sheriff_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        sheriff_embed.add_field(name="Cost", value =f"{data['cost']}")

        sheriff_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        sheriff_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        sheriff_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        sheriff_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        sheriff_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=sheriff_embed,
        components=[
                [
                    Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Sheriff"),
                    Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                    Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
                ]

            ]

        )
        

    @weapon.command(aliases=['Stinger'])
    async def stinger(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Stinger')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        
        stinger_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Stinger - SMG"
        )
        stinger_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        stinger_embed.add_field(name="Cost", value =f"{data['cost']}")
        stinger_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: 4-Round Burst, Aim down sights
        :small_blue_diamond: Fire Rate: 8.471 rounds/sec
        """,inline=False)
        stinger_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        stinger_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        stinger_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        stinger_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        stinger_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=stinger_embed,
        components=[
                [
                    Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Stinger"),
                    Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                    Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
                ]
            ]

        )
   


    @weapon.command(aliases=['Spectre'])
    async def spectre(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Spectre')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        spectre_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Spectre - SMG"
        )
        spectre_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        spectre_embed.add_field(name="Cost", value =f"{data['cost']}")
        spectre_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Zoom Mode(1.15x), Aim down sights
        :small_blue_diamond: Fire Rate: 12 rounds/sec
        """,inline=False)
        spectre_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        spectre_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        spectre_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        spectre_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        spectre_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=spectre_embed,
        components=[
                [
                    Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Spectre"),
                    Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                    Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
                ]
            ]

        )
        

    @weapon.command(aliases=['Bucky'])
    async def bucky(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Bucky')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        bucky_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Bucky - Shotgun"
        )
        bucky_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        bucky_embed.add_field(name="Cost", value =f"{data['cost']}")
        bucky_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Fire a canister that detonates after a short distance, spraying pellets
        :small_blue_diamond: Fire Rate: 1.1 rounds/sec
        """,inline=False)
        bucky_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        Head {data['damageRange2'][2]} | Body {data['damageRange2'][3]} | Leg {data['damageRange2'][4]} - **{data['damageRange2'][0]}m-{data['damageRange2'][1]}m**
        """,inline=False)
        bucky_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        bucky_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        bucky_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        bucky_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=bucky_embed,
        components=[
            [
                Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Bucky"),
                Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])


    @weapon.command(aliases=['Judge'])
    async def judge(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Judge')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        judge_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Judge - Shotgun"
        )
        judge_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        judge_embed.add_field(name="Cost", value =f"{data['cost']}")

        judge_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        Head {data['damageRange2'][2]} | Body {data['damageRange2'][3]} | Leg {data['damageRange2'][4]} - **{data['damageRange2'][0]}m-{data['damageRange2'][1]}m**
        """,inline=False)
        judge_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        judge_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        judge_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        judge_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=judge_embed,
        components=[
            [
            Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Judge"),
            Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
            Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])

    @weapon.command(aliases=['Bulldog'])
    async def bulldog(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Bulldog')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        bulldog_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Bulldog - Rifle"
        )
        bulldog_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        bulldog_embed.add_field(name="Cost", value =f"{data['cost']}")
        bulldog_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: (6.555 rounds/sec)2.185 bursts/sec
        """,inline=False)
        bulldog_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        """,inline=False)
        bulldog_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        bulldog_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        bulldog_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        bulldog_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=bulldog_embed,
        components=[
            [
            Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Bulldog"),
            Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
            Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
        


    @weapon.command(aliases=['Guardian'])
    async def guardian(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Guardian')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        guardian_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Guardian - Rifle"
        )
        guardian_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        guardian_embed.add_field(name="Cost", value =f"{data['cost']}")
        guardian_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 4.275 rounds/sec
        """,inline=False)
        guardian_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        """,inline=False)
        guardian_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        guardian_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        guardian_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        guardian_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=guardian_embed,
        components=[
            [
            Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Guardian"),
            Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
            Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
       


    @weapon.command(aliases=['Vandal'])
    async def vandal(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Vandal')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        vandal_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Vandal - Rifle"
        )
        vandal_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        vandal_embed.add_field(name="Cost", value =f"{data['cost']}")
        vandal_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 8.775 rounds/sec
        """,inline=False)
        vandal_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        """,inline=False)
        vandal_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        vandal_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        vandal_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        vandal_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=vandal_embed,
        components=[
            [
            Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Vandal"),
            Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
            Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
        

    @weapon.command(aliases=['Phantom'])
    async def phantom(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Phantom')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        phantom_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Phantom - Rifle"
        )
        phantom_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        phantom_embed.add_field(name="Cost", value =f"{data['cost']}")
        phantom_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 9.9 rounds/sec
        """,inline=False)
        phantom_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        Head {data['damageRange2'][2]} | Body {data['damageRange2'][3]} | Leg {data['damageRange2'][4]} - **{data['damageRange2'][0]}m-{data['damageRange2'][1]}m**
        """,inline=False)
        phantom_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        phantom_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        phantom_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        phantom_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=phantom_embed,
        components=[
            [
            Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Phantom"),
            Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
            Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
    

    @weapon.command(aliases=['Marshal'])
    async def marshal(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Marshal')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        marshall_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Marshal - Sniper rifle"
        )
        marshall_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        marshall_embed.add_field(name="Cost", value =f"{data['cost']}")
        marshall_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 1.2 rounds/sec
        """,inline=False)
        marshall_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        """,inline=False)
        marshall_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        marshall_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        marshall_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        marshall_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=marshall_embed,
        components=[
            [
            Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Marshal"),
            Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
            Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
       



    @weapon.command(aliases=['Operator'])
    async def operator(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Operator')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        operator_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Operator - Sniper rifle"
        )
        operator_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        operator_embed.add_field(name="Cost", value =f"{data['cost']}")
        operator_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 0.75 rounds/sec
        """,inline=False)
        operator_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        """,inline=False)
        operator_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        operator_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        operator_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        operator_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=operator_embed,
        components=[
            [
                Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Operator"),
                Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
        
    


    @weapon.command(aliases=['Odin'])
    async def odin(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Odin')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        odin_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Odin - Machine gun"
        )
        odin_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        odin_embed.add_field(name="Cost", value =f"{data['cost']}")
        odin_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 15.6 rounds/sec
        """,inline=False)
        odin_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        odin_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        odin_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        odin_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        odin_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=odin_embed,
        components=[
            [
                Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Odin"),
                Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
                Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])
    

    @weapon.command(aliases=['Ares'])
    async def ares(self, ctx):
        uuid , display_name = get_uuid()

        index = display_name.index('Ares')
        weapon_uuid = uuid[index]

        data = get_data(weapon_uuid)
        area_embed = discord.Embed(
            color = 0x0AFFB5,
            title = "Ares - Machine gun"
        )
        area_embed.add_field(name="Primary Fire",value=f"""
        :small_blue_diamond: Fire Rate: {data['fireRate']}
        :small_blue_diamond: Reload time: {data['reloadTimeSeconds']} sec
        """)
        area_embed.add_field(name="Cost", value =f"{data['cost']}")
        area_embed.add_field(name="Alt. Fire",value=f"""
        :small_blue_diamond: Aim Down Sights
        :small_blue_diamond: Fire Rate: 10 rounds/sec
        """,inline=False)
        area_embed.add_field(name="Damage",value=f"""
        Head {data['damageRange0'][2]} | Body {data['damageRange0'][3]} | Leg {data['damageRange0'][4]} - **{data['damageRange0'][0]}m-{data['damageRange0'][1]}m**
        Head {data['damageRange1'][2]} | Body {data['damageRange1'][3]} | Leg {data['damageRange1'][4]} - **{data['damageRange1'][0]}m-{data['damageRange1'][1]}m**
        """,inline=False)
        area_embed.add_field(name="Magazine Capacity", value=f"{data['magazineSize']}")
        area_embed.add_field(name="Wall Penetration",value=f"{data['wallPenetration']}")
        area_embed.set_thumbnail(url=f"{data['killStreamIcon']}")
        area_embed.set_image(url=f"{data['displayIcon']}")
        await ctx.send(
        embed=area_embed,
        components=[
            [
            Button(label="More", style=5, url="https://valorant.fandom.com/wiki/Ares"),
            Button(label="Vote", style=5, url="https://top.gg/bot/864451929346539530/vote"),
            Button(label="Support", style=5, url="https://discord.gg/m5mSyTV7RR")
            ]

        ])

def setup(client):
    client.add_cog(weapon(client))
    print("Weapon       | Imported")