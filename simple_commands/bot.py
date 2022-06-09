# bot.py
import json
import os
import random
from discord.ext import commands

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = commands.Bot(command_prefix='!')
else:
    from builtins import bot

@bot.command(name='futurama', help='Responds with a random quote from Futurama', pass_context=True)
async def futurama(ctx):
    curpath = os.path.abspath(os.curdir)
    filename = "simple_examples/command_example/futurama.json"
    filepath = os.path.join(curpath, filename)

    f = open(filepath)
    futurama_quotes = json.load(f)

    response = random.choice(futurama_quotes)
    print(response)
    await ctx.send(response)

@bot.command(name='zen', help='Responds with zen of python by Tim Peters', pass_context=True)
async def zen(ctx):
    curpath = os.path.abspath(os.curdir)
    filename = "simple_examples/command_example/zen_of_python.md"
    filepath = os.path.join(curpath, filename)
    f = open(filepath)
    lines = f.read()

    print(lines)
    await ctx.send(lines)


@bot.command(name='roll_dice', help='Simulates rolling dice. Format: !roll_dice {num_of_dice} {num_of_sides} Example: !roll_dice 2 6', pass_context=True)
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

if __name__ == "__main__":
    bot.run(TOKEN)
