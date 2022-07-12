import json
import os

import requests as r
from discord.ext import commands, tasks
from dotenv import load_dotenv


def _url(path):
    return "https://api.meetup.com/PyRVAUserGroup/" + path

def _get_next():
    response = r.get(_url("events"))
    event_list = response.json()
    x = event_list[0]
    event_info = f"Event: {x['name']} \
                    \nDate: {x['local_date']} Time: {x['local_time']} EST \
                    \nLink: {x['link']}"
    return event_info

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = commands.Bot(command_prefix='!')
else:
    from builtins import bot

################################################################################################
#   Tasks on a loop is something I am shelving until someone pokes me to deal with it. -RSB    #
################################################################################################

# target_channel_id = int(os.getenv("target_channel_id"))

# @tasks.loop(seconds=int(os.getenv("meetupbot_loop_interval")))  # change this to the interval you want to update
# async def update_announcements():
#     message_channel = bot.get_channel(target_channel_id)
#     print(f"Got channel {message_channel}")
#     update = mra._get_upcoming()

#     if update != "No New Updates":
#         await message_channel.send(update)
#     else:
#         pass

# @update_announcements.before_loop
# async def before():
#     await bot.wait_until_ready()
#     print("Finished waiting")

# update_announcements.start()

@bot.command(name='next_meetup', help='whens the next meetup?', pass_context=True)
async def next_meetup(ctx):
    response = _get_next()
    print(response) #RSB-TODO need to look into setting up proper logging instead of this ad-hoc non-sense
    await ctx.send(response)

if __name__ == "__main__":
    bot.run(TOKEN)
