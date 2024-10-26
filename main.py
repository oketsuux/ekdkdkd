import discord
from discord.ext import commands

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True  # This is fine to keep

bot = commands.Bot(command_prefix='!', intents=intents)

# Replace with the ID of the user you want to auto-react to
TARGET_USER_ID = 983338229233246238  # Change to the target user's ID
REACTION_EMOJI = '😭'  # Change to your desired emoji

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author.id == bot.user.id:
        return

    # Check if the message is from the target user
    if message.author.id == TARGET_USER_ID:
        await message.add_reaction(REACTION_EMOJI)

    # Process commands if any
    await bot.process_commands(message)

@bot.command()
async def set_target(ctx, user_id: int):
    global TARGET_USER_ID
    TARGET_USER_ID = user_id
    await ctx.send(f'Target user set to <@{user_id}>!')

@bot.command()
async def set_reaction(ctx, emoji: str):
    global REACTION_EMOJI
    REACTION_EMOJI = emoji
    await ctx.send(f'Reaction emoji set to {emoji}!')

# Run the bot with your token
bot.run('OTgzMzM4MjI5MjMzMjQ2MjM4.GGcMFl.7ZskElYTk499EYKSk9FFX5LTGGLpD0oI5ssOsE
')
