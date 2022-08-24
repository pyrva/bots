import json
import logging
import os

import requests as r
from discord.ext import commands, tasks

logger = logging.getLogger(__name__)


class meetup(commands.Cog):
    def _url(self, path):
        return "https://api.meetup.com/PyRVAUserGroup/" + path

    def _get_next(self):
        response = r.get(self._url("events"))
        event_list = response.json()
        x = event_list[0]
        event_info = f"Event: {x['name']} \
                        \nDate: {x['local_date']} Time: {x['local_time']} EST \
                        \nLink: {x['link']}"
        return event_info

    @commands.command(name='next', help='whens the next meetup?', pass_context=True)
    async def next_meetup(self, ctx):
        response = self._get_next()
        logger.info(f'output\n{response}')
        await ctx.send(response)

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


def setup(bot):
    bot.add_cog(meetup(bot))


