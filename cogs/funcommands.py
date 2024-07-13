import discord
from discord import app_commands
from discord.ext import commands

from utils.databasefunctions import insert


class funcmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clap", description="Command for the bot to clap for you or a friend.")
    async def clap(self, interaction: discord.Interaction, user: discord.User = None):
        try:
            if user is None:
                await interaction.response.send_message(content=f"""{self.bot.user.name} claps for you 👏""",
                                                        ephemeral=True)
                
            else:
                if user.id == self.bot.user.id:
                    await interaction.response.send_message(content=f"""{self.bot.user.name} claps for himself. 👏""",
                                                            ephemeral=True)
                    
                else:
                    await interaction.response.send_message(
                        content=f"""{self.bot.user.name} claps for {user.mention}! 👏""")
                    
        except Exception as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.command(name="punch", description="Command to get punched")
    async def punch(self, interaction: discord.Interaction, user: discord.User = None):
        try:
            if user is None:
                await interaction.response.send_message(
                    content=f"""{self.bot.user.name} punches you 👊 <:GordoBeanie:1185829164020936776>""", ephemeral=True)
                
            else:
                if user.id == self.bot.user.id:
                    await interaction.response.send_message(content=f"""I can't punch myself, duh.""", ephemeral=True)
                    
                else:
                    await interaction.response.send_message(
                        content=f"""{self.bot.user.name} punches {user.mention} 👊 <:GordoBeanie:1185829164020936776>""")
                    
        except Exception as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.command(name="poke", description="Command to get poked")
    async def poke(self, interaction: discord.Interaction, user: discord.User = None):
        try:
            if user is None:
                await interaction.response.send_message(content=f"""{self.bot.user.name} pokes you 🫵""", ephemeral=True)
                
            else:
                if user.id == self.bot.user.id:
                    await interaction.response.send_message(content=f"""{self.bot.user.name} pokes himself.""",
                                                            ephemeral=True)
                    
                else:
                    await interaction.response.send_message(content=f"""{self.bot.user.name} pokes {user.mention} 👆""")
                    
        except Exception as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.command(name="pat", description="Command to get patted")
    async def pat(self, interaction: discord.Interaction, user: discord.User = None):
        try:
            if user is None:
                await interaction.response.send_message(
                    content=f"""{self.bot.user.name} pats your head <:Gordo:1185828693495525408>""",
                    ephemeral=True)
                
            else:
                if user.id == self.bot.user.id:
                    await interaction.response.send_message(content=f"""I can't pet my own head, silly.""",
                                                            ephemeral=True)
                    
                else:
                    await interaction.response.send_message(
                        content=f"""{self.bot.user.name} pats {user.mention}'s head <:Gordo:1185828693495525408>""")
                    
        except Exception as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.command(name="hug", description="Command for the bot to hug you or a friend.")
    async def hug(self, interaction: discord.Interaction, user: discord.User = None):
        try:
            if user is None:
                await interaction.response.send_message(content=f"""{self.bot.user.name} hugs you 🤗""", ephemeral=True)
                
            else:
                if user.id == self.bot.user.id:
                    await interaction.response.send_message(content=f"""{self.bot.user.name} hugs himself. 🤗""",
                                                            ephemeral=True)
                    
                else:
                    await interaction.response.send_message(content=f"""{self.bot.user.name} hugs {user.mention}! 🤗""")
                    
        except Exception as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)

    @app_commands.command(name="kiss", description="Command for the bot to kiss you or a friend.")
    async def kiss(self, interaction: discord.Interaction, user: discord.User = None):
        try:
            if user is None:
                await interaction.response.send_message(content=f"""{self.bot.user.name} kisses you 😘""", ephemeral=True)
                
            else:
                if user.id == self.bot.user.id:
                    await interaction.response.send_message(content=f"""{self.bot.user.name} stares at your confused.""", ephemeral=True)
                    
                else:
                    await interaction.response.send_message(content=f"""{self.bot.user.name} kisses {user.mention}! 😘""")
                    
        except Exception as e:
            print(e)
            await interaction.response.send_message(content=f"""Something went wrong.""", ephemeral=True)


async def setup(bot):
    await bot.add_cog(funcmds(bot))
