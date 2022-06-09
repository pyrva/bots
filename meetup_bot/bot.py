import os

from discord.ext import commands, tasks
from dotenv import load_dotenv

import meetup_rest_api as mra

load_dotenv()
# token = os.environ.get("api-token")

target_channel_id = int(os.getenv("meetupbot_target_channel_id"))
bot = commands.Bot("!")

@tasks.loop(seconds=int(os.getenv("meetupbot_loop_interval")))  # change this to the interval you want to update
async def update_announcements():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    update = mra._get_upcoming()

    if update != "No New Updates":
        await message_channel.send(update)
    else:
        pass


@update_announcements.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

update_announcements.start()

# create .env file => Secret_Token = "Enter your token here"
bot.run(os.getenv("DISCORD_TOKEN"))
