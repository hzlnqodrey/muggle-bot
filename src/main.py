import os
import asyncio
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands


# Dir, Import & Register Commands
from utils.response import get_response
from utils.commands import setup


# Load Env Variables
load_dotenv()

# Load Token
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True

# Create a Discord Client (For Normal Messages)
client: Client = Client(intents=intents)

# Create a Discord Bot (For Slash Commands)
bot = commands.Bot(command_prefix="!", intents=intents)

# Message Functionally
async def send_messages(message: Message, user_messages: str) -> None:

    if not user_messages:
        print("(Message was empty, because intents were not enabled)")
        return
    
    if is_private := user_messages[0] == '?':
        user_messages = user_messages[1:]

    try:
        response: str = get_response(user_messages)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f'Error: {e}')

# Handle STARTUP for the bot
@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user} and has connected to Discord - [is running!]')

# Handle Incomming Message for the bot
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author).split('#')[0]
    user_message: str = str(message.content)
    channel_name: str = str(message.channel)

    print(f'({channel_name}) {username}: {user_message}')
    await send_messages(message, user_message)

# Handle Startup for Bot & Register Commands
@bot.event
async def on_ready():
    print(f'Bot Connected: {bot.user}')

    # Sync Slash Commands
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

async def load_extensions():
    await setup(bot) # Load MathCommands

# Main | Entry Point
async def main() -> None:
    await load_extensions()

    task1 = asyncio.create_task(client.start(TOKEN))
    task2 = asyncio.create_task(bot.start(TOKEN))

    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    asyncio.run(main())