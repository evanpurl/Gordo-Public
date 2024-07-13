import discord
from discord.ext import commands
from aiomysql import Error
from utils.databasefunctions import get
from utils.timeutils import timetounix


class logginglisteners(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            if member.created_at.date() == member.joined_at.date():
                loggingchannel = await get(self.bot.database,
                                           f""" SELECT configoption FROM server_{str(member.guild.id)} WHERE configname='logging_channel' """)
                if loggingchannel:
                    channel = discord.utils.get(member.guild.channels, id=int(loggingchannel))
                    if channel:
                        embed = discord.Embed(
                            title="New Discord Account", color=discord.Color.green())
                        embed.set_author(name=member.name, icon_url=member.display_avatar.url)
                        embed.add_field(name="Creation Date:", value=await timetounix(member.created_at))
                        embed.add_field(name="Join Date:", value=await timetounix(member.joined_at))
                        embed.set_thumbnail(url=member.display_avatar.url)
                        await channel.send(embed=embed)
                    return
                else:
                    return
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        try:
            if message.author.bot:
                return
            option = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(message.guild.id)} WHERE configname='message_logging' """)
            if not int(option):
                return  # message delete feature is disabled
            loggingchannel = await get(self.bot.database,
                                       f""" SELECT configoption FROM server_{str(message.guild.id)} WHERE configname='logging_channel' """)
            if loggingchannel:
                if message.channel.id == loggingchannel:
                    return
                channel = discord.utils.get(message.guild.channels, id=int(loggingchannel))
                if channel:
                    embed = discord.Embed(
                        title="Message Deleted", color=discord.Color.green())
                    embed.set_author(name=message.author.name, icon_url=message.author.avatar)
                    embed.add_field(name="Channel", value=message.channel.mention)
                    embed.add_field(name="Message", value=message.content[:1000])
                    embed.set_thumbnail(url=self.bot.user.avatar)
                    await channel.send(embed=embed)
                return
            else:
                return
        except Exception or Error as e:
            print(f"Message Delete: {e}")

    @commands.Cog.listener()
    async def on_message_edit(self, message_before: discord.Message, message_after: discord.Message):
        try:
            if message_before.author.id == self.bot.user.id:
                return
            if message_before.author.bot:
                return
            if message_before.pinned:
                return
            option = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(message_before.guild.id)} WHERE configname='message_logging' """)
            if not option:
                return  # message edit feature is disabled
            loggingchannel = await get(self.bot.database,
                                       f""" SELECT configoption FROM server_{str(message_before.guild.id)} WHERE configname='logging_channel' """)
            if loggingchannel:
                channel = discord.utils.get(message_before.guild.channels, id=loggingchannel)
                if channel:
                    embed = discord.Embed(
                        title="Message Edited", color=discord.Color.green())
                    embed.set_author(name=message_before.author.name, icon_url=message_before.author.avatar)
                    embed.add_field(name="Channel", value=message_before.channel.mention)
                    embed.add_field(name="Before", value=message_before.content[:1000])
                    embed.add_field(name="After", value=message_after.content[:1000])
                    embed.add_field(name="Link", value=message_after.jump_url)
                    embed.set_thumbnail(url=self.bot.user.avatar)
                    await channel.send(embed=embed)

                return
            else:

                return
        except Exception or Error as e:
            print(f"Message Edit: {e}")

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.TextChannel):
        try:
            option = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(channel.guild.id)} WHERE configname='channel_logging' """)
            if not option:
                return  # channel logging feature is disabled
            loggingchannel = await get(self.bot.database,
                                       f""" SELECT configoption FROM server_{str(channel.guild.id)} WHERE configname='logging_channel' """)
            if loggingchannel:
                logchannel = discord.utils.get(channel.guild.channels, id=loggingchannel)
                if logchannel:
                    embed = discord.Embed(
                        title="Channel Created", color=discord.Color.green())
                    embed.add_field(name="Channel", value=channel.mention)
                    embed.add_field(name="Name", value=channel.name)
                    embed.set_thumbnail(url=self.bot.user.avatar)
                    await logchannel.send(embed=embed)

                return
            else:

                return
        except Exception as e:
            print(f"Channel create: {e}")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.TextChannel):
        try:
            option = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(channel.guild.id)} WHERE configname='channel_logging' """)
            if not option:
                return  # channel logging feature is disabled
            loggingchannel = await get(self.bot.database,
                                       f""" SELECT configoption FROM server_{str(channel.guild.id)} WHERE configname='logging_channel' """)
            if loggingchannel:
                logchannel = discord.utils.get(channel.guild.channels, id=loggingchannel)
                if logchannel:
                    embed = discord.Embed(
                        title="Channel Deleted", color=discord.Color.green())
                    embed.add_field(name="Channel", value=channel.name)
                    embed.set_thumbnail(url=self.bot.user.avatar)
                    await logchannel.send(embed=embed)

                return
            else:

                return
        except Exception as e:
            print(f"Channel delete: {e}")

    @commands.Cog.listener()
    async def on_guild_channel_update(self, channel_before: discord.TextChannel, channel_after: discord.TextChannel):
        try:
            if str(channel_before.type) == "category" or "voice":  # Category or Voice channels no longer get logged.
                return
            option = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(channel_before.guild.id)} WHERE configname='channel_logging' """)
            if not option:
                return  # channel logging feature is disabled
            if channel_before.name != channel_after.name:
                loggingchannel = await get(self.bot.database,
                                           f""" SELECT configoption FROM server_{str(channel_before.guild.id)} WHERE configname='logging_channel' """)
                if loggingchannel:
                    logchannel = discord.utils.get(channel_after.guild.channels, id=loggingchannel)
                    if logchannel:
                        embed = discord.Embed(
                            title="Channel Name Changed", color=discord.Color.green())
                        embed.add_field(name="Before", value=channel_before.name)
                        embed.add_field(name="After", value=channel_after.name)
                        embed.set_thumbnail(url=self.bot.user.avatar)
                        await logchannel.send(embed=embed)
                    return
                else:
                    return
            if not channel_before.topic:
                return
            if channel_before.topic != channel_after.topic:
                loggingchannel = await get(self.bot.database,
                                           f""" SELECT configoption FROM server_{str(channel_before.guild.id)} WHERE configname='logging_channel' """)
                if loggingchannel:
                    logchannel = discord.utils.get(channel_after.guild.channels, id=loggingchannel)
                    if logchannel:
                        embed = discord.Embed(
                            title="Channel Topic Changed", color=discord.Color.green())
                        embed.add_field(name="Before", value=channel_before.topic)
                        embed.add_field(name="After", value=channel_after.topic)
                        embed.add_field(name="Channel Name", value=channel_after.name)
                        embed.add_field(name="Channel", value=channel_after.mention)
                        embed.set_thumbnail(url=self.bot.user.avatar)
                        await logchannel.send(embed=embed)
                    return
                else:
                    return
        except Exception as e:
            print(f"Channel update: {e}")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.Role):
        try:
            option = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(role.guild.id)} WHERE configname='role_logging' """)
            if not option:
                return  # role logging feature is disabled
            loggingchannel = await get(self.bot.database,
                                       f""" SELECT configoption FROM server_{str(role.guild.id)} WHERE configname='logging_channel' """)
            if loggingchannel:
                logchannel = discord.utils.get(role.guild.channels, id=loggingchannel)
                if logchannel:
                    embed = discord.Embed(
                        title="Role Deleted", color=discord.Color.green())
                    embed.add_field(name="Role", value=role.name)
                    embed.add_field(name="Name", value=role.name)
                    embed.set_thumbnail(url=self.bot.user.avatar)
                    await logchannel.send(embed=embed)

                return
            else:

                return
        except Exception as e:
            print(f"Role delete: {e}")

    @commands.Cog.listener()
    async def on_guild_role_update(self, role_before: discord.Role, role_after: discord.Role):
        try:
            option = await get(self.bot.database,
                               f""" SELECT configoption FROM server_{str(role_before.guild.id)} WHERE configname='role_logging' """)
            if not option:
                return  # role logging feature is disabled
            if role_before.name != role_after.name:
                loggingchannel = await get(self.bot.database,
                                           f""" SELECT configoption FROM server_{str(role_before.guild.id)} WHERE configname='logging_channel' """)
                if loggingchannel:
                    logchannel = discord.utils.get(role_after.guild.channels, id=loggingchannel)
                    if logchannel:
                        embed = discord.Embed(
                            title="Role Name Changed", color=discord.Color.green())
                        embed.add_field(name="Before", value=role_before.name)
                        embed.add_field(name="After", value=role_after.name)
                        embed.set_thumbnail(url=self.bot.user.avatar)
                        await logchannel.send(embed=embed)
                    return
                else:
                    return
        except Exception as e:
            print(f"Role update: {e}")


async def setup(bot: commands.Cog):
    await bot.add_cog(logginglisteners(bot))
