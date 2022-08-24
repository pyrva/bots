import logging
import os

import discord
import requests
from discord.ext import commands

logger = logging.getLogger(__name__)

class utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def ping_pong(self, ctx, bot): # Alias for the Z.ping command
        return(discord.Embed(
            title="Pong.",
            description=f"Bot's current ping is **{round(bot.latency * 1000)}ms**",
            timestamp=ctx.message.created_at,
            color=discord.Color.green()))
    
    @commands.command(name='ping', help='measures the latency of the bot', pass_context=True)
    async def ping(self, ctx):
        logger.info(f'function: google / requester: {str(ctx.message.author).split("#")[0]}')
        await ctx.send(embed=self.ping_pong(ctx, self.bot))

    @commands.command(name='google', help='creates a lmgtfy link', pass_context=True)
    async def google(self, ctx, *, args):
        logger.info(f'function: google / requester: {str(ctx.message.author).split("#")[0]}')

        await ctx.send(f"Here, allow me to google that one for you:\nhttps://letmegooglethat.com/?q={args.replace(' ', '+')}") #,reference=ctx.message
    
    @commands.command(aliases=["pip", "pypi"], help='searches for pip package', pass_context=True)
    async def pipsearch(self,ctx):
        logger.info(f'function: google / requester: {str(ctx.message.author).split("#")[0]}')
        package = ctx.message.content.split(" ")[-1]
        
        if not package:
            await ctx.send(embed=discord.Embed(title="Traceback (most recent call): \"~/ur_brain\"", description="Invalid pacakge name!", colour=discord.Colour.red()))
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
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["git"], help='returns embed of github repo')
    async def github(self, ctx, endpoint):
        logger.info(f'function: git / requester: {str(ctx.message.author).split("#")[0]}')

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

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(utilities(bot))
