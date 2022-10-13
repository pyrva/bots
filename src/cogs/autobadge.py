from discord.ext import commands


class AutoBadge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='whos_here', help='Responds with list of people here in mainstage',
        pass_context=True
    )
    async def whos_here(self, ctx):
        channel = self.bot.get_channel(
            691841117775462445
        )  # gets the channel you want to get the list from
        members = channel.members  # finds members connected to the channel

        mem = [member.name for member in members]
        print(mem)  # print info
        await ctx.send(mem)


async def setup(bot):
    await bot.add_cog(AutoBadge(bot))
