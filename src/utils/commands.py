"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
from discord import app_commands, Interaction
from discord.ext import commands

class MathCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """
        PEMDAS Math Commands included with 
        two number input by user for now.
    """

    # Simple Math Addiction
    # two inputs
    @app_commands.command(name='add', description="Adds two numbers together.", nsfw=False)
    async def add(self, interaction: Interaction, num1: float, num2: float) -> float:
        
        """Adds two numbers and returns the result"""
        result = num1 + num2
        await interaction.response.send_message(f'The sum of || {num1} + {num2} = {result}'.format(num1, num2))

    # TODO: 
    # Simple Math Subraction
    # Two Inputs
    @app_commands.command(name='subtract', description="Subtract two numbers together", nsfw=False)
    async def subtract(self, interaction: Interaction, num1: float, num2: float) -> float:
        
        """Subtracts two numbers and return the result"""
        result = num1 - num2
        await interaction.response.send_message(f'The sub of || {num1} - {num2} = {result}'.format(num1, num2))
    
    # TODO: 
    # Simple Math Multiplications
    # Two Inputs
    @app_commands.command(name='multi', description="Multis two numbers together", nsfw=False)
    async def multi(self, interaction: Interaction, num1: float, num2: float) -> float:

        """Multis two numbers and return the result"""
        result = num1 * num2
        await interaction.response.send_message(f'The multi of || {num1} * {num2} = {result}'.format(num1, num2))

    # TODO: 
    # Simple Math Division
    # Two Inputs
    @app_commands.command(name='division', description="Divs two numbers together", nsfw=False)
    async def div(self, interaction: Interaction, num1: float, num2: float) -> float:

        """Divs two number and return the result"""
        result = num1 / num2
        await interaction.response.send_message(f'The Div of || {num1} / {num2} = {result}'.format(num1, num2))

async def setup(bot: commands.Bot):
    await bot.add_cog(MathCommands(bot))
