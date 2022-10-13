# bot.py
import logging
import os
import random

from discord.ext import commands

logger = logging.getLogger(__name__)


class Raffle(commands.Cog):
    def __init__(self, bot):
        self.submissions = set()

    @commands.command(
        name='raffle',
        help='Raffle bot for pyrva raffle. Commands: enter, end, list, reset.',
        pass_context=True
    )
    async def raffle(self, ctx, command: str):
        _is_admin = any(
            x in os.getenv('ADMIN_ROLES') for x in
            [role.name for role in ctx.message.author.roles]
        )

        logger_message = f'Is author admin: {_is_admin}'
        logger.info(logger_message)
        msg = self.response(
            msg=command, author=str(ctx.message.author).split("#")[0],
            admin=_is_admin
        )

        logger.info(f'result {msg}')
        await ctx.send(msg)

    def response(self, msg: str, author: str, admin: bool) -> str:
        """Determine appropriate action to take.

        msg: text of incomming message from discord
        author: the name of the user sending the message
        admin: is the user sending the message an admin
        """
        if admin:
            if msg.lower() == 'end':
                if not self.submissions:
                    return 'Looks like there is nobody to win'
                winner = random.choice(list(self.submissions))
                self.submissions.remove(winner)
                return f'Congratulations {winner}! 🎉'
            elif msg.lower() == 'enter':
                return "Admins can't enter the raffle. Thems the rules."
            elif msg.lower() == 'list':
                return self.submissions
            elif msg.lower() == 'reset':
                self.submissions.clear()
                return "raffle reset"
        elif msg.lower() == 'enter':
            if author in self.submissions:
                return f'No worries, {author}, we already got you 😉'
            self.submissions.add(author)
            return f'Good Luck, {author}!'
        else:
            return "trying typing => !raffle enter"
        return 'something went wrong... does your command exist?'


async def setup(bot):
    await bot.add_cog(Raffle(bot))
