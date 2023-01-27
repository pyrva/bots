# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command(name="99", help="Responds with a random quote from Brooklyn 99")
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "I'm the human form of the 💯 emoji.",
        "Bingpot!",
        (
            "Cool. Cool cool cool cool cool cool cool, "
            "no doubt no doubt no doubt no doubt."
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name="roles", help="testing return role")
async def roles(ctx):
    print(ctx.message.author)
    print(ctx.message.author.roles)

    if any(
        x in os.getenv("ADMIN_ROLES")
        for x in [role.name for role in ctx.message.author.roles]
    ):
        response = "Admin True"
    else:
        response = "Admin False"

    await ctx.send(response)


if __name__ == "__main__":
    bot.run(TOKEN)
