import os
import random

from dotenv import load_dotenv
import discord
load_dotenv()


client = discord.Client()
submissions = set()
entry_keys = [
    'pick me',
    'select me',
]
selection_keys = [
    'pick winner',
    'select winner',
]


def response(msg: str, author: str, admin: bool) -> str:
    """Determine appropriate action to take.

    msg: text of incomming message from discord
    author: the name of the user sending the message
    admin: is the user sending the message an admin
    """
    if not admin and any([key in msg.lower() for key in entry_keys]):
        if author in submissions:
            return f'No worries, {author}, we already got you 😉'
        else:
            submissions.add(author)
            return f'Good Luck, {author}!'

    if admin and any([key in msg.lower() for key in selection_keys]):
        if submissions:
            winner = random.choice(list(submissions))
            submissions.remove(winner)
            return f'Congratulations {winner}! 🎉'
        else:
            return 'Looks like there is nobody to win'


@client.event
async def on_ready():
    print(f'raffle-bot is online!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = response(
        msg=message.content,
        author=str(message.author).split("#")[0],
        admin=message.author.guild_permissions.administrator,
    )
    print(msg)
    await message.channel.send(msg)


if __name__ == '__main__':
    client.run(os.getenv('RAFFLE_BOT_TOKEN'))
