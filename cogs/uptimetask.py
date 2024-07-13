import discord
from discord.ext import commands, tasks


class uptimetask(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.wait_until_ready()
        if not self.status_message.is_running():
            self.status_message.start()

    @tasks.loop(minutes=60)
    async def status_message(self):
        try:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                     name=f" bugs 🦟"))
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(uptimetask(bot))
