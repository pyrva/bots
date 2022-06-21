import builtins
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix='!')

builtins.bot = bot

import bot1
import bot2

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)

#RSB_TODO: look into Cogs:https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html#
