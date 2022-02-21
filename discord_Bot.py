import discord
import config
from discord.ext import commands 

client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

client.run(config.TOKEN)