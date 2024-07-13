import discord
from discord import app_commands
from discord.ext import commands
from utils.timeutils import timetounix


class accagefunction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="accage", description="Determines account age")
    async def accage(self, interaction: discord.Interaction, user: discord.User):
        try:
            await interaction.response.send_message(content=await timetounix(user.created_at), ephemeral=True)

        except Exception as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)


async def setup(bot):
    await bot.add_cog(accagefunction(bot))
