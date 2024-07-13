import discord
from discord.ext import commands
from utils.embeds import user_welcome_embed, user_goodbye_embed
from utils.databasefunctions import get


class memberfunctions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            channelid = await get(self.bot.database,
                                  f""" SELECT configoption FROM server_{str(member.guild.id)} WHERE configname='welcome_channel' """)
            roleid = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(member.guild.id)} WHERE configname='default_role' """)
            if channelid:
                channel = discord.utils.get(member.guild.channels, id=channelid)
                if channel:
                    await channel.send(embed=await user_welcome_embed(member, member.guild))
            if roleid:
                role = discord.utils.get(member.guild.roles, id=roleid)
                if role:
                    await member.add_roles(role)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channelid = await get(self.bot.database,
                              f""" SELECT configoption FROM server_{str(member.guild.id)} WHERE configname='goodbye_channel' """)
        channel = discord.utils.get(member.guild.channels, id=channelid)
        if channel:
            await channel.send(embed=await user_goodbye_embed(member, member.guild))


async def setup(bot):
    await bot.add_cog(memberfunctions(bot))
