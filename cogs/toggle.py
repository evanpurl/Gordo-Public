import discord
from discord import app_commands
from discord.ext import commands
from utils.databasefunctions import insert
from aiomysql import Error


class optionscmd(commands.GroupCog, name="gordo-options"):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="channel-logging", description="Command to enable or disable channel logging")
    async def channel_logging(self, interaction: discord.Interaction, option: bool):
        try:
            if option:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'channel_logging', 1)""")
                
                await interaction.response.send_message(
                    f"Channel logging has been enabled!",
                    ephemeral=True)
                return
            else:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                VALUES( 'channel_logging', 0)""")
                
                await interaction.response.send_message(
                    f"Channel logging has been disabled!",
                    ephemeral=True)
                return
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="message-logging", description="Command to enable or disable message logging")
    async def message_logging(self, interaction: discord.Interaction, option: bool):
        try:
            if option:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                    VALUES( 'message_logging', 1)""")
                
                await interaction.response.send_message(
                    f"Message logging has been enabled!",
                    ephemeral=True)
                return
            else:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                    VALUES( 'message_logging', 0)""")
                
                await interaction.response.send_message(
                    f"Message logging has been disabled!",
                    ephemeral=True)
                return
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="role-logging", description="Command to enable or disable role logging")
    async def role_logging(self, interaction: discord.Interaction, option: bool):
        try:
            if option:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'role_logging', 1)""")
                
                await interaction.response.send_message(
                    f"Role Logging has been enabled!",
                    ephemeral=True)
                return
            else:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                VALUES( 'role_logging', 0)""")
                
                await interaction.response.send_message(
                    f"Role Logging has been disabled!",
                    ephemeral=True)
                return
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="moderation-logging", description="Command to enable or disable moderation logging")
    async def moderation_logging(self, interaction: discord.Interaction, option: bool):
        try:
            if option:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                    VALUES( 'moderation_logging', 1)""")
                
                await interaction.response.send_message(
                    f"Moderation Logging has been enabled!",
                    ephemeral=True)
                return
            else:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                    VALUES( 'moderation_logging', 0)""")
                
                await interaction.response.send_message(
                    f"Moderation Logging has been disabled!",
                    ephemeral=True)
                return
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @channel_logging.error
    @role_logging.error
    @moderation_logging.error
    @message_logging.error
    async def onerror(self, interaction: discord.Interaction, error: app_commands.MissingPermissions):
        await interaction.response.send_message(content=error,
                                                ephemeral=True)


async def setup(bot):
    await bot.add_cog(optionscmd(bot))
