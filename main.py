from settings import DISCORD_TOKEN

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='Tichu.')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms')

bot.run(DISCORD_TOKEN)




