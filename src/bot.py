import asyncio
import logging
import os
import traceback
from datetime import datetime

import discord
from discord.ext import commands

import constants

logger = logging.getLogger(__name__)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, command_prefix=os.getenv('INVOCATION'), **kwargs)
        self.start_time = datetime.now()


    async def on_connect(self):
        # status automatically set to online if env does not exist
        status = os.getenv("STATUS") or 'online'
        stats_message = "!help"
        await self.change_presence(status=status,
                                   activity=discord.Activity(name=stats_message,
                                                             type=discord.ActivityType.playing))
        logger.info("On_connect complete.....")

    async def process_commands(self, message):
        if message.author.bot:
            return

        ctx = await self.get_context(message)
        if ctx.command is not None:
            logger.info(f'requester: {str(ctx.message.author).split("#")[0]} / message: {ctx.message.content}' )

        await self.invoke(ctx)

    def get_cog(self, name):
        # this is really hacky and is probably a sin, could break something
        return super().get_cog(name.capitalize())

    async def on_ready(self):
        logger.info(f"discord.py version: {discord.__version__}")
        logger.info(f"Successfully logged in as {self.user}   ID: {self.user.id}")
        logger.info(f"Started at: {self.start_time} / invocation set as: {self.command_prefix}")

    async def on_error(self, event, *args):
        msg = f"{event} event error exception!\n{traceback.format_exc()}"
        logger.critical(msg)
    #     await self.log_error(msg) # this is for seeing the error printed in the discord channel. not the best imo.

    # async def log_error(self, message):
    #     if not self.is_ready() or self.is_closed():
    #         return

    #     error_log_channel = self.get_channel(constants.error_log_channel_id)

    #     num_messages = 1 + len(message) // 1981
    #     split_messages = (message[i : i + 1980] for i in range(0, len(message), 1980))
    #     for count, message in enumerate(split_messages, 1):
    #         await error_log_channel.send(f"```Num {count}/{num_messages}:\n{message}```")
