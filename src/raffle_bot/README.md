# Raffle Bot

When PyRVA has something to raffle off.
This bot monitors all channels and tracks who wants to enter the raffle.

## Entering a Raffle

To enter the raffle, members have to enter `enter` in any text channel.

Admins are not eligible to win, so their submissions are ignored.
Submissions are stored in a set to prevent duplicate entries.

## Admin Controls

- To select a winner, an admin can type `end`. A winner is selected, their submission is removed from the list, and their victory is announced.

- `list` shows a list of everyone in the set

- `reset` scraps the current set and starts fresh

## Running the Bot

You must have access to the bot's authentication token.
The bot runs locally on a machine and must be spun up for meetings.

Python 3.9 does not quite work due to the async, so this bot runs on Python 3.8.
To run the bot, type

```
python raffle_bot.py
```
