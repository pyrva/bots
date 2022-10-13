import json
import logging
from pathlib import Path
import random

from discord.ext import commands

logger = logging.getLogger(__name__)


class SimpleFun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.resource_folder = "cogs/fun/"

    @commands.command(
        name='futurama', help='Responds with a random quote from Futurama',
        pass_context=True
    )
    async def futurama(self, ctx):
        futurama_quotes = json.loads(
            (Path(self.resource_folder) / 'futurama.json').read_text()
        )
        response = random.choice(futurama_quotes)

        logger.info(f'output:\n{response}')
        await ctx.send(response)

    @commands.command(
        name='zen', help='Responds with zen of python by Tim Peters',
        pass_context=True
    )
    async def zen(self, ctx):
        await ctx.send((Path(self.resource_folder) / 'zen_of_python.md').read_text())

    @commands.command(
        name='roll_dice',
        help='Simulates rolling dice. Format: !roll_dice {num_of_dice} {num_of_sides} Example: !roll_dice 2 6',
        pass_context=True
    )
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    # TODO Got the following error:
    # discord.ext.commands.errors.CommandInvokeError: Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions
    # @commands.command()
    # async def suggest(self, ctx, *, args):
    #     logger.info(f'function: suggest / requester: {str(ctx.message.author).split("#")[0]}')

    #     await ctx.message.delete()
    #     embed = discord.Embed(description=args, timestamp=ctx.message.created_at)
    #     embed.set_author(name=f"Suggestion by {ctx.message.author.display_name}", icon_url=ctx.message.author.avatar_url)
    #     msg = await ctx.send(embed=embed)
    #     await msg.add_reaction("👍")	
    #     await msg.add_reaction("👎")


async def setup(bot):
    await bot.add_cog(SimpleFun(bot))
