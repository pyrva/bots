import json
import logging
import os
import random

from discord.ext import commands

logger = logging.getLogger(__name__)

class simple_fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.resource_folder = "cogs/simple_fun/"
    
    @commands.command(name='futurama', help='Responds with a random quote from Futurama', pass_context=True)
    async def futurama(self, ctx):
        curpath = os.path.abspath(os.curdir)
        filename = f"{self.resource_folder}futurama.json"
        filepath = os.path.join(curpath, filename)

        f = open(filepath)
        futurama_quotes = json.load(f)

        response = random.choice(futurama_quotes)

        logger.info(f'function: futurama / requester: {str(ctx.message.author).split("#")[0]}')
        logger.info(f'output:\n{response}')
        await ctx.send(response)

    @commands.command(name='zen', help='Responds with zen of python by Tim Peters', pass_context=True)
    async def zen(self, ctx):
        curpath = os.path.abspath(os.curdir)
        filename = f"{self.resource_folder}zen_of_python.md"
        filepath = os.path.join(curpath, filename)
        f = open(filepath)
        response = f.read()

        logger.info(f'function: zen / requester: {str(ctx.message.author).split("#")[0]}')
        # logger.info(f'output:\n{response}') # this is super long and will always be the same
        await ctx.send(response)


    @commands.command(name='roll_dice', help='Simulates rolling dice. Format: !roll_dice {num_of_dice} {num_of_sides} Example: !roll_dice 2 6', pass_context=True)
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))


def setup(bot):
    bot.add_cog(simple_fun(bot))
