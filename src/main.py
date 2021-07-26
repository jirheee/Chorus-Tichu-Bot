from settings import DISCORD_TOKEN, GUILD_NAME

from discord.ext import commands
import random
import discord

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content == "Hello":
#         response = "Hello! I'm Chorus Tichu Bot."
#         await message.channel.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    print("roll!")
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


bot.run(DISCORD_TOKEN)




