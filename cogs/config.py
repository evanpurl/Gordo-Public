import datetime

import discord
from discord import app_commands
from discord.ext import commands
from utils.databasefunctions import insert
from aiomysql import Error


class configcmd(commands.GroupCog, name="gordo-config"):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="welcome-channel", description="Command to set your server's welcome channel.")
    async def welcomechannel(self, interaction: discord.Interaction, channel: discord.TextChannel = None,
                             reset: bool = None):
        try:
            if reset:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                VALUES( 'welcome_channel', 0)""")
                await interaction.response.send_message(
                    f"Your server's Welcome Channel has been reset.",
                    ephemeral=True)
                return
            if channel:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                VALUES( 'welcome_channel', {channel.id})""")
                await interaction.response.send_message(
                    f"Your server's Welcome Channel has been set to {discord.utils.get(interaction.guild.channels, id=channel.id).mention}.",
                    ephemeral=True)
                return
            else:
                await interaction.response.send_message(
                    f"*Ribbit* You didn't select any options you silly goose.",
                    ephemeral=True)
                print(f"No options selected.")
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="goodbye-channel", description="Command to set your server's goodbye channel.")
    async def goodbyechannel(self, interaction: discord.Interaction, channel: discord.TextChannel = None,
                             reset: bool = None):
        try:
            if reset:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'goodbye_channel', 0)""")
                
                await interaction.response.send_message(
                    f"Your server's Goodbye Channel has been reset.",
                    ephemeral=True)
                return
            else:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'goodbye_channel', {channel.id})""")
                
                await interaction.response.send_message(
                    f"Your server's Goodbye Channel has been set to {discord.utils.get(interaction.guild.channels, id=channel.id).mention}.",
                    ephemeral=True)
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="default-role", description="Command to set your server's default channel.")
    async def defaultrole(self, interaction: discord.Interaction, role: discord.Role = None,
                          reset: bool = None):
        try:
            if reset:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'default_role', 0)""")
                
                await interaction.response.send_message(
                    f"Your server's Default Role has been reset.",
                    ephemeral=True)
                return
            if role:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'default_role', {role.id})""")
                
                await interaction.response.send_message(
                    f"Your server's Default Role has been set to {discord.utils.get(interaction.guild.roles, id=role.id).mention}.",
                    ephemeral=True)
                return
            else:
                await interaction.response.send_message(
                    f"*Ribbit* You didn't select any options you silly goose.",
                    ephemeral=True)
                #  print(f"No options selected.")
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name="logging-channel", description="Command to set your server's logging channel.")
    async def loggingchannel(self, interaction: discord.Interaction, channel: discord.TextChannel = None,
                             reset: bool = None):
        try:
            if reset:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'logging_channel', 0)""")
                
                await interaction.response.send_message(
                    f"Your server's Logging Channel has been reset.",
                    ephemeral=True)
                return
            if channel:
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                VALUES( 'logging_channel', {channel.id})""")
                # Toggles all logging options on
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                VALUES( 'channel_logging', 1)""")
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                VALUES( 'role_logging', 1)""")
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                    VALUES( 'moderation_logging', 1)""")
                await insert(self.bot.database, f"""REPLACE INTO server_{str(interaction.guild.id)} (configname, configoption) 
                                                                                    VALUES( 'message_logging', 1)""")

                

                await interaction.response.send_message(
                    f"Your server's Logging Channel has been set to {discord.utils.get(interaction.guild.channels, id=channel.id).mention}.",
                    ephemeral=True)
                return
            else:
                await interaction.response.send_message(
                    f"*Ribbit* You didn't select any options you silly goose.",
                    ephemeral=True)
                #  print(f"No options selected.")
        except Exception or Error as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @welcomechannel.error
    @goodbyechannel.error
    @defaultrole.error
    @loggingchannel.error
    async def onerror(self, interaction: discord.Interaction, error: app_commands.MissingPermissions):
        await interaction.response.send_message(content=error,
                                                ephemeral=True)


async def setup(bot):
    await bot.add_cog(configcmd(bot))
