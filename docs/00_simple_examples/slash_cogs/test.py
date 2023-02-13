# This example requires the 'members' privileged intent to use the Member converter.
import os

import discord
from dotenv import load_dotenv
from discord.commands import SlashCommandGroup

load_dotenv()


intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)
# The debug guilds parameter can be used to restrict slash command registration to only the supplied guild IDs.
# This is done like so: discord.Bot(debug_guilds=[...])
# Without this, all commands are made global unless they have a guild_ids parameter in the command decorator.

# Note: If you want you can use commands.Bot instead of discord.Bot.
# Use discord.Bot if you don't want prefixed message commands.

# With discord.Bot you can use @bot.command as an alias
# of @bot.slash_command but this is overridden by commands.Bot.


@bot.slash_command()  # Create a slash command
async def hello(ctx: discord.ApplicationContext):
    """Say hello to the bot"""  # The command description can be supplied as the docstring
    await ctx.respond(f"Hello {ctx.author}!")
    # Note: interactions must be responded to within 3 seconds, if they're not, an
    # "Unknown interaction" error will be raised, you can circumvent this by using "ctx.defer()".
    # Additional note: You cannot respond to the same interaction twice!


@bot.slash_command(name="hi")
async def global_command(
    ctx: discord.ApplicationContext, num: int
):  # Takes one integer parameter
    await ctx.respond(f"This is a global command, {num}!")


@bot.slash_command()
@discord.default_permissions(
    administrator=True,
)  # Only members with this permission can use this command.
async def admin_only(ctx: discord.ApplicationContext):
    await ctx.respond(f"Hello {ctx.author}, you are an administrator.")


util = SlashCommandGroup("util", "utility commands")


@util.command()
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("pong!")


# To learn how to add descriptions and choices to options, check slash_options.py
bot.run(os.getenv("DISCORD_TOKEN"))
