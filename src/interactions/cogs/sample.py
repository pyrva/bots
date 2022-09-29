import random
import interactions

class Ext(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="command_in_ext",
        description="This command is in an Extension",
    )
    async def _ext_command(self, ctx: interactions.CommandContext):
        await ctx.send("This command is ran inside an Extension")

    @interactions.extension_command(
      name='roll_dice', 
      description='Simulates rolling dice. Format: /roll_dice {num_of_dice} {num_of_sides} Example: !roll_dice 2 6',
      options = [
            interactions.Option(
                name="number_of_dice",
                description="number of dice",
                type=interactions.OptionType.INTEGER,
                required=True,
            ),
            interactions.Option(
                name="number_of_sides",
                description="number of sides",
                type=interactions.OptionType.INTEGER,
                required=True,
            ),
        ])
    async def roll(self, ctx: interactions.CommandContext, number_of_dice: int, number_of_sides: int):
      dice = [
          str(random.choice(range(1, number_of_sides + 1)))
          for _ in range(number_of_dice)
      ]
      await ctx.send(', '.join(dice))

def setup(client):
    Ext(client)
