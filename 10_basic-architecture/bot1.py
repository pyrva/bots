from builtins import bot

from discord.ext import commands


@bot.command(pass_context=True)
async def hello(ctx):
    channel = ctx.message.channel
    await ctx.send("hi")

