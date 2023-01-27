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

    @autobadge.command(
        name="whos_here",
        help="Responds with list of people here in mainstage",
        pass_context=True,
    )
    @discord.default_permissions(
        administrator=True,
    )  # Only members with this permission can use this command.
    async def whos_here(self, ctx):
        channel = self.bot.get_channel(os.getenv("event_channel"))

        members = channel.members

        mem = []  # (list)
        for member in members:
            mem.append(member.name)

        print(mem)  # print info
        await ctx.send(mem)

    # TODO: Setup a trigger to start monitoring a VC. Cache the users that enter the VC.
    # When admin closes the meeting they trigger the automation of badging everyone in the cache
    #


def setup(bot):
    bot.add_cog(autobadge(bot))
