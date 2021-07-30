import discord
from discord.ext import commands
import json

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['h'],invoke_without_command=True)
    async def help(self, ctx):
        help_embed = discord.Embed(
            color=0x0AFF4D,
            title="COMMAND LIST",
            description=f"""
            :small_blue_diamond: `{prefix}vstat <region>` - shows server status of a region
            :small_blue_diamond: `{prefix}agent <name>` - shows info regarding agents
            :small_blue_diamond: `{prefix}map <name>` - shows info regarding valorant maps
            :small_blue_diamond: `{prefix}invite` - Get the bot invite link
            :small_blue_diamond: `{prefix}weapon <name>` - Get info of a weapon
            :small_blue_diamond: `{prefix}ace` - Get ace sounds of bundles
            :small_blue_diamond: `{prefix}skin` - shows info regarding skins
            :small_blue_diamond: `{prefix}spec` - shows PC requirements of Valorant
            """
        )
        help_embed.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")
        help_embed.add_field(name = "MORE", value =f"For more details regarding a specific command use `{prefix}help <command>`")
        help_embed.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")
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
        vstat_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
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
        agent_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
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
        map_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
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
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
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
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
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
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
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
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
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
        invite_help.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")  
        invite_help.set_thumbnail(url="https://i.imgur.com/A45DVhf.gif")   
        await ctx.send(embed=invite_help)


def setup(client):
    client.add_cog(help(client))
    print("help         | Imported")