import discord
import requests
from discord.commands import SlashCommandGroup
from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    util = SlashCommandGroup("utilities", "Various utilities for the team")

    def latency_check(self, ctx, bot):
        return(discord.Embed(
            title="latency check",
            description=f"Bot's current ping is **{round(bot.latency * 1000)}ms**",
            timestamp=ctx.message.created_at,
            color=discord.Color.green()))
    
    @util.command(name='latency', help='measures the latency of the bot')
    async def latency(self, ctx):
        await ctx.respond(embed=self.latency_check(ctx, self.bot))

    @util.command(name='google', help='creates a lmgtfy link')
    async def google(self, ctx, *, args):
        await ctx.respond(f"Here, allow me to google that one for you:\nhttps://letmegooglethat.com/?q={args.replace(' ', '+')}")
    
    @util.command(aliases=["pip", "pypi"], help='searches for pip package')
    async def pipsearch(self,ctx):
        package = ctx.message.content.split(" ")[-1]
        
        if not package:
            await ctx.respond(embed=discord.Embed(title="Traceback (most recent call): \"~/ur_brain\"", description="Invalid pacakge name!", colour=discord.Colour.red()))
        else:
            data = requests.get(f"https://pypi.org/pypi/{package}/json").json()
            
            embed=discord.Embed(
                title=f"Searched {package}",
                description=f"[Project URL]({data['info']['package_url']})",
                colour=discord.Colour.green(),
                timestamp=ctx.message.created_at,
            )

            embed.add_field(name=f"{data['info']['name']}-{data['info']['version']}", value=f"{data['info']['summary']}")
            embed.set_footer(text=f"Requested by {ctx.message.author}")
            await ctx.respond(embed=embed)
    
    @util.command(aliases=["git"], help='returns embed of github repo')
    async def github(self, ctx, endpoint):
        try:
            info = requests.get(f"https://api.github.com/repos/{endpoint}").json()
            contrib_info = requests.get(f"https://api.github.com/repos/{endpoint}/contributors").json()
            embed = discord.Embed(
                title=info["name"],
                description=f"[Repository Link]({info['html_url']})",
                colour=discord.Colour.green(),
                timestamp=ctx.message.created_at)
        
            embed.add_field(name="Owner",value=info["owner"]["login"])
            embed.add_field(name="Language",value=info["language"])
            embed.add_field(name="Stars",value=info["stargazers_count"])
            embed.add_field(name="Forks",value=info["forks"])
            embed.add_field(name="License",value=info["license"]["name"] if info["license"] is not None else "None")
            embed.add_field(name="Open Issues",value=info["open_issues"])
            embed.add_field(name="Contributors",value="\n".join([contribs["login"] for contribs in contrib_info]))
            embed.set_thumbnail(url=info["owner"]["avatar_url"])
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        except:
            embed = discord.Embed(
                title="Oops",
                description="Repository does not exist.",
                colour=discord.Colour.red(),
                timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)

        await ctx.respond(embed=embed)
    
    @commands.slash_command(name="userinfo", description="Gets info about a user.")
    async def info(ctx: discord.ApplicationContext, user: discord.Member = None):
        user = user or ctx.author  # If no user is provided it'll use the author of the message
        embed = discord.Embed(
            fields=[
                discord.EmbedField(name="ID", value=str(user.id), inline=False),  # User ID
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

def setup(bot):
    bot.add_cog(Utilities(bot))
