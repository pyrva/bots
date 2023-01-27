from discord.ext import commands

# from dotenv import load_dotenv
# import os
# import pytest

TOKEN = "bot token of tester bot"
bot = commands.Bot(command_prefix="?/")
target_id = "ID of bot to be tested"
channel_id = "ID of channel of where it will be tested"


@bot.command(
    name="ping"
)  # if name did not entered, function name will be the command name
async def test_ping(ctx):  # Every command takes context object as first parameter
    correct_response = "Pong!"
    channel = await bot.fetch_channel(channel_id)
    await channel.send("ping")

    def check(m):
        return m.content == correct_response and m.author.id == target_id

    response = await bot.wait_for("message", check=check)
    assert response.content == correct_response


bot.run(TOKEN)
