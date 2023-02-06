# bot.py
import logging
import os
import random

import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands

logger = logging.getLogger(__name__)


class raffle(commands.Cog):
    raffle = SlashCommandGroup("raffle", "Manages the raffle")

    def __init__(self, bot):
        self.submissions = set()

    @raffle.command(name="enter", help="enter the raffle")
    async def raffle_enter(self, ctx):
        if any(
            x in os.getenv("ADMIN_ROLES")
            for x in [role.name for role in ctx.author.roles]
        ):
            _is_admin = True
        else:
            _is_admin = False

        msg = self.response(
            msg="enter",
            author=str(ctx.author).split("#")[0],
            admin=_is_admin,
        )
        await ctx.respond(msg)

    @raffle.command(name="select", help="ADMIN ONLY ~ selects a winner from the list")
    @discord.default_permissions(
        administrator=True,
    )  # Only members with this permission can use this command.
    async def raffle_select_winner(self, ctx):
        msg = self.response(
            msg="select",
            author=str(ctx.author).split("#")[0],
            admin=True,
        )
        await ctx.respond(msg)

    @raffle.command(
        name="list", help="ADMIN ONLY ~ lists the participants in the raffle"
    )
    @discord.default_permissions(
        administrator=True,
    )  # Only members with this permission can use this command.
    async def raffle_list(self, ctx):
        msg = self.response(
            msg="list",
            author=str(ctx.author).split("#")[0],
            admin=True,
        )
        await ctx.respond(msg)

    @raffle.command(name="reset", help="ADMIN ONLY ~ resets the list of participants")
    @discord.default_permissions(
        administrator=True,
    )  # Only members with this permission can use this command.
    async def raffle_reset(self, ctx):
        msg = self.response(
            msg="reset",
            author=str(ctx.author).split("#")[0],
            admin=True,
        )
        await ctx.respond(msg)

    def response(self, msg: str, author: str, admin: bool) -> str:
        """Determine appropriate action to take.

        msg: text of incomming message from discord
        author: the name of the user sending the message
        admin: is the user sending the message an admin
        """

        if admin:
            if msg.lower() == "select":
                if self.submissions:
                    winner = random.choice(list(self.submissions))
                    self.submissions.remove(winner)
                    return f"Congratulations {winner}! 🎉"
                else:
                    return "Looks like there is nobody to win"
            elif msg.lower() == "enter":
                return "Admins can't enter the raffle. Thems the rules."
            elif msg.lower() == "list":
                return str(self.submissions)
            elif msg.lower() == "reset":
                self.submissions.clear()
                return "raffle reset"
        else:
            if msg.lower() == "enter":
                if author in self.submissions:
                    return f"No worries, {author}, we already got you 😉"
                else:
                    self.submissions.add(author)
                    return f"Good Luck, {author}!"
            else:
                return "trying typing => !raffle enter"

        return "something went wrong... does your command exist?"


def setup(bot):
    bot.add_cog(raffle(bot))
