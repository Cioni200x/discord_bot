from http import client
import discord
import config
from discord.ext import commands 

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hello(ctx):
    author = ctx.message.author 

    await ctx.send(f'Hello, {author.mention}!')

client.run(config.TOKEN)
