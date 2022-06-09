from builtins import bot

from discord.ext import commands


@bot.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    await ctx.send("pong")
