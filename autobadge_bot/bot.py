# bot.py
import os

if __name__ == "__main__":
    from discord.ext import commands
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = commands.Bot(command_prefix='!')
else:
    from builtins import bot
    
@bot.command(name='whos_here', help='Responds with list of people here in mainstage', pass_context=True)
async def whos_here(ctx):
    channel = bot.get_channel(691841117775462445) #gets the channel you want to get the list from

    members = channel.members #finds members connected to the channel

    mem = [] #(list)
    for member in members:
        mem.append(member.name)

    print(mem) #print info
    await ctx.send(mem)

if __name__ == "__main__":
    bot.run(TOKEN)
