import discord
from discord.ext import commands
from utils.data import create_dirs


class onready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            await self.bot.wait_until_ready()
            await create_dirs(self.bot.guilds)
            print(f'We have logged in as {self.bot.user}')
        except Exception as e:
            print(f"On Ready: {e}")


async def setup(bot):
    await bot.add_cog(onready(bot))
