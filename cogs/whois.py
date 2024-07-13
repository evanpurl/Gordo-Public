import discord
from discord import app_commands
from discord.ext import commands

from utils.databasefunctions import insert


class whoiscmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="who-is", description="Command to learn about Gordo.")
    async def whois(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content=f"""Hello! *croak* <:Gordo:1185828693495525408> I'm Gordo, a hoppy little frog bot made by my best friend Purls.

I'm trying my best to help people maintain their servers with many useful features.

I am hosted by Wyvern Hosting. They are pretty swell people. *Happy ribbit*

- Advanced Logging: Several different events on your server can be logged (if enabled) to help you moderate your server!
- Community Features: I can send welcome and goodbye messages into a channel of your choice! I can also add your members to a role when they join!

Check the commands under the /gordo-config command to see what needs to be configured!
Check /gordo-options for options to enable or disable""",
            ephemeral=True)


async def setup(bot):
    await bot.add_cog(whoiscmd(bot))
