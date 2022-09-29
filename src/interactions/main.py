import logging
import os
import traceback
from pathlib import Path
from sys import stdout

from dotenv import load_dotenv

import interactions

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
console = logging.StreamHandler(stdout)
console.setFormatter(formatter)
root_logger.addHandler(console)

root_logger.info(f"Running as main bot.")

load_dotenv()
if __name__ == "__main__":

    bot = interactions.Client(token=os.getenv("DISCORD_TOKEN"))

    @bot.command(
        name="say_something",
        description="say something!",
        options = [
            interactions.Option(
                name="text",
                description="What you want to say",
                type=interactions.OptionType.STRING,
                required=True,
            ),
        ],
    )
    async def my_first_command(ctx: interactions.CommandContext, text: str):
        await ctx.send(f"You said '{text}'!")

    for extension_path in Path("./cogs").glob("*.py"):
        extension_name = extension_path.stem
        dotted_path = f"cogs.{extension_name}"
        root_logger.info(f"attempting to load {dotted_path}")

        try:
            bot.load(dotted_path)
            root_logger.info(f"loaded {dotted_path}")
        except Exception as e:
            traceback_msg = traceback.format_exception()
            root_logger.info(f"Failed to load cog {dotted_path} - traceback:{traceback_msg}")


    bot.start()
