import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('Njk2NDM4MzEzMjE2NjM5MDA3.Xoov7Q.7b8X7XX2uyUDgRD9wl4s3U4j1A4')