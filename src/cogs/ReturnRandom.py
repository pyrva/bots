import random

import discord
from discord import option
from discord.ext import commands


class ReturnRandom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
      name='roll_dice', 
      description='Simulates rolling dice.')
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
    async def _roll(self, ctx: discord.ApplicationContext, number_of_dice: int, number_of_sides: int):
      dice = [
          str(random.choice(range(1, number_of_sides + 1)))
          for _ in range(number_of_dice)
      ]
      await ctx.respond(', '.join(dice))

def setup(bot):
    bot.add_cog(ReturnRandom(bot))
