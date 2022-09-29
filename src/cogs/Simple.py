# This example demonstrates a standalone cog file with the bot instance in a separate file.

import discord
from discord import option
from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        description="ping -> pong",
    )
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond("pong!")
    
    @commands.slash_command(
        name="say_something",
        description="say something!"
    )
    @option(
        name="text",
        description="What you want repeated back to you",
        required=True,
    )
    async def _say_something(self, ctx: discord.ApplicationContext, text: str):
        await ctx.send(f"You said '{text}'!")

def setup(bot):
    bot.add_cog(Example(bot))
