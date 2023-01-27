import logging

import discord
import requests
from discord import option
from discord.commands import SlashCommandGroup
from discord.ext import commands

logger = logging.getLogger(__name__)


class utilities(commands.Cog):
    util = SlashCommandGroup("util", "utility commands")

    def __init__(self, bot):
        self.bot = bot

    @util.command()
    @discord.default_permissions(
        administrator=True,
    )  # Only members with this permission can use this command.
    async def admin_only(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"Hello {ctx.author}, you are an administrator.")

    def latency_check(self):  # Alias for the Z.ping command
        return discord.Embed(
            title="Pong.",
            description=f"Bot's current ping is **{round(self.bot.latency * 1000)}ms**",
            color=discord.Color.green(),
        )

    @util.command(name="latency", help="measures the latency of the bot")
    async def latency(self, ctx: discord.ApplicationContext):
        await ctx.respond(embed=self.latency_check())

    @util.command(name="google", help="creates a lmgtfy link")
    async def google(self, ctx, *, args):
        await ctx.respond(
            f"Here, allow me to google that one for you:\nhttps://letmegooglethat.com/?q={args.replace(' ', '+')}"
        )  # ,reference=ctx.message

    @util.command(help="searches for pip package")
    @option(
        name="package",
        input_type=str,
        description="what package do you want to search for",
        required=True,
    )
    async def pipsearch(self, ctx: discord.ApplicationContext, package: str):
        if not package:
            await ctx.respond(
                embed=discord.Embed(
                    title='Traceback (most recent call): "~/ur_brain"',
                    description="Invalid pacakge name!",
                    colour=discord.Colour.red(),
                )
            )
        else:
            data = requests.get(f"https://pypi.org/pypi/{package}/json").json()

            embed = discord.Embed(
                title=f"Searched {package}",
                description=f"[Project URL]({data['info']['package_url']})",
                colour=discord.Colour.green(),
            )

            embed.add_field(
                name=f"{data['info']['name']}-{data['info']['version']}",
                value=f"{data['info']['summary']}",
            )
            await ctx.respond(embed=embed)

    @util.command(help="returns embed of github repo")
    @option(
        name="endpoint",
        input_type=str,
        description="what repo do you want to search for",
        required=True,
    )
    async def github(self, ctx: discord.ApplicationContext, endpoint: str):
        try:
            info = requests.get(f"https://api.github.com/repos/{endpoint}").json()
            contrib_info = requests.get(
                f"https://api.github.com/repos/{endpoint}/contributors"
            ).json()
            embed = discord.Embed(
                title=info["name"],
                description=f"[Repository Link]({info['html_url']})",
                colour=discord.Colour.green(),
            )

            embed.add_field(name="Owner", value=info["owner"]["login"])
            embed.add_field(name="Language", value=info["language"])
            embed.add_field(name="Stars", value=info["stargazers_count"])
            embed.add_field(name="Forks", value=info["forks"])
            embed.add_field(
                name="License",
                value=info["license"]["name"]
                if info["license"] is not None
                else "None",
            )
            embed.add_field(name="Open Issues", value=info["open_issues"])
            embed.add_field(
                name="Contributors",
                value="\n".join([contribs["login"] for contribs in contrib_info]),
            )
            embed.set_thumbnail(url=info["owner"]["avatar_url"])
        except ValueError:
            embed = discord.Embed(
                title="Oops",
                description="Repository does not exist.",
                colour=discord.Colour.red(),
            )

        await ctx.respond(embed=embed)

    @util.command(name="userinfo", description="Gets info about a user.")
    async def user_info(
        self, ctx: discord.ApplicationContext, user: discord.Member = None
    ):
        user = (
            user or ctx.author
        )  # If no user is provided it'll use the author of the message
        embed = discord.Embed(
            fields=[
                discord.EmbedField(
                    name="ID", value=str(user.id), inline=False
                ),  # User ID
                discord.EmbedField(
                    name="Created",
                    value=discord.utils.format_dt(user.created_at, "F"),
                    inline=False,
                ),  # When the user's account was created
            ],
        )
        embed.set_author(name=user.name)
        embed.set_thumbnail(url=user.display_avatar.url)

        if user.colour.value:  # If user has a role with a color
            embed.colour = user.colour

        if isinstance(user, discord.User):  # Checks if the user in the server
            embed.set_footer(text="This user is not in this server.")
        else:  # We end up here if the user is a discord.Member object
            embed.add_field(
                name="Joined",
                value=discord.utils.format_dt(user.joined_at, "F"),
                inline=False,
            )  # When the user joined the server

        await ctx.respond(embeds=[embed])  # Sends the embed

    @util.command(name="suggestion", description="facilitates making a suggestion")
    @option(
        name="suggestion",
        description="This is the suggestion you are asking feedback for",
        required=True,
    )
    async def suggest(self, ctx: discord.ApplicationContext, suggestion: str):
        logger.info(f"function: suggest / requester: {str(ctx.author)}")
        print(suggestion)
        embed = discord.Embed(description=suggestion)
        embed.set_author(name=f"Suggestion by {ctx.author.name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

def setup(bot):
    bot.add_cog(utilities(bot))
