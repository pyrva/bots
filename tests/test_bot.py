import discord
from discord import Intents
from discord.app_commands import commands
from discord.ext.commands import Cog
import pytest

from bot import Bot
from main import load_cogs


@pytest.mark.asyncio
async def test_bot_can_load_a_sample_cog():
    bot = Bot(case_insensitive=True, intents=Intents.all())
    await load_cogs(bot, SampleBot(bot))
    assert 'SampleBot' in bot.cogs


class SampleBot(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member
