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
        super().__init__(*args, command_prefix=os.getenv('invocation'), **kwargs)
        self.start_time = datetime.now()


    async def on_connect(self):
        logger.info("On_connect complete.....")

    def get_cog(self, name):
        # this is really hacky and is probably a sin, could break something
        return super().get_cog(name.capitalize())

    async def on_ready(self):
        logger.info(f"discord.py version: {discord.__version__}")
        logger.info(f"Successfully logged in as {self.user}   ID: {self.user.id}")
        logger.info(f"Started at: {self.start_time} / invocation set as: {os.getenv('invocation')}")

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

    async def scheduled_presence_update(self):
        await self.wait_until_ready()
        while not self.is_closed():
            await asyncio.sleep(60 * 60)  # 60 minutes
