import logging
import os
import traceback
from datetime import datetime
from pathlib import Path
from sys import stdout

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
if os.getenv("SAVE_LOG_TO_FILE"):
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
console = logging.StreamHandler(stdout)
console.setFormatter(formatter)
logger.addHandler(console)

description = """
An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.
"""
start_time = datetime.now()
invocation = os.getenv("INVOCATION") or "?"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot(
    command_prefix=commands.when_mentioned_or(invocation), 
    description=description, 
    intents=intents)
   
for extension_path in Path("./cogs").glob("*.py"):
    extension_name = extension_path.stem
    dotted_path = f"cogs.{extension_name}"
    logger.info(f"loading... {dotted_path}")
    try:
        bot.load_extension(dotted_path)
        logger.info(f"loaded {dotted_path}")
    except Exception as e:
        traceback_msg = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
        logger.info(f"Failed to load cog {dotted_path} - traceback:{traceback_msg}")

bot.run(os.getenv("DISCORD_TOKEN"))
