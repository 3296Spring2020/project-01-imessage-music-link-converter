from botObject import musicbot
import discord
import picklerick
import re

client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith('help buddy'):
        pass
        # for key in self.musicPlatformDirectory:
        #     self.helpmessage += self.musicPlatformDirectory[key]
        # await message.channel.send(self.helpmessage)
    if message.content.startswith('go buddy'):
        tokens = (message.content).split(' ')
        url = tokens[2]
        mb = musicbot('Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc')
        platform = mb.findGivenPlatform(url)
        await message.channel.send(platform)
client.run("Njk2NDM4MzEzMjE2NjM5MDA3.XpYMlA.BP7IY80x-EbPfdgLjSNVWQ3Gdgc")