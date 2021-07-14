import discord
from discord.ext import commands

class skin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.group(name="Agents", aliases=['agent', 'ag', 'a'], invoke_without_command=True)
    async def agents(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )
        embed.add_field(name="AGENTS",
        value="""
        [1] BRIMSTONE
        [2] PHOENIX
        [3] SAGE
        [4] SOVA
        [5] VIPER
        [6] CYPHER
        [7] REYNA
        [8] KILLJOY
        [9] BREACH
        [10] OMEN
        [11] JETT
        [12] RAGE
        [13] SKYE
        [14] YORU
        [15] ASTRA
        [16] KAY/O
        """)
        await ctx.send(embed=embed)
    
    @agents.command()
    async def reyna(self, ctx):
        embed = discord.Embed(
            title='Reyna - Duelist',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=" :flag_mx: Mexico",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Leer
        **Q** - Devour
        **E** - Dismiss - **Signature**
        **X** - Empress - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Forged in the heart of Mexico, Reyna dominates single combat, popping off with each kill she scores. Her capability is only limited by her raw skill, making her highly dependent on performance.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://imgur.com/u82EvYB.png")
        await ctx.send(embed=embed)

    @agents.command(aliases=['bs','Brimstone'])
    async def brimstone(self, ctx):
        embed = discord.Embed(
            title="Brimstone - Controller",
            colour = discord.Colour.orange()
        )
        embed.add_field(name ="Country", value = ":flag_us: USA",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        C - Stim Beacon
        Q - Incendiary
        E - Sky Smoke - Signature
        X - Orbital Strike - Ultimate
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Brimstone's orbital arsenal ensures his squad always has advantage. His ability to deliver utility precisely and safely make him the unmatched boots-on-the-ground commander.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://imgur.com/kttAyZq.png")
        await ctx.send(embed=embed)


    @agents.command()
    async def jett(self, ctx):
        embed = discord.Embed(
            title='Jett - Duelist',
            color=0x00FFFF
        )
        embed.add_field(name ="Country",value=" 🇰🇷 South Korea",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Cloudburst
        **Q** - Updraft
        **E** - Tailwind - **Signature**
        **X** - Blade Storm - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Jett's agile and evasive fighting style lets her take risks no one else can. She runs circles around every skirmish, cutting enemies up before they even know what hit them.

        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864946744118345738/V_AGENTS_587x900_Jett.png")
        await ctx.send(embed=embed)


    @agents.command()
    async def phoenix(self, ctx):
        embed = discord.Embed(
            title='Phoenix - Duelist',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=":flag_gb: United Kingdom",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Blaze
        **Q** - Curveball
        **E** - Hot Hands - **Signature**
        **X** - Run it Back - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Phoenix's star power shines through in his fighting style, igniting the battlefield with flash and flare. Whether he's got backup or not, he's rushing in to fight on his own terms.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://images-ext-1.discordapp.net/external/lY1T7tKRPxFJGdoLMDI2BbI_x4TAeJSpdl0E7sMq0A8/https/imgur.com/RLLfAKs.png?width=480&height=480")
        await ctx.send(embed=embed)

    @agents.command()
    async def sage(self, ctx):
        embed = discord.Embed(
            title='Sage - Sentinel',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=" :flag_cn: China",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Barrier Orb
        **Q** - Slow Orb
        **E** - Healing Orb - **Signature**
        **X** - Ressurection - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Sage creates safety for herself and her team wherever she goes. Able to revive fallen friends and stave off forceful assaults, she provides a calm center to a hellish battlefield.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url=" https://static.wikia.nocookie.net/valorant-lore/images/3/37/Sage_-_Full_body.png/revision/latest?cb=20210123180615")
        await ctx.send(embed=embed)


    @agents.command()
    async def cypher(self, ctx):
        embed = discord.Embed(
            title='Cypher - Sentinel',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=":flag_ma: Morocco",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Trapwire
        **Q** - Cyber Cage
        **E** - Spycam - **Signature**
        **X** - Neural Theft - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Cypher is a one-man surveillance network who keeps tab on the enemy's every move. No secret is safe. No manuever goes unseen. Cypher is always watching.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://i.imgur.com/mmEC6WB.png")
        await ctx.send(embed=embed)


    @agents.command(aliases=['kj'])
    async def killjoy(self, ctx):
        embed = discord.Embed(
            title='Killjoy - Sentinel',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=" :flag_de: Germany",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Nanoswarm
        **Q** - Alarmbot
        **E** - Turret - **Signature**
        **X** - Lockdown - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        The genius of Germany. Killjoy secures the battlefield with ease using her arsenal of inventions. If the damage from her gear doesn't stop her enemies, her robots' debuff will help make short work of them.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://imgur.com/pJSKqkC.png")
        await ctx.send(embed=embed)



    @agents.command(aliases=['Viper','vipr'])
    async def viper(self, ctx):
        embed = discord.Embed(
            title='Viper - Controller',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=":flag_us: USA",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Snake Bite
        **Q** - Poison Cloud
        **E** - Toxic Screen - **Signature**
        **X** - Viper's Pit - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Sova tracks, finds and eliminates enemies with ruthless efficiency and precision. His custom bow and incredible scouting abilities ensure that even if you run, you cannot hide.
        """)
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864936191311740959/latest.png")
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        await ctx.send(embed=embed)



    @agents.command()
    async def sova(self, ctx):
        embed = discord.Embed(
            title='Sova - Initiator',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=" :flag_ru: Russia",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Owl Drone
        **Q** - Shock Bolt
        **E** - Recon Bolt - **Signature**
        **X** - Hunter's Fury - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Sova tracks, finds and eliminates enemies with ruthless efficiency and precision. His custom bow and incredible scouting abilities ensure that even if you run, you cannot hide.   
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864936191311740959/latest.png")
        await ctx.send(embed=embed)


    @agents.command()
    async def breach(self, ctx):
        embed = discord.Embed(
            title='Breach - Initiator',
            color=0x58472C
        )
        embed.add_field(name ="Country",value=":flag_se: Sweden",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Aftershock
        **Q** - Flashpoint
        **E** - Fault Line - **Signature**
        **X** - Rolling Thunder - **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Breach fires powerful, targeted kinetic blasts to aggressively clear a path through enemy ground. The damage and disruption he inflicts ensures no fight is ever fair.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864938040572510228/V_AGENTS_587x900_Breach.png")
        await ctx.send(embed=embed)

    @agents.command()
    async def raze(self, ctx):
        embed = discord.Embed(
            title='Raze - Duelist',
            color=0xFC5400
        )
        embed.add_field(name ="Country",value=" :flag_br: Brazil",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Boom Bot
        **Q** - Blast Pack
        **E** - Paint Shells - **Signature**
       ** X** - Showstopper- **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""Raze loves explosives. With her blunt-force-trauma playstyle, she excels at flushing entrenched enemies and clearing tight spaces with a generous dose of "boom".
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864938093404618792/V_AGENTS_587x900_ALL_Raze_2.png")
        await ctx.send(embed=embed)


    @agents.command()
    async def skye(self, ctx):
        embed = discord.Embed(
            title='Skye - Initiator',
            color=discord.Color.green()
        )
        embed.add_field(name ="Country",value=" 🇦🇺 Australia",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Regrowth
        **Q** - Trailblazer
        **E** - Guiding Light - **Signature**
       ** X** - Seekers- **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Hailing from Australia, Skye and her band of beasts trail-blaze the way through hostile territory. With her creations hampering the enemy, and her power to heal others, the team is strongest and safest by Skye’s side.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/d/d6/Skye_artwork.png/revision/latest?cb=20201013182515")
        await ctx.send(embed=embed)

    @agents.command()
    async def omen(self, ctx):
        embed = discord.Embed(
            title='Omen - Controller',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=" Unknown",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Shrouded Step
        **Q** - Paranoia
        **E** - Dark Cover - **Signature**
       ** X** - From The Shadows- **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""Omen hunts in the shadows. He renders enemies blind, teleports across the field, then lets paranoia take hold as foes scramble to uncover where it might strike next..
        
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864940971375460422/V_AGENTS_587x900_Omen.png")
        await ctx.send(embed=embed)


    @agents.command()
    async def yoru(self, ctx):
        embed = discord.Embed(
            title='Yoru - Duelists',
            color=0x0076F4
        )
        embed.add_field(name ="Country",value=" 🇯🇵 Japan",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Fakeout
        **Q** - Blindside
        **E** - Gatecrash - **Signature**
       ** X** - Dimensional Drift- **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""
        Japanese native Yoru rips holes straight through reality to infiltrate enemy lines unseen. Using deception and aggression in equal measure, he gets the drop on each target before they know where to look.
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/1/1a/Yoru_artwork.png/revision/latest?cb=20210112180407")
        await ctx.send(embed=embed)

    @agents.command()
    async def astra(self, ctx):
        embed = discord.Embed(
            title='Astra - Controller',
            color=0xB10AFF
        )
        embed.add_field(name ="Country",value=" GH.png Ghana",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - Gravity Well
        **Q** - Nova Pulse
        **E** - Nebula - **Signature**
       ** X** - Cosmic Divide- **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""Ghanaian Agent Astra harnesses the energies of the cosmos to reshape battlefields to her whim. With full command of her astral form and a talent for deep strategic foresight, she’s always eons ahead of her enemy’s next move.
        
        """)
        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864943485592928286/Astra_Artwork.png")
        await ctx.send(embed=embed)


    @agents.command(aliases=["Kay/O","kay/o"])
    async def kayo(self, ctx):
        embed = discord.Embed(
            title='Kayo - Initiator',
            color=0xA902FC
        )
        embed.add_field(name ="Country",value=" Unknown",inline=False)
        embed.add_field(name = "Abilities",
        value="""
        **C** - FRAG/ment
        **Q** - FLASH/drive
        **E** -  ZERO/point - **Signature**
       ** X** -  NULL/cmd- **Ultimate**
        """,inline=False)
        embed.add_field(name = "Description",
        value="""KAY/O is a machine of war built for a single purpose: neutralizing radiants. His power to suppress enemy abilities cripples his opponents' capacity to fight back, securing him and his allies the ultimate edge.
        """)
        embed.set_image(url="https://cdn.discordapp.com/attachments/864780326357827585/864944008198750239/latest.png")
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(skin(client))
    print("agents      | Imported")   