"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
from __future__ import annotations
from discord import app_commands, Interaction
from discord.ext import commands

class MathCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='add', description="Adds two numbers together.")
    async def add(self, interaction: Interaction, a: int, b: int):
        """Adds two numbers and returns the result"""
        result = a + b
        await interaction.response.send_message(f'The sum of {a} and {b} is {result}'.format(a, b))

async def setup(bot: commands.Bot):
    await bot.add_cog(MathCommands(bot))
