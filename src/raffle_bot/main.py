# bot.py
import json
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=os.getenv('invocation'))

submissions = set()

def response(msg: str, author: str, admin: bool) -> str:
    """Determine appropriate action to take.

    msg: text of incomming message from discord
    author: the name of the user sending the message
    admin: is the user sending the message an admin
    """

    if admin:
        if msg.lower() == 'end':
            if submissions:
                winner = random.choice(list(submissions))
                submissions.remove(winner)
                return f'Congratulations {winner}! 🎉'
            else:
                return 'Looks like there is nobody to win'
        elif msg.lower() == 'enter':
            return "Admins can't enter the raffle. Thems the rules."
        elif msg.lower() == 'list':
            return submissions
        elif msg.lower() == 'reset':
            submissions.clear()
            return "raffle reset"
    else:
        if msg.lower() == 'enter':
            if author in submissions:
                return f'No worries, {author}, we already got you 😉'
            else:
                submissions.add(author)
                return f'Good Luck, {author}!'
        else:
            return "trying typing => !raffle enter"
    
    return 'something went wrong... does your command exist?'

@bot.command(name='raffle', help='Raffle bot for pyrva raffle. Commands: enter, end, list, reset.', pass_context=True)
async def raffle(ctx, command: str):

    if any( x in os.getenv('ADMIN_ROLES') for x in [role.name for role in ctx.message.author.roles]):
        _is_admin = True
    else:
        _is_admin = False

    print('--- RAFFLE BOT ---')
    print(f'command {command}')
    print(f'author {str(ctx.message.author).split("#")[0]}')
    print(f'admin {_is_admin}')
    
    msg = response(
        msg=command,
        author=str(ctx.message.author).split("#")[0],
        admin=_is_admin,
    )

    print(f'result {msg}')
    print('------------------')
    await ctx.send(msg)


bot.run(TOKEN)

