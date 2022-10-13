from pathlib import Path

from discord import Intents
import pytest

from bot import Bot
from main import load_cogs


@pytest.mark.asyncio
async def test_bot_can_load_our_cogs():
    cogs = [
        f'cogs.{x.stem}'
        for x in Path('cogs').glob('*.py')
    ]
    assert 'cogs.raffle' in cogs, 'Raffle cog not found. Please update test.'
    bot = Bot(case_insensitive=True, intents=Intents.all())
    await load_cogs(bot, *cogs)
    assert 'raffle' in bot.cogs
