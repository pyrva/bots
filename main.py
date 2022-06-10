import builtins
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix='!')

builtins.bot = bot

import simple_commands.bot
import autobadge_bot.bot
import raffle_bot.bot_refactored

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
