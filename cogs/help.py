import discord
from discord.ext import commands
import json

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("<@!864451929346539530>"):
            embed = discord.Embed(
                color=0xC7FC02
            )
            embed.add_field(name=f'My prefix is `{prefix}`', value=f'type `{prefix}h` to learn more')
            await message.channel.send(embed=embed)

        

    @commands.group(aliases=['h'],invoke_without_command=True)
    async def help(self, ctx):
        help_embed = discord.Embed(
            color=0x0AFF4D,
            title="COMMAND LIST",
            description=f"""
            **GENERAL**
            :small_blue_diamond: `{prefix}status <region>` - shows server status of a region
            :small_blue_diamond: `{prefix}agent <name>` - shows info regarding agents
            :small_blue_diamond: `{prefix}map <name>` - shows info regarding valorant maps
            :small_blue_diamond: `{prefix}invite` - Get the bot invite link
            :small_blue_diamond: `{prefix}weapon <name>` - Get info of a weapon
            :small_blue_diamond: `{prefix}ace` - Get ace sounds of bundles
            :small_blue_diamond: `{prefix}skin` - shows info regarding skins
            :small_blue_diamond: `{prefix}spec` - shows PC requirements of Valorant
            :small_blue_diamond: `{prefix}leaderboard <region> <amount>` -  shows leaderboard 

            **PLAYER STAT**
            :small_blue_diamond: `{prefix}link <name>#<tagline>` - link to you valorant account
            :small_blue_diamond: `{prefix}unlink` - unlink to you valorant account
            :small_blue_diamond: `{prefix}rank` - show your rank and some other infos
            :small_blue_diamond: `{prefix}profile` - show your profile
            :small_blue_diamond: `{prefix}recent` - show your recent Competitive match

            **BUNDLE**
            :small_blue_diamond: `{prefix}bundle <name>` - show image of bundle with <name>
            :small_blue_diamond: `{prefix}bunl` - show list of bundles available in game
            """
        )
        help_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        help_embed.add_field(name = "MORE", value =f"For more details regarding a specific command use `{prefix}help <command>`")
        help_embed.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")
        await ctx.send(embed=help_embed)


    @help.command(aliases=["status"])
    async def vstat(self, ctx):
        vstat_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}vstat",
            description=f"full command = `{prefix}vstat <region>`"
        )
        vstat_help.add_field(name ="ALIASES", value=f"`{prefix}status <region>`", inline=False)
        vstat_help.add_field(name ="USAGE", value =f"""
        It will show conditions of valorant server of given <region>
        To get the region list use command `{prefix}reglist`
        """, inline=False)
        vstat_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        vstat_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=vstat_help)

    @help.command(aliases=['a', 'agents','ag'])
    async def agent(self, ctx):
        agent_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}agent",
            description=f"full command = `{prefix}agent <name>`"
        )
        agent_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}agents <name>`
        :white_small_square: `{prefix}a <name>`
        :white_small_square: `{prefix}ag <name>`
        """, inline=False)
        agent_help.add_field(name ="USAGE", value =f"""
        It will show details regarding a given Valorant Agent.
        To get the list of agent names use `{prefix}agent`
        """, inline=False)
        agent_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        agent_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=agent_help)


    @help.command(aliases=['Map','maps'])
    async def map(self, ctx):
        map_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}map",
            description=f"full command = `{prefix}map <name>`"
        )
        map_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}Map <name>`
        :white_small_square: `{prefix}maps <name>`
        """, inline=False)
        map_help.add_field(name ="USAGE", value =f"""
        It will show details regarding a given Valorant Map.
        To get the list of map names use `{prefix}map`
        """, inline=False)
        map_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        map_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=map_help)



    @help.command(aliases=['inv','Invite','inviteme'])
    async def invite(self, ctx):
        invite_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}map",
            description=f"full command = `{prefix}invite`"
        )
        invite_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}inv`
        :white_small_square: `{prefix}Invite`
        :white_small_square: `{prefix}inviteme`
        """, inline=False)
        invite_help.add_field(name ="USAGE", value =f"""
        It will send you the bot invite link
        """, inline=False)
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=invite_help)

    @help.command(aliases=['wp', 'wplist'])
    async def weapon(self, ctx):
        invite_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}Weapon",
            description=f"full command = `{prefix}weapon <name>`"
        )
        invite_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}wp`
        """, inline=False)
        invite_help.add_field(name ="USAGE", value =f"""
        It will show details regarding a weapon
        to get list of weapon use `{prefix}wplist`
        """, inline=False)
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=invite_help)

    @help.command(aliases=['as', 'ace'])
    async def acesound(self, ctx):
        invite_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}acesound",
            description=f"full command = `{prefix}acesound`"
        )
        invite_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}as`
        :white_small_square: `{prefix}ace`
        """, inline=False)
        invite_help.add_field(name ="USAGE", value =f"""
        It will send the ace sound of some popular collections
        """, inline=False)
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=invite_help)


    @help.command(aliases=['skins'])
    async def skin(self, ctx):
        invite_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}skin",
            description=f"full command = `{prefix}skin`"
        )
        invite_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}skins`
        """, inline=False)
        invite_help.add_field(name ="USAGE", value =f"""
        It will send the information related to any skin
        that you would like to see.
        To see list of guns use `{prefix}gunl`
        """, inline=False)
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=invite_help)
    
    @help.command(aliases=['specs','spec'])
    async def specification(self, ctx):
        invite_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}specification",
            description=f"full command = `{prefix}specification`"
        )
        invite_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}spec`
        :white_small_square: `{prefix}specs`
        """, inline=False)
        invite_help.add_field(name ="USAGE", value =f"""
        It will show PC requirements for Valorant
        """, inline=False)
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=invite_help)

    @help.command()
    async def link(self, ctx):
        invite_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}link",
            description=f"full command = `{prefix}link <name>#<tagline>`"
        )
        invite_help.add_field(name ="EXAMPLE", value =f"""
        so if your username is `TYshambo#0001` use command 
        `{prefix}link TYshambo#0001`
        make sure you do use `#` in the command
        """, inline=False)
        invite_help.add_field(name ="USAGE", value =f"""
        It will link the bot with your valorant account,
        so that you can access commands like 
        - `{prefix}recent`
        - `{prefix}rank`

        **NOTE**
        You need to link your profile with tracker.gg to use command  `{prefix}profile`
        [click here](https://cutt.ly/MQIpIBz) to link your profile with tracker.gg
        """, inline=False)
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=invite_help)


    @help.command()
    async def unlink(self, ctx):
        unlink_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}unlink",
            description=f"full command = `{prefix}unlink`"
        )

        unlink_help.add_field(name ="USAGE", value =f"""
        It will unlink your valorant account without your discord account
        

        **NOTE**
        You need to link your valorant account first
        before you can use this command.
        use `{prefix}h link` to know more
        """, inline=False)
        unlink_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        unlink_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=unlink_help)

    # @help.command()
    # async def shop(self, ctx):
    #     invite_help = discord.Embed(
    #         color=0x0AFF4D,
    #         title=f"{prefix}shop",
    #         description=f"full command = `{prefix}shop`"
    #     )

    #     invite_help.add_field(name ="USAGE", value =f"""
    #     It will show items available in your shop ingame

    #     **NOTE**
    #     Due to report, we may remove this command soon!",
    #     Join our support server to know more about it.
    #     """, inline=False)
    #     invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
    #     invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
    #     await ctx.send(embed=invite_help)

    @help.command(aliases=['bunl'])
    async def bundlelist(self, ctx):
        bundle_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}bundlelist",
            description=f"full command = `{prefix}bundlelist`"
        )
        bundle_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}bunl`
        """, inline=False)

        bundle_help.add_field(name ="USAGE", value =f"""
        It will show items list of available bundles in valorant 
        """, inline=False)
        bundle_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        bundle_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=bundle_help)
    
    @help.command()
    async def bundle(self, ctx):
        bundle_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}bundle",
            description=f"full command = `{prefix}bundle <name>`"
        )

        bundle_help.add_field(name ="USAGE", value =f"""
        It will show image of the bundle that has been given in place
        of <name>

        To get the list of bundles use `{prefix}bunl`
        """, inline=False)
        bundle_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        bundle_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=bundle_help)

    @help.command()
    async def rank(self, ctx):
        bundle_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}rank",
            description=f"full command = `{prefix}rank`"
        )

        bundle_help.add_field(name ="USAGE", value =f"""
        It will show your rank and some other stats

        **NOTE**
        You need to link your valorant account first
        before you can use this command.
        use `{prefix}h link` to know more
        """, inline=False)
        bundle_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        bundle_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=bundle_help)

    @help.command()
    async def profile(self, ctx):
        bundle_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}profile",
            description=f"full command = `{prefix}profile`"
        )

        bundle_help.add_field(name ="USAGE", value =f"""
        It will show some stats regarding your profile
        like - your K/D, Win Rate, Number of Hours you played etc.

        **NOTE**
        You need to connect your account with tracker.gg
        [click here](https://cutt.ly/MQIpIBz) to login!
        """, inline=False)
        bundle_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        bundle_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=bundle_help)

    @help.command()
    async def recent(self, ctx):
        recent_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}recent",
            description=f"full command = `{prefix}recent`"
        )

        recent_help.add_field(name ="USAGE", value =f"""
        It will show stats regarding your recent competitive match
        

        **NOTE**
        You need to link your valorant account first
        before you can use this command.
        use `{prefix}h link` to know more
        """, inline=False)
        recent_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        recent_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=recent_help)


    @help.command(aliases=['lb'])
    async def leaderboard(self, ctx):
        leaderboard_help = discord.Embed(
            color=0x0AFF4D,
            title=f"{prefix}leaderboard",
            description=f"full command = `{prefix}leaderboard <region> <amount>`"
        )
        leaderboard_help.add_field(name ="ALIASES", value=f"""
        :white_small_square: `{prefix}lb <region> <amount>`
        """, inline=False)
        leaderboard_help.add_field(name ="USAGE", value =f"""
        It will show leaderboard for a given region
        """, inline=False)
        leaderboard_help.add_field(name ="REGIONS AVAILABLE", value = """
        :white_small_square: `na` - North America
        :white_small_square: `eu` - Europe
        :white_small_square: `br` - Brazil
        :white_small_square: `ap` - Asia Pacific
        :white_small_square: `kr` - Korea
        :white_small_square: `latam` - Latin America
        """)
        leaderboard_help.add_field(name = "NOTE!",value="""
        Make sure that the region you provided is in lower case.
        It's not `AP` it's `ap`
        """)
        leaderboard_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/m5mSyTV7RR) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)", inline=False)  
        leaderboard_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=leaderboard_help)



def setup(client):
    client.add_cog(help(client))
    print("help         | Imported")