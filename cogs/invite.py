import discord
from discord.ext import commands
import json

with open ('config\config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']

class invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Invite','inv', 'inviteme'])
    async def invite(self, ctx):
        dm_embed = discord.Embed(
            color=0xA6FF0A
        )
        dm_embed.add_field(name ="THANK YOU FOR CHOOSING ME!",value="[click here](https://discord.com/oauth2/authorize?client_id=864451929346539530&permissions=2885938240&scope=bot) to invite me")

        ch_embed = discord.Embed(
            color=0xA6FF0A,
            description=f":white_check_mark: Check you dm {ctx.author.mention}"
        )
        await ctx.send(embed=ch_embed)
        await ctx.author.send(embed=dm_embed)

def setup(client):
    client.add_cog(invite(client))
    print("invite       | Imported")