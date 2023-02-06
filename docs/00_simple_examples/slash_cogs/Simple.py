# This example demonstrates a standalone cog file with the bot instance in a separate file.
import discord
from discord import option
from discord.ext import commands


class Simple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="ping -> pong")
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond("pong!")

    @commands.slash_command(description="Say something and the bot will respond!")
    @option(
        name="text",
        description="What you want repeated back to you",
        required=True,
    )
    async def say_something(self, ctx: discord.ApplicationContext, text: str):
        await ctx.respond(f"You said '{text}'!")


def setup(bot):
    bot.add_cog(Simple(bot))
