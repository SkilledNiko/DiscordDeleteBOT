import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="delete", description="Deletes a specified number of messages in the channel")
@app_commands.describe(number="Number of messages to delete (default: 1000)")
async def delete(interaction: discord.Interaction, number: int = 1000):
    await interaction.response.defer(ephemeral=True) 
    channel = interaction.channel
    deleted = 0

    async for message in channel.history(limit=number):
        try:
            await message.delete()
            deleted += 1
        except discord.Forbidden:
            continue

    await interaction.followup.send(f"Deleted {deleted} messages.", ephemeral=True)



# Replace BOT_TOKEN with the bot's token (can be found in the discord bot dashboard)
bot.run('BOT_TOKEN')
