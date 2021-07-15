import discord
from discord.ext import commands
import DiscordUtils 
from valoStatus import Region
from discord.ext.commands import MissingRequiredArgument


class Valostatus(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(aliases=['vstat'])
    async def status(self, ctx, region):
        
        region = Region(region)
        if region.get_status_issue() == False:
            await ctx.send("no errors")

        else:
            
            if region.incident_check() == True:
                embed1 = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.incident_title()
                )
                embed1.add_field(name=region.incident_date(), value=region.incident_reason())

            if region.maintenence_check() == True:
                embed2 = discord.Embed(
                    colour = discord.Colour.orange(),
                    title = region.maintenance_title()
                )
                embed2.add_field(name=region.incident_reason(), value=region.maintenance_reason())

                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, auto_footer = True)
                paginator.add_reaction('⬅️', "back")
                paginator.add_reaction('➡️', "next")
                embeds = [embed1, embed2]
                await paginator.run(embeds)


    @status.error
    async def status_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            embed = discord.Embed(
                description='',
                color=discord.Color.red()
            )
            embed.add_field(name ="❌You need to give REGION",value="`$status <region>`",inline=False)
            embed.add_field(name ="REGION LIST",value="""
            NA - North America
            EU - Europe
            BR - Brazil
            AP - Asia Pacific
            KR - Korea
            LATAM - Latin America
            """,inline=False)
            embed.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")

            embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
            
            
            await ctx.send(embed=embed)

    @commands.command(aliases =['reglist'])
    async def regionlist(self, ctx):
        embed = discord.Embed(
            color = discord.Color.red()
        )
        embed.add_field(name ="REGION LIST",value="""
        NA - North America
        EU - Europe
        BR - Brazil
        AP - Asia Pacific
        KR - Korea
        LATAM - Latin America
        """,inline=False)
        embed.add_field(name = "Join support server!", value="[support server](https://discord.com/invite/tygamers) | [github](https://github.com/typhonshambo/Valorant-server-stat-bot)")

        embed.set_thumbnail(url="https://toppng.com/public/uploads/thumbnail/valorant-logo-icon-11608279985fgrckoiiql.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Valostatus(client))
    print("Valostatus   | Imported")