import json
import logging
import os
import random

import discord
from discord import option
from discord.commands import SlashCommandGroup
from discord.ext import commands

logger = logging.getLogger(__name__)


class ForFun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.resource_folder = "cogs/fun/"

    fun = SlashCommandGroup("fun", "for the lolz")

    @fun.command(description="Responds with a random quote from Futurama")
    async def futurama(self, ctx: discord.ApplicationContext):
        curpath = os.path.abspath(os.curdir)
        filename = f"{self.resource_folder}futurama.json"
        filepath = os.path.join(curpath, filename)

        f = open(filepath)
        futurama_quotes = json.load(f)

        response = random.choice(futurama_quotes)

        logger.info(f"output:\n{response}")
        await ctx.respond(response)

    @fun.command(description="Responds with zen of python by Tim Peters")
    async def zen(self, ctx: discord.ApplicationContext):
        curpath = os.path.abspath(os.curdir)
        filename = f"{self.resource_folder}zen_of_python.md"
        filepath = os.path.join(curpath, filename)
        f = open(filepath)
        response = f.read()
        await ctx.respond(response)

    @fun.command()
    async def suggest(self, ctx, *, args):
        logger.info(
            f'function: suggest / requester: {str(ctx.message.author).split("#")[0]}'
        )

        await ctx.message.delete()
        embed = discord.Embed(description=args, timestamp=ctx.message.created_at)
        embed.set_author(
            name=f"Suggestion by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar_url,
        )
        msg = await ctx.respond(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @fun.command(name="roll_dice", description="Simulates rolling dice.")
    @option(
        name="number_of_dice",
        description="number of dice",
        min_value=1,
        max_value=99,
        required=True,
    )
    @option(
        name="number_of_sides",
        description="number of sides",
        min_value=1,
        max_value=99,
        required=True,
    )
    async def _roll(
        self, ctx: discord.ApplicationContext, number_of_dice: int, number_of_sides: int
    ):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.respond(", ".join(dice))


def setup(bot):
    bot.add_cog(ForFun(bot))
