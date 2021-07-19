import discord
from discord.ext import commands
import traceback
import sys
import json 
import requests
from discord_components import *

with open ('config/config.json', 'r') as f:
    config = json.load(f)
    token = config['token']
    prefix = config['prefix']



bot = commands.Bot(command_prefix=f'{prefix}') #defining bot prefix 

bot.remove_command('help')




@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle, 
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"{prefix}vstat")
    )
    print("Bot online!")
    DiscordComponents(bot)



with open ('extension/extension.json', 'r') as data:
    cog_data = json.load(data)
    extension = cog_data['extension']

if __name__ == "__main__":
        for extension in extension:
            try:
                bot.load_extension(extension)
            except:
                print(f'Error loading {extension}', file=sys.stderr)
                traceback.print_exc()


bot.run(f"{token}")