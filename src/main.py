import logging
import os
import traceback
from datetime import datetime
from pathlib import Path
from sys import stdout

import discord
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger('discord')
if os.getenv("DEBUG") == 'True':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
if os.getenv("SAVE_LOG_TO_FILE") == 'True':
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

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Bot(
    description=description, 
    intents=intents)

for extension_path in Path("./cogs").glob("*.py"):
    extension_name = extension_path.stem
    dotted_path = f"cogs.{extension_name}"
    logger.info(f"loading... {dotted_path}")
    try:
        bot.load_extension(str(dotted_path))  
    except Exception as e:
        traceback_msg = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
        logger.info(f"Failed to load cog {dotted_path} - traceback:{traceback_msg}")
    logger.info(f"loaded {dotted_path}")

@bot.command()
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond('pong!')

@bot.event
async def on_connect():
    bot_activity = discord.Game(str(os.getenv("STATUS_MESSAGE")))
    await bot.change_presence(status=discord.Status.online,
                            activity=bot_activity)
    logger.info("On_connect complete.....")

@bot.event
async def on_ready():
    logger.info(f"version: {discord.__version__}")
    logger.info(f"Successfully logged in as {bot.user}/ ID: {bot.user.id}")
    logger.info(f"Started at: {start_time}")

@bot.listen('on_interaction')
async def log_interaction(interaction):
    if interaction is not None:
        logger.info(f'requester: {str(interaction.user)}')
        logger.info(f'Command: {str(interaction.data)}')

@bot.listen('on_message')
async def log_message(message):
    if message.interaction is not None:
        logger.info(f'response: {str(message.content)}')
        logger.info(f'url: {str(message.jump_url)}')


bot.run(os.getenv("DISCORD_TOKEN"))
