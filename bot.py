import discord
from discord.ext import commands
from googletrans import Translator
import os

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="()", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Find the custom emojis by name
    eng_emoji = discord.utils.get(
        bot.emojis, name="eng"
    )  # Replace 'eng' with your English emoji name
    geo_emoji = discord.utils.get(
        bot.emojis, name="ka"
    )  # Replace 'ka' with your Georgian emoji name

    if eng_emoji and geo_emoji:
        # Add the reaction emojis to all messages
        await message.add_reaction(eng_emoji)
        await message.add_reaction(geo_emoji)

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    # Check if the reaction emoji matches the one you specified
    eng_emoji = discord.utils.get(
        bot.emojis, name="eng"
    )  # Replace 'eng' with your English emoji name
    geo_emoji = discord.utils.get(
        bot.emojis, name="ka"
    )  # Replace 'ka' with your Georgian emoji name

    if reaction.emoji == eng_emoji:
        # Translate to English
        await translate_and_reply(reaction, "en")

    elif reaction.emoji == geo_emoji:
        # Translate to Georgian
        await translate_and_reply(reaction, "ka")

async def translate_and_reply(reaction, target_language):
    try:
        # Get the message where the reaction occurred
        reacted_message = reaction.message

        # Translate the original message
        text_to_translate = reacted_message.content
        translator = Translator()
        translated = translator.translate(text_to_translate, dest=target_language)

        # Reply to the original message with the translation
        await reacted_message.reply(
            f"Translated ({target_language}): {translated.text}"
        )
    except Exception as e:
        await reacted_message.reply(f"Translation error: {str(e)}")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run()

