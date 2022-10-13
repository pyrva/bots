import os
import logging
import traceback
from pathlib import Path
from sys import stdout

from discord import Intents
from discord.ext.commands import Cog
from dotenv import load_dotenv

import constants
from bot import Bot

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
console = logging.StreamHandler(stdout)
console.setFormatter(formatter)
root_logger.addHandler(console)

root_logger.info("Running as main bot.")


async def load_cogs(bot: Bot, *cogs: str | Cog):
    for cog_module in cogs:
        try:
            await bot.load_extension(cog_module)
            root_logger.info(f'loaded {cog_module}')
        except Exception as e:
            traceback_msg = traceback.format_exception(
                type(e), value=e, tb=e.__traceback__
            )
            root_logger.info(
                f'Failed to load cog {cog_module} - traceback:{traceback_msg}'
            )
            raise e


if __name__ == '__main__':
    load_dotenv()
    bot = Bot(case_insensitive=True, intents=Intents.all())
    cogs = [
        f'cogs.{x.stem}'
        for x in Path(__file__, 'cogs').glob('*.py')
        if x.stem not in constants.IGNORED_EXTENSIONS
    ]
    load_cogs(bot, *cogs)

    bot.run(os.getenv('DISCORD_TOKEN'))


