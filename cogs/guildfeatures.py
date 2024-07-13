from aiomysql import Error
from discord.ext import commands
from utils.data import assemble_data
from utils.databasefunctions import drop_server


class guildfunctions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await assemble_data(self.bot.database, guild.id)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            await drop_server(self.bot.database, f"""DROP TABLE server_{str(guild.id)};""")
        except Exception or Error as e:
            print(f"Drop Server: {e}")


async def setup(bot):
    await bot.add_cog(guildfunctions(bot))
