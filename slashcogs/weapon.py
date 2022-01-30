import discord
from discord.ext import commands
from discord.commands import Option, slash_command
import requests
import json

def weapon_list():
	r = requests.get("https://valorant-api.com/v1/weapons")
	data = r.json()
	weapons = []
	weapon_dict = {}

	for i in range(len(data["data"])):
		name = data["data"][i]["displayName"]
		weapons.append(name)
		weapon_dict[name] = data["data"][i]["uuid"] 
	
	weapons.remove("Melee") #;-; no questions pls
	
	return weapons, weapon_dict



def weapon_stats(uuid):

	WEAPON_STAT = {}
	r = requests.get(f"https://valorant-api.com/v1/weapons/{uuid}")
	data = r.json()

	WEAPON_STAT["displayName"] = data["data"]["displayName"]
	WEAPON_STAT["displayIcon"] = data["data"]["displayIcon"]
	WEAPON_STAT["killStreamIcon"] = data["data"]["killStreamIcon"]
	WEAPON_STAT["weaponStats"] = data["data"]["weaponStats"]
	

	return WEAPON_STAT

def embed_maker(WEAPON_STAT):
	
	if len(WEAPON_STAT["weaponStats"]["damageRanges"]) == 0:
		embed = discord.Embed(
			colour = discord.Colour.random(),
			title = WEAPON_STAT["displayName"],

		)
		embed.add_field(name = "PRIMARY FIRE", value=f"""
		> :small_blue_diamond: fireRate - {WEAPON_STAT["weaponStats"]["fireRate"]} 
		> :small_blue_diamond: magazineSize - {WEAPON_STAT["weaponStats"]["magazineSize"]} 
		> :small_blue_diamond: runSpeedMultiplier - {WEAPON_STAT["weaponStats"]["runSpeedMultiplier"]} 
		> :small_blue_diamond: reloadTimeSeconds - {WEAPON_STAT["weaponStats"]["reloadTimeSeconds"]} 
		> :small_blue_diamond: firstBulletAccuracy - {WEAPON_STAT["weaponStats"]["firstBulletAccuracy"]} 
		""")
		embed.set_image(url=WEAPON_STAT["displayIcon"])
		embed.set_thumbnail(url=WEAPON_STAT["killStreamIcon"])
	
	elif len(WEAPON_STAT["weaponStats"]["damageRanges"]) == 1:
			
		embed = discord.Embed(
			colour = discord.Colour.random(),
			title = WEAPON_STAT["displayName"],

		)
		embed.add_field(name = "PRIMARY FIRE", value=f"""
		> :small_blue_diamond: fireRate - {WEAPON_STAT["weaponStats"]["fireRate"]} 
		> :small_blue_diamond: magazineSize - {WEAPON_STAT["weaponStats"]["magazineSize"]} 
		> :small_blue_diamond: runSpeedMultiplier - {WEAPON_STAT["weaponStats"]["runSpeedMultiplier"]} 
		> :small_blue_diamond: reloadTimeSeconds - {WEAPON_STAT["weaponStats"]["reloadTimeSeconds"]} 
		> :small_blue_diamond: firstBulletAccuracy - {WEAPON_STAT["weaponStats"]["firstBulletAccuracy"]} 
		""")
		embed.add_field(name = "DAMAGE", value=f"""
		> `{WEAPON_STAT["weaponStats"]["damageRanges"][0]["rangeStartMeters"]}` - `{WEAPON_STAT["weaponStats"]["damageRanges"][0]["rangeEndMeters"]}`| Head : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["headDamage"]} | Body : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["bodyDamage"]} | Leg : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["legDamage"]}  
		""",inline=False)
		embed.set_image(url=WEAPON_STAT["displayIcon"])
		embed.set_thumbnail(url=WEAPON_STAT["killStreamIcon"])

	elif len(WEAPON_STAT["weaponStats"]["damageRanges"]) == 2:
			
		embed = discord.Embed(
			colour = discord.Colour.random(),
			title = WEAPON_STAT["displayName"],

		)
		embed.add_field(name = "PRIMARY FIRE", value=f"""
		> :small_blue_diamond: fireRate - {WEAPON_STAT["weaponStats"]["fireRate"]} 
		> :small_blue_diamond: magazineSize - {WEAPON_STAT["weaponStats"]["magazineSize"]} 
		> :small_blue_diamond: runSpeedMultiplier - {WEAPON_STAT["weaponStats"]["runSpeedMultiplier"]} 
		> :small_blue_diamond: reloadTimeSeconds - {WEAPON_STAT["weaponStats"]["reloadTimeSeconds"]} 
		> :small_blue_diamond: firstBulletAccuracy - {WEAPON_STAT["weaponStats"]["firstBulletAccuracy"]} 
		""")
		embed.add_field(name = "DAMAGE", value=f"""
		> `{WEAPON_STAT["weaponStats"]["damageRanges"][0]["rangeStartMeters"]}` - `{WEAPON_STAT["weaponStats"]["damageRanges"][0]["rangeEndMeters"]}`| Head : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["headDamage"]} | Body : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["bodyDamage"]} | Leg : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["legDamage"]}  
		> `{WEAPON_STAT["weaponStats"]["damageRanges"][1]["rangeStartMeters"]}` - `{WEAPON_STAT["weaponStats"]["damageRanges"][1]["rangeEndMeters"]}`| Head : {WEAPON_STAT["weaponStats"]["damageRanges"][1]["headDamage"]} | Body : {WEAPON_STAT["weaponStats"]["damageRanges"][1]["bodyDamage"]} | Leg : {WEAPON_STAT["weaponStats"]["damageRanges"][1]["legDamage"]}  
		""",inline=False)
		embed.set_image(url=WEAPON_STAT["displayIcon"])
		embed.set_thumbnail(url=WEAPON_STAT["killStreamIcon"])

	elif len(WEAPON_STAT["weaponStats"]["damageRanges"]) == 3:
			
		embed = discord.Embed(
			colour = discord.Colour.random(),
			title = WEAPON_STAT["displayName"],

		)
		embed.add_field(name = "PRIMARY FIRE", value=f"""
		> :small_blue_diamond: fireRate - {WEAPON_STAT["weaponStats"]["fireRate"]} 
		> :small_blue_diamond: magazineSize - {WEAPON_STAT["weaponStats"]["magazineSize"]} 
		> :small_blue_diamond: runSpeedMultiplier - {WEAPON_STAT["weaponStats"]["runSpeedMultiplier"]} 
		> :small_blue_diamond: reloadTimeSeconds - {WEAPON_STAT["weaponStats"]["reloadTimeSeconds"]} 
		> :small_blue_diamond: firstBulletAccuracy - {WEAPON_STAT["weaponStats"]["firstBulletAccuracy"]} 
		""")
		embed.add_field(name = "DAMAGE", value=f"""
		> `{WEAPON_STAT["weaponStats"]["damageRanges"][0]["rangeStartMeters"]}` - `{WEAPON_STAT["weaponStats"]["damageRanges"][0]["rangeEndMeters"]}`| Head : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["headDamage"]} | Body : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["bodyDamage"]} | Leg : {WEAPON_STAT["weaponStats"]["damageRanges"][0]["legDamage"]}  
		> `{WEAPON_STAT["weaponStats"]["damageRanges"][1]["rangeStartMeters"]}` - `{WEAPON_STAT["weaponStats"]["damageRanges"][1]["rangeEndMeters"]}`| Head : {WEAPON_STAT["weaponStats"]["damageRanges"][1]["headDamage"]} | Body : {WEAPON_STAT["weaponStats"]["damageRanges"][1]["bodyDamage"]} | Leg : {WEAPON_STAT["weaponStats"]["damageRanges"][1]["legDamage"]} 
		> `{WEAPON_STAT["weaponStats"]["damageRanges"][2]["rangeStartMeters"]}` - `{WEAPON_STAT["weaponStats"]["damageRanges"][2]["rangeEndMeters"]}`| Head : {WEAPON_STAT["weaponStats"]["damageRanges"][2]["headDamage"]} | Body : {WEAPON_STAT["weaponStats"]["damageRanges"][2]["bodyDamage"]} | Leg : {WEAPON_STAT["weaponStats"]["damageRanges"][2]["legDamage"]}   
		""",inline=False)
		embed.set_image(url=WEAPON_STAT["displayIcon"])
		embed.set_thumbnail(url=WEAPON_STAT["killStreamIcon"])

	return embed


class slash_weapon(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	weapon_list, wpn_dict = weapon_list()
	@commands.slash_command(description="Get info. about weapons")
	async def weapon(
			self,
			ctx,
			name: Option(str, "Choose the weapon", choices=weapon_list, required=True)
		):
			await ctx.response.defer()
			weapon_lists, wp_dict = weapon_list()
			uuid = wp_dict[name]
			WEAPON_STAT = weapon_stats(uuid)
			embed = embed_maker(WEAPON_STAT)

			view = discord.ui.View()
			view.add_item(discord.ui.Button(label='Support Server', url='https://discord.gg/m5mSyTV7RR', style=discord.ButtonStyle.url))
			view.add_item(discord.ui.Button(label='Vote', url='https://top.gg/bot/864451929346539530/vote', style=discord.ButtonStyle.url))
		
			
			await ctx.respond(embed=embed,view=view)
			
def setup(bot):
	bot.add_cog(slash_weapon(bot))
