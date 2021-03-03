import discord
from discord.ext import commands
import random
from discord import Activity, ActivityType
client = commands.Bot(command_prefix = '$')
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('test'))
    print(f'{client.user.name} Is Now Online!')


client.run('TOKEN')
