import discord
from discord.ext import commands
from .valinfo import getValorantInfo
from discord.ext.commands import MissingRequiredArgument
import json
from discord_components import *

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']




class skin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def patch(self, message):
        await message.channel.send("Find the patch notes for the recent patch here: https://playvalorant.com/en-us/news/game-updates/valorant-patch-notes-1-03/")



    @commands.command(aliases=['gunl'])
    async def gunlist(self, ctx):

        embed = discord.Embed(
            color = discord.Color.green()
        )
        embed.add_field(name ="GUN LIST", value = """
        classic 
        shorty
        frenzy
        ghost
        sheriff 
        stinger
        spectre 
        bucky 
        judge
        bulldog
        guardian
        vandal 
        phantom
        marshall 
        operator 
        odin
        ares
        """)
        await ctx.send(embed=embed)


    @commands.group(aliases = ['skins'])
    async def skin(self, ctx):
        await ctx.send("Select a gun",
            components=[
                Select(placeholder='Selection',
                options=[
                    SelectOption(label="Classic",value="classic"),
                    SelectOption(label="Shorty",value="shorty"),
                    SelectOption(label="Frenzy",value="frenzy"),
                    SelectOption(label="Ghost",value="ghost"),
                    SelectOption(label="Sheriff",value="sheriff"),
                    SelectOption(label="Stinger",value="stinger"),
                    SelectOption(label="Spectre",value="spectre"),
                    SelectOption(label="Bucky",value="bucky"),
                    SelectOption(label="Judge",value="judge"),
                    SelectOption(label="Bulldog",value="bulldog"),
                    SelectOption(label="Guardian",value="guardian"),
                    SelectOption(label="Vandal",value="vandal"),
                    SelectOption(label="Phantom",value="phantom"),
                    SelectOption(label="Marshal",value="marshal"),
                    SelectOption(label="Operator",value="operator"),
                    SelectOption(label="Odin",value="odin"),
                    SelectOption(label="Ares",value="ares")
                    ])
            ]
        )
        _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

        
        if _res.user == ctx.author:
            if _res.component[0].value=="classic":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Pistolinha Classic",value="Pistolinha Classic"),
                        SelectOption(label="Red Alert Classic",value="Red Alert Classic"),
                        SelectOption(label="Glitchpop Classic",value="Glitchpop Classic"),
                        SelectOption(label="Surge Classic",value="Surge Classic"),
                        SelectOption(label="Forsaken Classic",value="Forsaken Classic"),
                        SelectOption(label="Prime Classic",value="Prime Classic"),
                        SelectOption(label="Avalanche  Classic",value="Avalanche  Classic"),
                        SelectOption(label="Prism III  Classic",value="Prism III  Classic"),
                        SelectOption(label="Kingdom Classic",value="Kingdom Classic"),
                        SelectOption(label="Spline Classic",value="Spline Classic"),
                        SelectOption(label="Galleria Classic",value="Galleria Classic"),
                        SelectOption(label="Neuroblaster Classic",value="Neuroblaster Classic"),
                        SelectOption(label="Sakura Classic",value="Sakura Classic"),
                        SelectOption(label="Infinity Classic",value="Infinity Classic"),
                        SelectOption(label="Final Chamber Classic",value="SFinal Chamber Classic")
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])
                if _res.component[0].value=="Pistolinha Classic":
                    embed = discord.Embed(
                        title="Pistolinha Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Raze Level 10")
                    embed.set_image(url="https://vgraphs.com/images/weapons/skins/full-details/valorant-pistolinha-classic-weapon-skin.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])
                if _res.component[0].value=="Red Alert Classic":
                    embed = discord.Embed(
                        title="Red Alert Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 40")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/12/Classic_red_alert_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])

                if _res.component[0].value=="Glitchpop Classic":
                    embed = discord.Embed(
                        title="Glitchpop Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/6b/Classic_glitchpop_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])
        

                if _res.component[0].value=="Surge Classic":
                    embed = discord.Embed(
                        title="Surge Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 16")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/6d/Classic_surge_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])
        
                if _res.component[0].value=="Forsaken Classic":
                    embed = discord.Embed(
                        title="Forsaken Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/81/Classic_forsaken_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])

                
                if _res.component[0].value=="Prime Classic":
                    embed = discord.Embed(
                        title="Prime Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/5a/Classic_prime_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])  

                if _res.component[0].value=="Avalanche  Classic":
                    embed = discord.Embed(
                        title="Avalanche  Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/26/Classic_avalanche_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])                    
                

                if _res.component[0].value=="Prism III  Classic":
                    embed = discord.Embed(
                        title="Prism III  Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/21/Classic_prism_iii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])    

                if _res.component[0].value=="Kingdom Classic":
                    embed = discord.Embed(
                        title="Kingdom Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/64/Classic_kingdom_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])   

                if _res.component[0].value=="Spline Classic":
                    embed = discord.Embed(
                        title="Spline Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c6/Classic_spline_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])   

                if _res.component[0].value=="Galleria Classic":
                    embed = discord.Embed(
                        title="Galleria Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/60/Classic_galleria_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])   

                if _res.component[0].value=="Neuroblaster Classic":
                    embed = discord.Embed(
                        title="ravitational Uranium Neuroblaster Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/ad/Classic_g.u.n_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])   

                if _res.component[0].value=="rSakura Classic":
                    embed = discord.Embed(
                        title="Sakura Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:  1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f7/Classic_sakura_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])   


                if _res.component[0].value=="Infinity Classic":
                    embed = discord.Embed(
                        title="Infinity Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f2/Classic_infinity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])   


                if _res.component[0].value=="Final Chamber Classic":
                    embed = discord.Embed(
                        title="Final Chamber Classic",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Sage Level 10")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/7d/Classic_sage%27s_classic_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Classic/Skins")])   

        
        if _res.user == ctx.author:
            if _res.component[0].value=="shorty":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Viper's Shorty",value="Viper's Shorty"),
                        SelectOption(label="Killjoy's Shorty",value="Killjoy's Shorty"),
                        SelectOption(label="Hivemind Shorty",value="Hivemind Shorty"),
                        SelectOption(label="Ruin Shorty",value="Ruin Shorty"),
                        SelectOption(label="Wasteland Shorty",value="Wasteland Shorty"),
                        SelectOption(label="Aerosol Shorty",value="Aerosol Shorty"),
                        SelectOption(label="Prism II Shorty",value="Prism II Shorty"),
                        SelectOption(label="Oni Shorty",value="Oni Shorty"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])
                if _res.component[0].value=="Viper's Shorty":
                    embed = discord.Embed(
                        title="Viper's Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Viper Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/56/Shorty_viper%27s_shorty_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")])   

                if _res.component[0].value=="Killjoy's Shorty":
                    embed = discord.Embed(
                        title="Killjoy's Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Killjoy Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/75/Shorty_killjoy%27s_shorty_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")])  

                if _res.component[0].value=="Hivemind Shorty":
                    embed = discord.Embed(
                        title="Hivemind Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/ba/Shorty_hivemind_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")]) 

                if _res.component[0].value=="Ruin Shorty":
                    embed = discord.Embed(
                        title="Ruin Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 20")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a9/Shorty_ruin_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")])       
        

                if _res.component[0].value=="Wasteland Shorty":
                    embed = discord.Embed(
                        title="Wasteland Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/cf/Shorty_wasteland_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")])        
                
                if _res.component[0].value=="Aerosol Shorty":
                    embed = discord.Embed(
                        title="Aerosol Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 15")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/48/Shorty_aerosol_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")])        
                
                
                if _res.component[0].value=="Prism II Shorty":
                    embed = discord.Embed(
                        title="Prism II Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/1e/Shorty_prism_ii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")])    
        
                if _res.component[0].value=="Oni Shorty":
                    embed = discord.Embed(
                        title="Oni Shorty",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/1b/Shorty_oni_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Shorty/Skins")])        
        






        if _res.user == ctx.author:
            if _res.component[0].value=="frenzy":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="RagnaRocker Frenzy",value="RagnaRocker Frenzy"),
                        SelectOption(label="Origin Frenzy",value="Origin Frenzy"),
                        SelectOption(label="Glitchpop Frenzy",value="Glitchpop Frenzy"),
                        SelectOption(label="Elderflame Frenzy",value="Elderflame Frenzy"),
                        SelectOption(label="Swooping Frenzy",value="Swooping Frenzy"),
                        SelectOption(label="Horizon Frenzy",value="Horizon Frenzy"),
                        SelectOption(label="Prime//2.0 Frenzy",value="Prime//2.0 Frenzy"),
                        SelectOption(label="Couture Frenzy",value="Couture Frenzy"),
                        SelectOption(label="Celestial Frenzy",value="Celestial Frenzy"),
                        SelectOption(label="Spitfire Frenzy",value="Spitfire Frenzy"),
                        SelectOption(label="Sensation Frenzy",value="Sensation Frenzy"),
                        SelectOption(label="Lightwave Frenzy",value="Lightwave Frenzy"),
                        SelectOption(label="Standard Frenzy",value="Standard Frenzy"),
                        SelectOption(label="BlastX Frenzy",value="BlastX Frenzy"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])
                
                if _res.component[0].value=="RagnaRocker Frenzy":
                    embed = discord.Embed(
                        title="RagnaRocker Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Breach Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/75/Frenzy_breach%27s_frenzy_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])   

                if _res.component[0].value=="Origin Frenzy":
                    embed = discord.Embed(
                        title="Origin Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/af/Frenzy_origin_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])   
        
                if _res.component[0].value=="Glitchpop Frenzy":
                    embed = discord.Embed(
                        title="Glitchpop Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:  2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c4/Frenzy_glitchpop_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")]) 

                if _res.component[0].value=="Elderflame Frenzy":
                    embed = discord.Embed(
                        title="Elderflame Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:  2,475 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b0/Frenzy_elderflame_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")]) 

                if _res.component[0].value=="Swooping Frenzy":
                    embed = discord.Embed(
                        title="Swooping Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Skye Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/d/d3/Frenzy_skye%27s_frenzy_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")]) 

                if _res.component[0].value=="Horizon Frenzy":
                    embed = discord.Embed(
                        title="Horizon Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:  1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/35/Frenzy_horizon_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")]) 


                if _res.component[0].value=="Prime//2.0 Frenzy":
                    embed = discord.Embed(
                        title="Prime//2.0 Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:  1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/71/Frenzy_prime_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")]) 
        
                if _res.component[0].value=="Couture Frenzy":
                    embed = discord.Embed(
                        title="Couture Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 16   ")
                    embed.set_image(url="https://cdn.discordapp.com/attachments/855461233866965023/867668779961417738/241px-Frenzy_couture_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])
                
                if _res.component[0].value=="Celestial Frenzy":
                    embed = discord.Embed(
                        title="Celestial Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/1/17/Frenzy_celestial_VALORANT.png/362px-Frenzy_celestial_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])

                if _res.component[0].value=="Spitfire Frenzy":
                    embed = discord.Embed(
                        title="Spitfire Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Phoenix Level 9 ")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/5/56/Frenzy_phoenix%27s_frenzy_VALORANT.png/362px-Frenzy_phoenix%27s_frenzy_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])

                if _res.component[0].value=="Sensation Frenzy":
                    embed = discord.Embed(
                        title="Sensation Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/5/54/Frenzy_sensation_VALORANT.png/362px-Frenzy_sensation_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])

                if _res.component[0].value=="Lightwave Frenzy":
                    embed = discord.Embed(
                        title="Lightwave Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 50 ")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/7/7e/Frenzy_lightwave_VALORANT.png/362px-Frenzy_lightwave_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])

                if _res.component[0].value=="Standard Frenzy":
                    embed = discord.Embed(
                        title="Standard Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Default Skin ")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/8/85/Frenzy_amp-11_VALORANT.png/362px-Frenzy_amp-11_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])

                if _res.component[0].value=="BlastX Frenzy":
                    embed = discord.Embed(
                        title="BlastX Frenzy",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/5/5f/Frenzy_blastx_VALORANT.png/362px-Frenzy_blastx_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Frenzy/Skins")])        

        

        if _res.user == ctx.author:
            if _res.component[0].value=="ghost":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="VALORANT GO! Vol. 1 Ghost",value="VALORANT GO! Vol. 1 Ghost"),
                        SelectOption(label="dot EXE Ghost",value="dot EXE Ghost"),
                        SelectOption(label="Hush Ghost",value="Hush Ghost"),
                        SelectOption(label="Infantry Ghost",value="Infantry Ghost"),
                        SelectOption(label="Outpost Ghost",value="Outpost Ghost"),
                        SelectOption(label="Prism Ghost",value="Prism Ghost"),
                        SelectOption(label="Serenity Ghost",value="Serenity Ghost"),
                        SelectOption(label="Ruination Ghost",value="Ruination Ghost"),
                        SelectOption(label="Luxe Ghost",value="Luxe Ghost"),
                        SelectOption(label="Magepunk Ghost",value="Magepunk Ghost"),
                        SelectOption(label="Jigsaw Ghost",value="Jigsaw Ghost"),
                        SelectOption(label="Eclipse Ghost",value="Eclipse Ghost"),
                        SelectOption(label="Sovereign Ghost",value="Sovereign Ghost"),
                        SelectOption(label="Tethered Realms Ghost",value="Tethered Realms Ghost"),
                        SelectOption(label="Depths Ghost",value="Depths Ghost"),
                        SelectOption(label="Ego Ghost",value="Ego Ghost"),
                        SelectOption(label="Vendetta Ghost",value="Vendetta Ghost"),
                        SelectOption(label="Winterwunderland Ghost",value="Winterwunderland Ghost"),
                        SelectOption(label="Soul Silencer Ghost",value="Soul Silencer Ghost")
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="VALORANT GO! Vol. 1 Ghost":
                    embed = discord.Embed(
                        title="VALORANT GO! Vol. 1 Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/89/Ghost_valorant_go%21_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")]) 
                
                
                if _res.component[0].value=="dot EXE Ghost":
                    embed = discord.Embed(
                        title="dot EXE Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 35")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/43/Ghost_dot_exe_ghost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])   

                if _res.component[0].value=="Hush Ghost":
                    embed = discord.Embed(
                        title="Hush Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Cypher Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/34/Ghost_cypher%27s_ghost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])   
 
                if _res.component[0].value=="Infantry Ghost":
                    embed = discord.Embed(
                        title="Infantry Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/60/Ghost_infantry_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])   

                if _res.component[0].value=="Outpost Ghost":
                    embed = discord.Embed(
                        title="Outpost Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 10")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/4f/Ghost_outpost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])   

                if _res.component[0].value=="Prism Ghost":
                    embed = discord.Embed(
                        title="Prism Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/57/Ghost_prism_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])   

                if _res.component[0].value=="Serenity Ghost":
                    embed = discord.Embed(
                        title="Serenity Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 5")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/73/Ghost_serenity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")]) 

                if _res.component[0].value=="Ruination Ghost":
                    embed = discord.Embed(
                        title="Ruination Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/ruination_ghost.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])   


                if _res.component[0].value=="Luxe Ghost":
                    embed = discord.Embed(
                        title="Luxe Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/49/Ghost_luxe_blue_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")]) 


                if _res.component[0].value=="Magepunk Ghost":
                    embed = discord.Embed(
                        title="Magepunk Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b7/Ghost_magepunk_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")]) 


                if _res.component[0].value=="Jigsaw Ghost":
                    embed = discord.Embed(
                        title="Jigsaw Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Reflexion: Act 1 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/25/Ghost_jigsaw_yoru_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])
        
                if _res.component[0].value=="Eclipse Ghost":
                    embed = discord.Embed(
                        title="Eclipse Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Astra Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f9/Ghost_astra%27s_ghost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])

                 
                if _res.component[0].value=="Sovereign Ghost":
                    embed = discord.Embed(
                        title="Sovereign Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a0/Ghost_sovereign_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])
      
        
        
                if _res.component[0].value=="Tethered Realms Ghost":
                    embed = discord.Embed(
                        title="Tethered Realms Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/fb/Ghost_tethered_realms_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])
        
                if _res.component[0].value=="Depths Ghost":
                    embed = discord.Embed(
                        title="Depths Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 30")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f6/Ghost_depths_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])
        
                if _res.component[0].value=="Ego Ghost":
                    embed = discord.Embed(
                        title="Ego Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/ff/Ghost_ego_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])

                if _res.component[0].value=="Vendetta Ghost":
                    embed = discord.Embed(
                        title="Vendetta Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Reyna Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/85/Ghost_reyna%27s_ghost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")]) 


                if _res.component[0].value=="Winterwunderland Ghost":
                    embed = discord.Embed(
                        title="Winterwunderland Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a1/Ghost_winter_wunderland_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])     

                if _res.component[0].value=="Soul Silencer Ghost":
                    embed = discord.Embed(
                        title="Soul Silencer Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Omen Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/bc/Ghost_omen%27s_ghost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ghost/Skins")])    
        
        
        
        
        
        if _res.user == ctx.author:
            if _res.component[0].value=="spectre":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="VALORANT GO! Vol. 1",value="VALORANT GO! Vol. 1"),
                        SelectOption(label="Singularity Spectre",value="Singularity Spectre"),
                        SelectOption(label="Hivemind Spectre",value="Hivemind Spectre"),
                        SelectOption(label="Forsaken Spectre",value="Forsaken Spectre"),
                        SelectOption(label="Infantry Spectre",value="Infantry Spectre"),
                        SelectOption(label="Horizon Spectre",value="Horizon Spectre"),
                        SelectOption(label="Prime Spectre",value="Prime Spectre"),
                        SelectOption(label="Avalanche Spectre",value="Avalanche Spectre"),
                        SelectOption(label="Prism Spectre",value="Prism Spectre"),
                        SelectOption(label="Serenity Spectre",value="Serenity Spectre"),
                        SelectOption(label="Ruination Spectre",value="Ruination Spectre"),
                        SelectOption(label="Kingdom Spectre",value="Kingdom Spectre"),
                        SelectOption(label="Luxe Spectre",value="Luxe Spectre"),
                        SelectOption(label="Magepunk Spectre",value="Magepunk Spectre"),
                        SelectOption(label="Spline Spectre",value="Spline Spectre"),
                        SelectOption(label="Minima Spectre",value="Minima Spectre"),
                        SelectOption(label="POLYfrog Spectre",value="POLYfrog Spectre"),
                        SelectOption(label="Neuroblaster Spectre",value="Neuroblaster Spectre"),
                        SelectOption(label="Infinity Spectre",value="Infinity Spectre"),
                        SelectOption(label="Convex Spectre",value="Convex Spectre"),
                        SelectOption(label="BlastX Spectre",value="BlastX Spectre"),
                        SelectOption(label="Wasteland Spectre",value="Wasteland Spectre"),
                        ])    
                    ]
                ) 
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="VALORANT GO! Vol. 1":
                    embed = discord.Embed(
                        title="VALORANT GO! Vol. 1",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/d/d1/Spectre_valorant_go%21_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                       
               
                if _res.component[0].value=="Singularity Spectre":
                    embed = discord.Embed(
                        title="Singularity Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b0/Spectre_singularity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                       
        
        
        
                if _res.component[0].value=="Hivemind Spectre":
                    embed = discord.Embed(
                        title="Hivemind Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/4a/Spectre_hivemind_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
          
        
        
                if _res.component[0].value=="Forsaken Spectre":
                    embed = discord.Embed(
                        title="Forsaken Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/70/Spectre_forsaken_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                       
        
                if _res.component[0].value=="Infantry Spectre":
                    embed = discord.Embed(
                        title="Infantry Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/50/Spectre_infantry_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                       
      
        
                if _res.component[0].value=="Horizon Spectre":
                    embed = discord.Embed(
                        title="Horizon Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/bc/Spectre_horizon_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                       
        
        
                if _res.component[0].value=="Prime Spectre":
                    embed = discord.Embed(
                        title="Prime Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a9/Spectre_prime_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
                if _res.component[0].value=="Avalanche Spectre":
                    embed = discord.Embed(
                        title="Avalanche Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/84/Spectre_avalanche_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
        
                if _res.component[0].value=="Prism Spectre":
                    embed = discord.Embed(
                        title="Prism Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/ef/Spectre_prism_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
                if _res.component[0].value=="Serenity Spectre":
                    embed = discord.Embed(
                        title="Serenity Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 40")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/70/Spectre_serenity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
        
        
                if _res.component[0].value=="Ruination Spectre":
                    embed = discord.Embed(
                        title="Ruination Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://www.splitskins.com/uploads/1/3/3/8/133851419/spectre-king-standard-sideview_orig.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
                if _res.component[0].value=="Kingdom Spectre":
                    embed = discord.Embed(
                        title="Kingdom Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 5")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/37/Spectre_kingdom_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
        
                if _res.component[0].value=="Luxe Spectre":
                    embed = discord.Embed(
                        title="Luxe Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/3d/Spectre_luxe_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
        

        
                if _res.component[0].value=="Magepunk Spectre":
                    embed = discord.Embed(
                        title="Magepunk Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/54/Spectre_magepunk_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
        
                if _res.component[0].value=="Spline Spectre":
                    embed = discord.Embed(
                        title="Spline Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/23/Spectre_spline_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
        
        
                if _res.component[0].value=="Minima Spectre":
                    embed = discord.Embed(
                        title="Minima Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/ac/Spectre_minima_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
                 
                if _res.component[0].value=="POLYfrog Spectre":
                    embed = discord.Embed(
                        title="POLYfrog Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 40")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/56/Spectre_polyfrog_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
            
                if _res.component[0].value=="Neuroblaster Spectre":
                    embed = discord.Embed(
                        title="Neuroblaster Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/57/Spectre_g.u.n_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
            


                if _res.component[0].value=="Infinity Spectre":
                    embed = discord.Embed(
                        title="Infinity Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 16")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/95/Spectre_infinity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
            

                if _res.component[0].value=="Convex Spectre":
                    embed = discord.Embed(
                        title="Convex Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/83/Spectre_convex_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
            

                if _res.component[0].value=="BlastX Spectre":
                    embed = discord.Embed(
                        title="BlastX Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c3/Spectre_blastx_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
            
                if _res.component[0].value=="Wasteland Spectre":
                    embed = discord.Embed(
                        title="Wasteland Spectre",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/29/Spectre_wasteland_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Spectre/Skins")]) 
            

        if _res.user == ctx.author:
            if _res.component[0].value=="bucky":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Origin Bucky",value="Origin Bucky"),
                        SelectOption(label="Red Alert Bucky",value="Red Alert Bucky"),
                        SelectOption(label="Surge Bucky",value="Surge Bucky"),
                        SelectOption(label="Horizon Bucky",value="Horizon Bucky"),
                        SelectOption(label="Monarch Bucky",value="Monarch Bucky"),
                        SelectOption(label="Prime//2.0 Bucky",value="Prime//2.0 Bucky"),
                        SelectOption(label="Prism II Bucky",value="Prism II Bucky"),
                        SelectOption(label="Kingdom Bucky",value="Kingdom Bucky"),
                        SelectOption(label="Magepunk Bucky",value="Magepunk Bucky"),
                        SelectOption(label="Galleria Bucky",value="Galleria Bucky"),
                        SelectOption(label="Ion Bucky",value="Ion Bucky"),
                        SelectOption(label="Oni Bucky",value="Oni Bucky"),
                        SelectOption(label="Neuroblaster Bucky",value="Neuroblaster Bucky"),
                        SelectOption(label="Lightwave Bucky",value="Lightwave Bucky"),
                        SelectOption(label="Cavalier Bucky",value="Cavalier Bucky"),
                        SelectOption(label="Aerosol Bucky",value="Aerosol Bucky")
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="Origin Bucky":
                    embed = discord.Embed(
                        title="Origin Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/ff/Bucky_origin_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
                       
                if _res.component[0].value=="Red Alert Bucky":
                    embed = discord.Embed(
                        title="Red Alert Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 30")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/9f/Bucky_red_alert_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
                       
               
                if _res.component[0].value=="Surge Bucky":
                    embed = discord.Embed(
                        title="Surge Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 10")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/9f/Bucky_red_alert_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
                       

                if _res.component[0].value=="Horizon Bucky":
                    embed = discord.Embed(
                        title="Horizon Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/82/Bucky_horizon_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
    
                if _res.component[0].value=="Monarch Bucky":
                    embed = discord.Embed(
                        title="Monarch Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: EP. 03 Act 1 Battle Pass")
                    embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/fa/Monarch_Bucky.png/revision/latest?cb=20210623170200")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
          
    
                if _res.component[0].value=="Prime//2.0 Bucky":
                    embed = discord.Embed(
                        title="Prime//2.0 Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/58/Bucky_prime_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
          
          
    
                if _res.component[0].value=="Prism II Bucky":
                    embed = discord.Embed(
                        title="Prism II Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/71/Bucky_prism_ii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     
                if _res.component[0].value=="Kingdom Bucky":
                    embed = discord.Embed(
                        title="Kingdom Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 1")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/ec/Bucky_kingdom_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     

     
                if _res.component[0].value=="Magepunk Bucky":
                    embed = discord.Embed(
                        title="Magepunk Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/93/Bucky_magepunk_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     
                if _res.component[0].value=="Galleria Bucky":
                    embed = discord.Embed(
                        title="Galleria Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/8b/Bucky_galleria_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     
                if _res.component[0].value=="Ion Bucky":
                    embed = discord.Embed(
                        title="Ion Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e3/Bucky_ion_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     

                if _res.component[0].value=="Neuroblaster Bucky":
                    embed = discord.Embed(
                        title="Neuroblaster Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/31/Bucky_g.u.n_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
                

                if _res.component[0].value=="Lightwave Bucky":
                    embed = discord.Embed(
                        title="Lightwave Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 16")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/35/Bucky_lightwave_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     
                if _res.component[0].value=="Cavalier Bucky":
                    embed = discord.Embed(
                        title="Cavalier Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 30")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/0b/Bucky_cavalier_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     
     
                if _res.component[0].value=="Aerosol Bucky":
                    embed = discord.Embed(
                        title="Aerosol Bucky",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 5")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/78/Bucky_aerosol_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bucky/Skins")]) 
     

        if _res.user == ctx.author:
            if _res.component[0].value=="judge":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Glitchpop Judge",value="Glitchpop Judge"),
                        SelectOption(label="Enderflame Judge",value="Elderflame Judge"),
                        SelectOption(label="Rush Judge",value="Rush Judge"),
                        SelectOption(label="dot EXE Judge",value="dot EXE Judge"),
                        SelectOption(label="Outpost Judge",value="Outpost Judge"),
                        SelectOption(label="Prism III Judge",value="Prism III Judge"),
                        SelectOption(label="Serenity Judge",value="Serenity Judge"),
                        SelectOption(label="Smite Judge",value="Smite Judge"),
                        SelectOption(label="Celestial Judge",value="Celestial Judge"),
                        SelectOption(label="Luxe Judge",value="Luxe Judge"),
                        SelectOption(label="POLYfox Judge",value="POLYfox Judge"),
                        SelectOption(label="Jigsaw Judge",value="Jigsaw Judge"),
                        SelectOption(label="Sensation Judge",value="Sensation Judge"),
                        SelectOption(label="Convex Judge",value="Convex Judge"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="Glitchpop Judge":
                    embed = discord.Embed(
                        title="Glitchpop Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/86/Judge_glitchpop_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                
                if _res.component[0].value=="Elderflame Judge":
                    embed = discord.Embed(
                        title="Enderflame Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,475 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/2b/Judge_enderflame_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                
                if _res.component[0].value=="Rush Judge":
                    embed = discord.Embed(
                        title="Rush Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b8/Judge_rush_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                
                if _res.component[0].value=="dot EXE Judge":
                    embed = discord.Embed(
                        title="dot EXE Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 40")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/05/Judge_dot_exe_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                

                if _res.component[0].value=="Outpost Judge":
                    embed = discord.Embed(
                        title="Outpost Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 20")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/5d/Judge_outpost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                
                if _res.component[0].value=="Rush Judge":
                    embed = discord.Embed(
                        title="Rush Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b8/Judge_rush_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                

                if _res.component[0].value=="Prism III Judge":
                    embed = discord.Embed(
                        title="Prism III Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/fb/Judge_prism_iii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                

                if _res.component[0].value=="Serenity Judge":
                    embed = discord.Embed(
                        title="Serenity Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 15")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/69/Judge_serenity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                

                if _res.component[0].value=="Smite Judge":
                    embed = discord.Embed(
                        title="Smite Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/34/Judge_smite_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                
                if _res.component[0].value=="Celestial Judge":
                    embed = discord.Embed(
                        title="Celestial Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/cd/Judge_celestial_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                

                if _res.component[0].value=="Luxe Judge":
                    embed = discord.Embed(
                        title="Luxe Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/1c/Judge_luxe_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                
                if _res.component[0].value=="POLYfox Judge":
                    embed = discord.Embed(
                        title="POLYfox Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 10")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/5c/Judge_polyfox_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                
                
                if _res.component[0].value=="Jigsaw Judge":
                    embed = discord.Embed(
                        title="Jigsaw Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Reflexion: Act 1 Level 15")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f1/Judge_jigsaw_killjoy_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                

                if _res.component[0].value=="Sensation Judge":
                    embed = discord.Embed(
                        title="Sensation Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/78/Judge_sensation_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                

                if _res.component[0].value=="Convex Judge":
                    embed = discord.Embed(
                        title="Convex Judge",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/1c/Judge_convex_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Judge/Skins")]) 
                







        if _res.user == ctx.author:
            if _res.component[0].value=="bulldog":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Aristocrat Bulldog",value="Aristocrat Bulldog"),
                        SelectOption(label="Glitchpop Bulldog",value="Glitchpop Bulldog"),
                        SelectOption(label="Rush Bulldog",value="Rush Bulldog"),
                        SelectOption(label="Horizon Bulldog",value="Horizon Bulldog"),
                        SelectOption(label="K/TAC Bulldog",value="K/TAC Bulldog"),
                        SelectOption(label="Couture Bulldog",value="Couture Bulldog"),
                        SelectOption(label="POLYfox Bulldog",value="POLYfox Bulldog"),
                        SelectOption(label="Infinity Bulldog",value="Infinity Bulldog"),
                        SelectOption(label="Convex Bulldog",value="Convex Bulldog"),
                        SelectOption(label="Depths Bulldog",value="Depths Bulldog"),
                        ])    
                    ]
                )

                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="Aristocrat Bulldog":
                    embed = discord.Embed(
                        title="Aristocrat Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/64/Bulldog_aristocrat_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                
                if _res.component[0].value=="Glitchpop Bulldog":
                    embed = discord.Embed(
                        title="Glitchpop Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b4/Bulldog_glitchpop_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                
                
                if _res.component[0].value=="Rush Bulldog":
                    embed = discord.Embed(
                        title="Rush Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/83/Bulldog_rush_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                                
                if _res.component[0].value=="Horizon Bulldog":
                    embed = discord.Embed(
                        title="Horizon Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e3/Bulldog_horizon_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                                                
                if _res.component[0].value=="K/TAC Bulldog":
                    embed = discord.Embed(
                        title="K/TAC Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="REFLECTION : Act 1 battlepass")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/k-tac-bulldog.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                
                if _res.component[0].value=="Couture Bulldog":
                    embed = discord.Embed(
                        title="Couture Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 10")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c4/Bulldog_couture_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                
                if _res.component[0].value=="POLYfox Bulldog":
                    embed = discord.Embed(
                        title="POLYfox Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 15")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/4b/Bulldog_polyfox_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                                  
                if _res.component[0].value=="POLYfox Bulldog":
                    embed = discord.Embed(
                        title="POLYfox Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 1")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e6/Bulldog_infinity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                               
                if _res.component[0].value=="Convex Bulldog":
                    embed = discord.Embed(
                        title="Convex Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/04/Bulldog_convex_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                               
                              
                if _res.component[0].value=="Depths Bulldog":
                    embed = discord.Embed(
                        title="Depths Bulldog",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 5")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/15/Bulldog_depths_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Bulldog/Skins")]) 
                               





        if _res.user == ctx.author:
            if _res.component[0].value=="guardian":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="VALORANT GO! Vol. 1",value="VALORANT GO! Vol. 1"),
                        SelectOption(label="Nebula Guardian",value="Nebula Guardian"),
                        SelectOption(label="Songsteel Guardian",value="Songsteel Guardian"),
                        SelectOption(label="Ruin Guardian",value="Ruin Guardian"),
                        SelectOption(label="Infantry Guardian",value="Infantry Guardian"),
                        SelectOption(label="Prime Guardian",value="Prime Guardian"),
                        SelectOption(label="Galleria Guardian",value="Galleria Guardian"),
                        SelectOption(label="Oni Guardian",value="Oni Guardian"),
                        SelectOption(label="POLYfox Guardian",value="POLYfox Guardian"),
                        SelectOption(label="Jigsaw Guardian",value="Jigsaw Guardian"),
                        SelectOption(label="Reaver Guardian",value="Reaver Guardian"),
                        SelectOption(label="Sovereign Guardian",value="Sovereign Guardian"),
                        SelectOption(label="Tethered Realms Guardian",value="Tethered Realms Guardian"),
                        SelectOption(label="Infinity Guardian",value="Infinity Guardian"),
                        SelectOption(label="Ego Guardian",value="Ego Guardian"),
                        ])    
                    ]
                )

                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="VALORANT GO! Vol. 1":
                    embed = discord.Embed(
                        title="VALORANT GO! Vol. 1 Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/00/Guardian_valorant_go%21_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                if _res.component[0].value=="Nebula Guardian":
                    embed = discord.Embed(
                        title="Nebula Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/4a/Guardian_nebula_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                                
                if _res.component[0].value=="Songsteel Guardian":
                    embed = discord.Embed(
                        title="Songsteel Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 1")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/03/Guardian_songsteel_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                if _res.component[0].value=="Ruin Guardian":
                    embed = discord.Embed(
                        title="Ruin Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 30")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/fb/Guardian_ruin_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                
                if _res.component[0].value=="Infantry Guardian":
                    embed = discord.Embed(
                        title="Infantry Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/0f/Guardian_infantry_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                

                
                if _res.component[0].value=="Prime Guardian":
                    embed = discord.Embed(
                        title="Prime Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/68/Guardian_prime_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                 
                if _res.component[0].value=="Galleria Guardian":
                    embed = discord.Embed(
                        title="Galleria Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/7f/Guardian_galleria_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                if _res.component[0].value=="Oni Guardian":
                    embed = discord.Embed(
                        title="Oni Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/cb/Guardian_oni_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                
                if _res.component[0].value=="POLYfox Guardian":
                    embed = discord.Embed(
                        title="POLYfox Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 20")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/0d/Guardian_polyfox_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
              
                
                if _res.component[0].value=="Jigsaw Guardian":
                    embed = discord.Embed(
                        title="Jigsaw Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Reflexion: Act 1 Level 35")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/3a/Guardian_jigsaw_astra_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                
                
                if _res.component[0].value=="Reaver Guardian":
                    embed = discord.Embed(
                        title="Reaver Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/99/Guardian_reaver_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                
                
                if _res.component[0].value=="Sovereign Guardian":
                    embed = discord.Embed(
                        title="Sovereign Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/6e/Guardian_sovereign_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                

             
                if _res.component[0].value=="Tethered Realms Guardian":
                    embed = discord.Embed(
                        title="Tethered Realms Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/33/Guardian_tethered_realms_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                             
                if _res.component[0].value=="Infinity Guardian":
                    embed = discord.Embed(
                        title="Infinity Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 1")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c5/Guardian_infinity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                if _res.component[0].value=="Ego Guardian":
                    embed = discord.Embed(
                        title="Ego Guardian",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/2c/Guardian_ego_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Guardian/Skins")]) 
                
                
        if _res.user == ctx.author:
            if _res.component[0].value=="vandal":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Aristocrat Vandal",value="Aristocrat Vandal"),
                        SelectOption(label="Origin Vandal",value="Origin Vandal"),
                        SelectOption(label="Glitchpop Vandal",value="Glitchpop Vandal"),
                        SelectOption(label="Enderflame Vandal",value="Enderflame Vandal"),
                        SelectOption(label="Hivemind Vandal",value="Hivemind Vandal"),
                        SelectOption(label="Forsaken Vandal",value="Forsaken Vandal"),
                        SelectOption(label="Ruin Vandal",value="Ruin Vandal"),
                        SelectOption(label="dot EXE Vandal",value="dot EXE Vandal"),
                        SelectOption(label="Horizon Vandal",value="Horizon Vandal"),
                        SelectOption(label="Prime Vandal",value="Prime Vandal"),
                        SelectOption(label="Avalanche Vandal",value="Avalanche Vandal"),
                        SelectOption(label="Prism II Vandal",value="Prism II Vandal"),
                        SelectOption(label="K/TAC Vandal",value="K/TAC Vandal"),
                        SelectOption(label="Luxe Vandal",value="Luxe Vandal"),
                        SelectOption(label="Silvanus Vandal",value="Silvanus Vandal"),
                        SelectOption(label="Sensation Vandal",value="Sensation Vandal"),
                        SelectOption(label="Sakura Vandal",value="Sakura Vandal"),
                        SelectOption(label="Reaver Vandal",value="Reaver Vandal"),
                        SelectOption(label="Tethered Realms Vandal",value="Tethered Realms Vandal"),
                        SelectOption(label="Cavalier Vandal",value="Cavalier Vandal"),
                        SelectOption(label="Depths Vandal",value="Depths Vandal"),
                        SelectOption(label="Ego Vandal",value="Ego Vandal"),
                        SelectOption(label="Wasteland Vandal",value="Wasteland Vandal"),
                        SelectOption(label="Winterwunderland",value="Winterwunderland"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="Aristocrat Vandal":
                    embed = discord.Embed(
                        title="Aristocrat Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/2c/Vandal_aristocrat_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
                if _res.component[0].value=="Origin Vandal":
                    embed = discord.Embed(
                        title="Origin Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/1f/Vandal_origin_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
                if _res.component[0].value=="Glitchpop Vandal":
                    embed = discord.Embed(
                        title="Glitchpop Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/ec/Vandal_glitchpop_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
          
                if _res.component[0].value=="Enderflame Vandal":
                    embed = discord.Embed(
                        title="Enderflame Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,475 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/51/Vandal_enderflame_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
                  
                if _res.component[0].value=="Hivemind Vandal":
                    embed = discord.Embed(
                        title="Hivemind Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 20")
                    embed.set_image(url="https://liquipedia.net/commons/images/2/20/Vandal_hivemind_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
                if _res.component[0].value=="Forsaken Vandal":
                    embed = discord.Embed(
                        title="Forsaken Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b1/Vandal_forsaken_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
     
                if _res.component[0].value=="Ruin Vandal":
                    embed = discord.Embed(
                        title="Ruin Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 45")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c5/Vandal_ruin_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
        
                if _res.component[0].value=="dot EXE Vandal":
                    embed = discord.Embed(
                        title="dot EXE Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 45")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e5/Vandal_dot_exe_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
        
                if _res.component[0].value=="Horizon Vandal":
                    embed = discord.Embed(
                        title="Horizon Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/6b/Vandal_horizon_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
            
           
                if _res.component[0].value=="Prime Vandal":
                    embed = discord.Embed(
                        title="Prime Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/85/Vandal_prime_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
   
                if _res.component[0].value=="Avalanche Vandal":
                    embed = discord.Embed(
                        title="Avalanche Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a5/Vandal_avalanche_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
                if _res.component[0].value=="Prism II Vandal":
                    embed = discord.Embed(
                        title="Prism II Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/96/Vandal_prism_ii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
    
                if _res.component[0].value=="K/TAC Vandal":
                    embed = discord.Embed(
                        title="K/TAC Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Reflection: Act 1 battlepass")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/k-tac-vandal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
                if _res.component[0].value=="Luxe Vandal":
                    embed = discord.Embed(
                        title="Luxe Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/48/Vandal_luxe_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
                if _res.component[0].value=="Silvanus Vandal":
                    embed = discord.Embed(
                        title="Silvanus Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/4d/Vandal_silvanus_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
        
                if _res.component[0].value=="Sensation Vandal":
                    embed = discord.Embed(
                        title="Sensation Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e2/Vandal_sensation_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
                if _res.component[0].value=="Sakura Vandal":
                    embed = discord.Embed(
                        title="Sakura Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/33/Vandal_sakura_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
                if _res.component[0].value=="Reaver Vandal":
                    embed = discord.Embed(
                        title="Reaver Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/4c/Vandal_reaver_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
        
        
                if _res.component[0].value=="Tethered Realms Vandal":
                    embed = discord.Embed(
                        title="Tethered Realms Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b1/Vandal_tethered_realms_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
       
                if _res.component[0].value=="Cavalier Vandal":
                    embed = discord.Embed(
                        title="Cavalier Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 25")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/0e/Vandal_cavalier_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                

       
                if _res.component[0].value=="Depths Vandal":
                    embed = discord.Embed(
                        title="Depths Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 45")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/30/Vandal_depths_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
       
                if _res.component[0].value=="Ego Vandal":
                    embed = discord.Embed(
                        title="Ego Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/d/d2/Vandal_ego_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
       
                if _res.component[0].value=="Wasteland Vandal":
                    embed = discord.Embed(
                        title="Wasteland Vandal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/d/d6/Vandal_wasteland_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
                if _res.component[0].value=="Winterwunderland":
                    embed = discord.Embed(
                        title="Winterwunderland",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://cx.valorbuff.com/blob/BRcfB9CUanCVlXv2K+x3lIs2KrLJBtcO5thS5+Q3K6bNKNiNi190laLqKacGva0E?w=900")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Vandal/Skins")]) 
                
        
        
        
        if _res.user == ctx.author:
            if _res.component[0].value=="ares":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Aristocrat Ares",value="Aristocrat Ares"),
                        SelectOption(label="Nebula Ares",value="Nebula Ares"),
                        SelectOption(label="Singularity Ares",value="Singularity Ares"),
                        SelectOption(label="Rush Ares",value="Rush Ares"),
                        SelectOption(label="Hivemind Ares",value="Hivemind Ares"),
                        SelectOption(label="Infantry Ares",value="Infantry Ares"),
                        SelectOption(label="Outpost Ares",value="Outpost Ares"),
                        SelectOption(label="Prism Ares",value="Prism Ares"),
                        SelectOption(label="Celestial Ares",value="Celestial Ares"),
                        SelectOption(label="Minima Ares",value="Minima Ares"),
                        SelectOption(label="POLYfrog Ares",value="POLYfrog Ares"),
                        SelectOption(label="Jigsaw Ares",value="Jigsaw Ares"),
                        SelectOption(label="Sakura Ares",value="Sakura Ares"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="Aristocrat Ares":
                    embed = discord.Embed(
                        title="Aristocrat Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/97/Ares_aristocrat_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                

                if _res.component[0].value=="Nebula Ares":
                    embed = discord.Embed(
                        title="Nebula Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/9f/Ares_nebula_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                if _res.component[0].value=="Singularity Ares":
                    embed = discord.Embed(
                        title="Singularity Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/55/Ares_singularity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                if _res.component[0].value=="Rush Ares":
                    embed = discord.Embed(
                        title="Rush Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/65/Ares_rush_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                

                if _res.component[0].value=="Hivemind Ares":
                    embed = discord.Embed(
                        title="Hivemind Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 1")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e8/Ares_hivemind_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                
                if _res.component[0].value=="Infantry Ares":
                    embed = discord.Embed(
                        title="Infantry Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e4/Ares_infantry_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
        
        
           
                if _res.component[0].value=="Outpost Ares":
                    embed = discord.Embed(
                        title="Outpost Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 30")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f5/Ares_outpost_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
        
                if _res.component[0].value=="Prism Ares":
                    embed = discord.Embed(
                        title="Prism Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a7/Ares_prism_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                if _res.component[0].value=="Luxe Ghost":
                    embed = discord.Embed(
                        title="Luxe Ghost",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e9/Ares_celestial_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                
                if _res.component[0].value=="Minima Ares":
                    embed = discord.Embed(
                        title="Minima Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/cb/Ares_minima_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                if _res.component[0].value=="POLYfrog Ares":
                    embed = discord.Embed(
                        title="POLYfrog Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 20")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/41/Ares_polyfrog_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                if _res.component[0].value=="Jigsaw Ares":
                    embed = discord.Embed(
                        title="Jigsaw Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Reflexion: Act 1 Level 5")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/0e/Ares_jigsaw_skye_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
                if _res.component[0].value=="Sakura Ares":
                    embed = discord.Embed(
                        title="Sakura Ares",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e0/Ares_sakura_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Ares/Skins")]) 
                
        
        
        
        
        if _res.user == ctx.author:
            if _res.component[0].value=="odin":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Glitchpop Odin",value="Glitchpop Odin"),
                        SelectOption(label="dot EXE Odin",value="dot EXE Odin"),
                        SelectOption(label="Prime//2.0 Odin",value="Prime//2.0 Odin"),
                        SelectOption(label="Prism III Odin",value="Prism III Odin"),
                        SelectOption(label="Smite Odin",value="Smite Odin"),
                        SelectOption(label="Sensation Odin",value="Sensation Odin"),
                        SelectOption(label="Lightwave Odin",value="Lightwave Odin"),
                        SelectOption(label="Aerosol Odin",value="Aerosol Odin"),
                        SelectOption(label="BlastX Odin",value="BlastX Odin"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

        
                if _res.component[0].value=="Glitchpop Odin":
                    embed = discord.Embed(
                        title="Glitchpop Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/ab/Odin_glitchpop_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
        
                if _res.component[0].value=="dot EXE Odin":
                    embed = discord.Embed(
                        title="dot EXE Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 30")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/5b/Odin_dot_exe_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
                if _res.component[0].value=="Prime//2.0 Odin":
                    embed = discord.Embed(
                        title="Prime//2.0 Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/57/Odin_prime_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
        
                if _res.component[0].value=="Prism III Odin":
                    embed = discord.Embed(
                        title="Prism III Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e6/Odin_prism_iii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
        
                if _res.component[0].value=="Smite Odin":
                    embed = discord.Embed(
                        title="Smite Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/e6/Odin_prism_iii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
                
                if _res.component[0].value=="Sensation Odin":
                    embed = discord.Embed(
                        title="Sensation Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/ae/Odin_sensation_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
        
                        
                if _res.component[0].value=="Lightwave Odin":
                    embed = discord.Embed(
                        title="Lightwave Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 35")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a1/Odin_lightwave_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
                if _res.component[0].value=="Aerosol Odin":
                    embed = discord.Embed(
                        title="Aerosol Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 40")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f5/Odin_aerosol_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
                if _res.component[0].value=="BlastX Odin":
                    embed = discord.Embed(
                        title="BlastX Odin",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/9c/Odin_blastx_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Odin/Skins")]) 
                
        
        
        
        
        
        if _res.user == ctx.author:
            if _res.component[0].value=="marshal":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Galleria marshal",value="Galleria marshal"),
                        SelectOption(label="Magepunk marshal",value="Magepunk marshal"),
                        SelectOption(label="Wasteland marshal",value="Wasteland marshal"),
                        SelectOption(label="Couture marshal",value="Couture marshal"),
                        SelectOption(label="Polyfrog marshal",value="Polyfrog marshal"),
                        SelectOption(label="Monarch marshal",value="Monarch marshal"),
                        SelectOption(label="Sovereign marshal",value="Sovereign marshal"),
                        SelectOption(label="Avalanche marshal",value="Avalanche marshal"),
                        SelectOption(label="Winter Wonderland",value="Winter Wonderland"),
                        SelectOption(label="Ruin marshal",value="Ruin marshal"),
                        SelectOption(label="Songsteel marshal",value="Songsteel marshal"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])
                
                if _res.component[0].value=="Galleria marshal":
                    embed = discord.Embed(
                        title="Galleria marshal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/galleria_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        
                if _res.component[0].value=="Magepunk marshal":
                    embed = discord.Embed(
                        title="Magepunk marshal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1775 [VP]")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/magepunk_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
                
                if _res.component[0].value=="Wasteland marshal":
                    embed = discord.Embed(
                        title="Wasteland marshal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1275 [VP]")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/wasteland_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        
                if _res.component[0].value=="Couture marshal":
                    embed = discord.Embed(
                        title="Couture marshal",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/couture_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        
        
        
                if _res.component[0].value=="Polyfrog marshal":
                    embed = discord.Embed(
                        title="Polyfrog marshal",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Episode 2: Act 2")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/polyfrog_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        
                if _res.component[0].value=="Monarch marshal":
                    embed = discord.Embed(
                        title="Monarch marshal",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Reflection: Act 1")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/monarch_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        
        
                if _res.component[0].value=="Sovereign marshal":
                    embed = discord.Embed(
                        title="Sovereign marshal",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1775 [VP]")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/sovereign_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 

                if _res.component[0].value=="Avalanche marshal":
                    embed = discord.Embed(
                        title="Avalanche marshal",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1275 [VP]")
                    embed.set_image(url="https://vgraphs.com/images/weapons/skins/full-details/valorant-avalanche-marshal-weapon-skin.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 

                if _res.component[0].value=="Winter Wonderland":
                    embed = discord.Embed(
                        title="Winter Wonderland",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1275 [VP]")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/winter_wonderland_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        
                if _res.component[0].value=="Ruin marshal":
                    embed = discord.Embed(
                        title="Ruin marshal",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/ruin_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        
                if _res.component[0].value=="Songsteel marshal":
                    embed = discord.Embed(
                        title="Songsteel marshal",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formaction: Act 3")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/songsteel_marshal.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Marshal/Skins")]) 
        



        
        if _res.user == ctx.author:
            if _res.component[0].value=="stinger":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Aristocrat Stinger",value="Aristocrat Stinger"),
                        SelectOption(label="Red Alert Stinger",value="Red Alert Stinger"),
                        SelectOption(label="Surge Stinger",value="Surge Stinger"),
                        SelectOption(label="Prism II Stinger",value="Prism II Stinger"),
                        SelectOption(label="Couture Stinger",value="Couture Stinger"),
                        SelectOption(label="Silvanus Stinger",value="Silvanus Stinger"),
                        SelectOption(label="Sensation Stinger",value="Sensation Stinger"),
                        SelectOption(label="Sakura Stinger",value="Sakura Stinger"),
                        SelectOption(label="Sovereign Stinger",value="Sovereign Stinger"),
                        SelectOption(label="Cavalier Stinger",value="Cavalier Stinger"),
                        SelectOption(label="Depths Stinger",value="Depths Stinger"),
                        SelectOption(label="Ego Stinger",value="Ego Stinger"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

                if _res.component[0].value=="Aristocrat Stinger":
                    embed = discord.Embed(
                        title="Aristocrat Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/ca/Stinger_aristocrat_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 

                if _res.component[0].value=="Red Alert Stinger":
                    embed = discord.Embed(
                        title="Red Alert Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 35")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/96/Stinger_red_alert_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
                
                if _res.component[0].value=="Surge Stinger":
                    embed = discord.Embed(
                        title="Surge Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 35")
                    embed.set_image(url="https://liquipedia.net/commons/images/e/ed/Stinger_surge_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
        
                if _res.component[0].value=="Prism II Stinger":
                    embed = discord.Embed(
                        title="Prism II Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/00/Stinger_prism_ii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
                
                if _res.component[0].value=="Couture Stinger":
                    embed = discord.Embed(
                        title="Couture Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition : Act 1 Tier 15")
                    embed.set_image(url="https://vgraphs.com/images/weapons/skins/full-details/valorant-couture-stinger-weapon-skin.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
                
                if _res.component[0].value=="Silvanus Stinger":
                    embed = discord.Embed(
                        title="Silvanus Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a2/Stinger_silvanus_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
        
                if _res.component[0].value=="Sensation Stinger":
                    embed = discord.Embed(
                        title="Sensation Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/6a/Stinger_sensation_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
                
                if _res.component[0].value=="Sakura Stinger":
                    embed = discord.Embed(
                        title="Sakura Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/19/Stinger_sakura_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
                
                if _res.component[0].value=="Sovereign Stinger":
                    embed = discord.Embed(
                        title="Sovereign Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/cf/Stinger_sovereign_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
                
                if _res.component[0].value=="Cavalier Stinger":
                    embed = discord.Embed(
                        title="Cavalier Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 10")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/3c/Stinger_cavalier_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
                
                if _res.component[0].value=="Depths Stinger":
                    embed = discord.Embed(
                        title="Depths Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 20")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/8f/Stinger_depths_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
        

                if _res.component[0].value=="Ego Stinger":
                    embed = discord.Embed(
                        title="Ego Stinger",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b8/Stinger_ego_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Stinger/Skins")]) 
        

        
        if _res.user == ctx.author:
            if _res.component[0].value=="phantom":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="VALORANT GO! Vol. 1",value="VALORANT GO! Vol. 1"),
                        SelectOption(label="Nebula Phantom",value="Nebula Phantom"),
                        SelectOption(label="Glitchpop Phantom",value="Glitchpop Phantom"),
                        SelectOption(label="Singularity Phantom",value="Singularity Phantom"),
                        SelectOption(label="Rush Phantom",value="Rush Phantom"),
                        SelectOption(label="Prime//2.0 Phantom",value="Prime//2.0 Phantom"),
                        SelectOption(label="Avalanche Phantom",value="Avalanche Phantom"),
                        SelectOption(label="Prism Phantom",value="Prism Phantom"),
                        SelectOption(label="Serenity Phantom",value="Serenity Phantom"),
                        SelectOption(label="Ruination Phantom",value="Ruination Phantom"),
                        SelectOption(label="Kingdom Phantom",value="Kingdom Phantom"),
                        SelectOption(label="Smite Phantom",value="Smite Phantom"),
                        SelectOption(label="Celestial Phantom",value="Celestial Phantom"),
                        SelectOption(label="Spline Phantom",value="Spline Phantom"),
                        SelectOption(label="Minima Phantom",value="Minima Phantom"),
                        SelectOption(label="Galleria Phantom",value="Galleria Phantom"),
                        SelectOption(label="Silvanus Phantom",value="Silvanus Phantom"),
                        SelectOption(label="Ion Phantom",value="Ion Phantom"),
                        SelectOption(label="Lightwave Phantom",value="Lightwave Phantom"),
                        SelectOption(label="Infinity Phantom",value="Infinity Phantom"),
                        SelectOption(label="BlastX Phantom",value="BlastX Phantom"),
                        SelectOption(label="Winterwunderland",value="Winterwunderland"),
                        ])    
                    ]
                )
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])
        
                if _res.component[0].value=="VALORANT GO! Vol. 1":
                    embed = discord.Embed(
                        title="VALORANT GO! Vol. 1",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/53/Phantom_valorant_go%21_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
        
                if _res.component[0].value=="Nebula Phantom":
                    embed = discord.Embed(
                        title="Nebula Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/d/d2/Phantom_nebula_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
            
                if _res.component[0].value=="Glitchpop Phantom":
                    embed = discord.Embed(
                        title="Glitchpop Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/88/Phantom_glitchpop_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
            
                if _res.component[0].value=="Singularity Phantom":
                    embed = discord.Embed(
                        title="Singularity Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/16/Phantom_singularity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
            
                if _res.component[0].value=="Rush Phantom":
                    embed = discord.Embed(
                        title="Rush Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/53/Phantom_rush_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
        
                if _res.component[0].value=="Prime//2.0 Phantom":
                    embed = discord.Embed(
                        title="Prime//2.0 Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/6/66/Phantom_prime_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
        
                if _res.component[0].value=="Avalanche Phantom":
                    embed = discord.Embed(
                        title="Avalanche Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/95/Phantom_avalanche_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                if _res.component[0].value=="Prism Phantom":
                    embed = discord.Embed(
                        title="Prism Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/9b/Phantom_prism_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                if _res.component[0].value=="Serenity Phantom":
                    embed = discord.Embed(
                        title="Serenity Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 25")
                    embed.set_image(url="https://liquipedia.net/commons/images/d/dc/Phantom_serenity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
        
                if _res.component[0].value=="Ruination Phantom":
                    embed = discord.Embed(
                        title="Ruination Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175  [VP]")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/ruination_phantom.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                if _res.component[0].value=="Kingdom Phantom":
                    embed = discord.Embed(
                        title="Kingdom Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 1 Level 25")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/05/Phantom_kingdom_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                
                if _res.component[0].value=="Smite Phantom":
                    embed = discord.Embed(
                        title="Smite Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f9/Phantom_smite_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                
                if _res.component[0].value=="Celestial Phantom":
                    embed = discord.Embed(
                        title="Celestial Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/01/Phantom_celestial_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                if _res.component[0].value=="Spline Phantom":
                    embed = discord.Embed(
                        title="Spline Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/cb/Phantom_spline_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                
                if _res.component[0].value=="Minima Phantom":
                    embed = discord.Embed(
                        title="Minima Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/d/d1/Phantom_minima_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                if _res.component[0].value=="Galleria Phantom":
                    embed = discord.Embed(
                        title="Galleria Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c2/Phantom_galleria_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
        
                if _res.component[0].value=="Silvanus Phantom":
                    embed = discord.Embed(
                        title="Silvanus Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/0/0b/Phantom_silvanus_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                if _res.component[0].value=="Ion Phantom":
                    embed = discord.Embed(
                        title="Ion Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/98/Phantom_ion_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
             
                if _res.component[0].value=="Lightwave Phantom":
                    embed = discord.Embed(
                        title="Lightwave Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 25")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/94/Phantom_lightwave_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
                
                if _res.component[0].value=="Infinity Phantom":
                    embed = discord.Embed(
                        title="Infinity Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 45")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b2/Phantom_infinity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
             
        
                if _res.component[0].value=="BlastX Phantom":
                    embed = discord.Embed(
                        title="BlastX Phantom",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/4f/Phantom_blastx_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
             
                if _res.component[0].value=="Winterwunderland":
                    embed = discord.Embed(
                        title="Winterwunderland",
                        color = discord.Color.green()   
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://vgraphs.com/images/weapons/skins/full-details/valorant-winterwunderland-phantom-weapon-skin.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Phantom/Skins")]) 
             
        
        if _res.user == ctx.author:
            if _res.component[0].value=="sheriff":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Aristocrat Sheriff",value="Aristocrat Sheriff"),
                        SelectOption(label="Nebula Sheriff",value="Nebula Sheriff"),
                        SelectOption(label="Singularity Sheriff",value="Singularity Sheriff"),
                        SelectOption(label="Surge Sheriff",value="Surge Sheriff"),
                        SelectOption(label="Protektor Sheriff",value="Protektor Sheriff"),
                        SelectOption(label="Prism II Sheriff",value="Prism II Sheriff"),
                        SelectOption(label="K/TAC Sheriff",value="K/TAC Sheriff"),
                        SelectOption(label="Minima Sheriff",value="Minima Sheriff"),
                        SelectOption(label="Silvanus Sheriff",value="Silvanus Sheriff"),
                        SelectOption(label="Ion Sheriff",value="Ion Sheriff"),
                        SelectOption(label="POLYfox Sheriff",value="POLYfox Sheriff"),
                        SelectOption(label="POLYfrog Sheriff",value="POLYfrog Sheriff"),
                        SelectOption(label="Lightwave Sheriff",value="Lightwave Sheriff"),
                        SelectOption(label="Sakura Sheriff",value="Sakura Sheriff"),
                        SelectOption(label="Peacekeeper Sheriff",value="Peacekeeper Sheriff"),
                        SelectOption(label="Reaver Sheriff",value="Reaver Sheriff"),
                        SelectOption(label="Standard Sheriff",value="Standard Sheriff"),
                        SelectOption(label="Convex Sheriff",value="Convex Sheriff"),
                        SelectOption(label="Wasteland Sheriff",value="Wasteland Sheriff"),
                        SelectOption(label="Game Over Sheriff",value="Game Over Sheriff"),
                        SelectOption(label="Death Wish Sheriff",value="Death Wish Sheriff"),
                        ])    
                    ]
                )  
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])


                if _res.component[0].value=="Aristocrat Sheriff":
                    embed = discord.Embed(
                        title="Aristocrat Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/3/30/Sheriff_aristocrat_sheriff_VALORANT.png/362px-Sheriff_aristocrat_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Nebula Sheriff":
                    embed = discord.Embed(
                        title="Nebula Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/4/4c/Sheriff_nebula_sheriff_VALORANT.png/362px-Sheriff_nebula_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Singularity Sheriff":
                    embed = discord.Embed(
                        title="Singularity Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/1/13/Sheriff_singularity_VALORANT.png/362px-Sheriff_singularity_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Surge Sheriff":
                    embed = discord.Embed(
                        title="Surge Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 3 Level 50")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/3/37/Sheriff_surge_VALORANT.png/362px-Sheriff_surge_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Protektor Sheriff":
                    embed = discord.Embed(
                        title="Protektor Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Sova Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/2/21/Sheriff_sova%27s_sheriff_VALORANT.png/362px-Sheriff_sova%27s_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Prism II Sheriff":
                    embed = discord.Embed(
                        title="Prism II Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/3/3d/Sheriff_prism_ii_VALORANT.png/362px-Sheriff_prism_ii_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="K/TAC Sheriff":
                    embed = discord.Embed(
                        title="K/TAC Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass : REFLECTION: Act 1")
                    embed.set_image(url="https://static.wikia.nocookie.net/valorant/images/0/08/KTAC_Sheriff.png/revision/latest/scale-to-width-down/512?cb=20210623170450")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Minima Sheriff":
                    embed = discord.Embed(
                        title="Minima Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/e/ec/Sheriff_minima_VALORANT.png/362px-Sheriff_minima_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Silvanus Sheriff":
                    embed = discord.Embed(
                        title="Silvanus Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/3/3c/Sheriff_silvanus_VALORANT.png/362px-Sheriff_silvanus_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Ion Sheriff":
                    embed = discord.Embed(
                        title="Ion Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/a/a7/Sheriff_ion_VALORANT.png/362px-Sheriff_ion_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Polyfox Sheriff":
                    embed = discord.Embed(
                        title="Polyfox Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 16")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/c/ca/Sheriff_polyfox_sheriff_VALORANT.png/362px-Sheriff_polyfox_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Polyfrog Sheriff":
                    embed = discord.Embed(
                        title="Polyfrog Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 15")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/2/21/Sheriff_polyfrog_VALORANT.png/362px-Sheriff_polyfrog_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="LightwaveSheriff":
                    embed = discord.Embed(
                        title="Lightwave Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 3 Level 10")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/5/5c/Sheriff_lightwave_VALORANT.png/362px-Sheriff_lightwave_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Sakura  Sheriff":
                    embed = discord.Embed(
                        title="Sakura  Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/b/b9/Sheriff_sakura_sheriff_VALORANT.png/362px-Sheriff_sakura_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Peacekeeper Sheriff":
                    embed = discord.Embed(
                        title="Peacekeeper Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Brimstone Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/d/d6/Sheriff_brimstone%27s_sheriff_VALORANT.png/362px-Sheriff_brimstone%27s_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Reaver  Sheriff":
                    embed = discord.Embed(
                        title="Reaver  Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/a/a4/Sheriff_reaver_VALORANT.png/362px-Sheriff_reaver_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Standard Sheriff":
                    embed = discord.Embed(
                        title="Standard Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Default Skin")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/9/96/Sheriff_sar-6_VALORANT.png/362px-Sheriff_sar-6_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Convex Sheriff":
                    embed = discord.Embed(
                        title="Convex Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/7/7f/Sheriff_convex_sheriff_VALORANT.png/362px-Sheriff_convex_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Wasteland Sheriff":
                    embed = discord.Embed(
                        title="Wasteland Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price:1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/5/5a/Sheriff_wasteland_VALORANT.png/362px-Sheriff_wasteland_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Game Over Sheriff":
                    embed = discord.Embed(
                        title="Game Over Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Jett Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/0/0e/Sheriff_jett%27s_sheriff_VALORANT.png/362px-Sheriff_jett%27s_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])

                if _res.component[0].value=="Death Wish Sheriff":
                    embed = discord.Embed(
                        title="Death Wish Sheriff",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Agent Contract: Yoru Level 9")
                    embed.set_image(url="https://liquipedia.net/commons/images/thumb/1/11/Sheriff_yoru%27s_sheriff_VALORANT.png/362px-Sheriff_yoru%27s_sheriff_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Sheriff/Skins")])
        
        
        
        
        if _res.user == ctx.author:
            if _res.component[0].value=="operator":
                await ctx.send("```SELECT THE SKIN```",
                    components=[
                        Select(placeholder='Selection',
                        options=[
                        SelectOption(label="Origin Operator",value="Origin Operator"),
                        SelectOption(label="Red Alert Operator",value="Red Alert Operator"),
                        SelectOption(label="Glitchpop Operator",value="Glitchpop Operator"),
                        SelectOption(label="Elderflame Operator",value="Elderflame Operator"),
                        SelectOption(label="Forsaken Operator",value="Forsaken Operator"),
                        SelectOption(label="Infantry Operator",value="Infantry Operator"),
                        SelectOption(label="K/TAC Operator",value="K/TAC Operator"),
                        SelectOption(label="Prism Operator",value="Prism Operator"),
                        SelectOption(label="Luxe Operator",value="Luxe Operator"),
                        SelectOption(label="Spline Operator",value="Spline Operator"),
                        SelectOption(label="Minima Operator",value="Minima Operator"),
                        SelectOption(label="Silvanus Operator",value="Silvanus Operator"),
                        SelectOption(label="Ion Operator",value="Ion Operator"),
                        SelectOption(label="Neuroblaster Operator",value="Neuroblaster Operator"),
                        SelectOption(label="Reaver Operator",value="Reaver Operator"),
                        SelectOption(label="Tethered Realms Operator",value="Tethered Realms Operator"),
                        SelectOption(label="Cavalier Operator",value="Cavalier Operator"),
                        SelectOption(label="Aerosol Operator",value="Aerosol Operator"),
                        SelectOption(label="Convex Operator",value="Convex Operator"),
                        ])    
                    ]
                )   
                _res = await self.bot.wait_for("select_option", check=lambda i: i.component[0])

        
                if _res.component[0].value=="Origin Operator":
                    embed = discord.Embed(
                        title="Origin Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/5/50/Operator_origin_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        
        
                if _res.component[0].value=="Red Alert Operator":
                    embed = discord.Embed(
                        title="Red Alert Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Ignition: Act 2 Level 45")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/cc/Operator_red_alert_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

                if _res.component[0].value=="Glitchpop Operator":
                    embed = discord.Embed(
                        title="Glitchpop Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,175 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/3d/Operator_glitchpop_2.0_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

                if _res.component[0].value=="Elderflame Operator":
                    embed = discord.Embed(
                        title="Elderflame Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 2,475 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/ba/Operator_elderflame_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        
                if _res.component[0].value=="Forsaken Operator":
                    embed = discord.Embed(
                        title="Forsaken Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/17/Operator_forsaken_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

       
                if _res.component[0].value=="Infantry Operator":
                    embed = discord.Embed(
                        title="Infantry Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/3/30/Operator_infantry_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        
                if _res.component[0].value=="K/TAC Operator":
                    embed = discord.Embed(
                        title="K/TAC Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Reflection: Act 1")
                    embed.set_image(url="https://cdn.valorantinfo.gg/img/skins/k-tac-operator.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

                if _res.component[0].value=="Prism Operator":
                    embed = discord.Embed(
                        title="Prism Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/1/1c/Operator_prism_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])


                if _res.component[0].value=="Luxe Operator":
                    embed = discord.Embed(
                        title="Luxe Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/9f/Operator_luxe_blue_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        
        

                if _res.component[0].value=="Spline Operator":
                    embed = discord.Embed(
                        title="Spline Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/ca/Operator_spline_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        

                if _res.component[0].value=="Minima Operator":
                    embed = discord.Embed(
                        title="Minima Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/7/76/Operator_minima_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

                if _res.component[0].value=="Silvanus Operator":
                    embed = discord.Embed(
                        title="Silvanus Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,275 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/b/b7/Operator_silvanus_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])
                
                if _res.component[0].value=="Ion Operator":
                    embed = discord.Embed(
                        title="Ion Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/44/Operator_ion_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        
        
                if _res.component[0].value=="Neuroblaster Operator":
                    embed = discord.Embed(
                        title="Neuroblaster Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/9/91/Operator_g.u.n_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

      
                if _res.component[0].value=="Reaver Operator":
                    embed = discord.Embed(
                        title="Reaver Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/8/83/Operator_reaver_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        
                if _res.component[0].value=="Tethered Realms Operator":
                    embed = discord.Embed(
                        title="Tethered Realms Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 1,775 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/c/c6/Operator_tethered_realms_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

                if _res.component[0].value=="Cavalier Operator":
                    embed = discord.Embed(
                        title="Cavalier Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 2 Level 45")
                    embed.set_image(url="https://liquipedia.net/commons/images/4/44/Operator_cavalier_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

                if _res.component[0].value=="Aerosol Operator":
                    embed = discord.Embed(
                        title="Aerosol Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Battlepass: Formation: Act 1 Level 25")
                    embed.set_image(url="https://liquipedia.net/commons/images/a/a8/Operator_aerosol_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

                if _res.component[0].value=="Convex Operator":
                    embed = discord.Embed(
                        title="Convex Operator",
                        color = discord.Color.green()
                    )
                    embed.add_field(name ="Availability",value="Price: 875 [VP]")
                    embed.set_image(url="https://liquipedia.net/commons/images/f/f7/Operator_convex_VALORANT.png")
                    await ctx.send(embed=embed,components=[Button(label="More", style=5, url="https://liquipedia.net/valorant/Operator/Skins")])

        
        
        else:
            _res.respond(content="You need to run your own command to do this")

def setup(bot):
    bot.add_cog(skin(bot))
    print("skins        | Imported")        