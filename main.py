import os
import asyncio
import discord

from utils.databasefunctions import create_pool, create_data_pool
from utils.load_extensions import load_extensions  # Our code
from discord.ext import commands
from dotenv import load_dotenv

from utils.talking_utils import create_speech_pool

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix="$", intents=intents)

load_dotenv()


# Main function to load extensions and then load bot.
async def main():
    async with client:
        try:
            await load_extensions(client)

            client.database = await create_pool()
            client.speech_database = await create_speech_pool()
            if client.database:
                print("Connected to Config Database")
            if client.speech_database:
                print("Connected to Speech Database")
            await client.start(os.getenv('token'))
        except KeyboardInterrupt:
            pass


asyncio.run(main())  # Runs main function above
