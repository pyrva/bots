import logging
import os
import traceback
from pathlib import Path
from sys import stdout

from discord import Intents
from dotenv import load_dotenv

import constants
from bot import Bot

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
console = logging.StreamHandler(stdout)
console.setFormatter(formatter)
root_logger.addHandler(console)

root_logger.info(f"Running as main bot.")


if __name__ == "__main__":
    load_dotenv()
    bot = Bot(case_insensitive=True, intents=Intents.all())
    for extension_path in Path("./cogs").glob("*.py"):
        extension_name = extension_path.stem
        if extension_name in constants.ignored_extensions:
            continue

        dotted_path = f"cogs.{extension_name}"
        try:
            bot.load_extension(dotted_path)
            root_logger.info(f"loaded {dotted_path}")
        except Exception as e:
            traceback_msg = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
            root_logger.info(f"Failed to load cog {dotted_path} - traceback:{traceback_msg}")

    bot.run(os.getenv("DISCORD_TOKEN"))
