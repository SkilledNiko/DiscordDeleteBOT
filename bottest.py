import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable the intent for message content

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def clearmsg(ctx, num_messages: int = 1000):
    """Deletes a specified number of messages in the current channel (default: 1000)."""
    if ctx.author == bot.user:
        return

    # fatch / look for the last "num_messages" messages in the channel
    messages = []
    async for message in ctx.channel.history(limit=num_messages + 1):
        messages.append(message)

    # Delete all messages except for the command itself
    for message in messages:
        if message.id != ctx.message.id:
            await message.delete()

# Replace BOT_TOKEN with the bot's token (can be found in the discord bot dashboard)
bot.run('BOT_TOKEN')
