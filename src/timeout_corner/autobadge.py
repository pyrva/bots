import discord
import os

from discord.commands import SlashCommandGroup
from discord.ext import commands


class autobadge(commands.Cog):
    autobadge = SlashCommandGroup(
        "autobadge", "commands and tasks for automatically assign badges to users"
    )

    def __init__(self, bot):
        self.bot = bot

    @autobadge.command()
    @discord.default_permissions(
        administrator=True,
    )  # Only members with this permission can use this command.
    @commands.command(
        name="whos_here",
        help="Responds with list of people here in mainstage",
        pass_context=True,
    )
    async def whos_here(self, ctx):
        channel = self.bot.get_channel(os.getenv("event_channel"))

        members = channel.members

        mem = []  # (list)
        for member in members:
            mem.append(member.name)

        print(mem)  # print info
        await ctx.send(mem)


def setup(bot):
    bot.add_cog(autobadge(bot))
