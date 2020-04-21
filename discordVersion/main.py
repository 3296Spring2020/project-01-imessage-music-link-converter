import botObject
import discord
import re

client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith('help buddy'):
        bot_instance = botObject.musicbot('')
        await message.channel.send(bot_instance.help_message)
    if message.content.startswith('go buddy'):
        bot_instance = botObject.musicbot('Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc')
        new_link = bot_instance.run_translation(message.content)
        await message.channel.send(new_link)
client.run("Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc")
