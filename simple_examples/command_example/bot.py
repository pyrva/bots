# bot.py
import json
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='futurama')
async def nine_nine(ctx):
    curpath = os.path.abspath(os.curdir)
    filename = "simple_examples/command_example/futurama.json"
    filepath = os.path.join(curpath, filename)

    f = open(filepath)
    futurama_quotes = json.load(f)

    response = random.choice(futurama_quotes)
    print(response)
    await ctx.send(response)

@bot.command(name='zen')
async def nine_nine(ctx):
    curpath = os.path.abspath(os.curdir)
    filename = "simple_examples/command_example/zen_of_python.md"
    filepath = os.path.join(curpath, filename)
    f = open(filepath)
    lines = f.read()

    print(lines)
    await ctx.send(lines)


bot.run(TOKEN)
