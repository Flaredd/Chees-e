import os
import discord
import time

client = discord.Client()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('chees e'):
      await message.channel.send('-stop')
      time.sleep(0.5)
      await message.channel.send('-p cheese meme')
      time.sleep(3.5)
      await message.channel.send('https://cdn.discordapp.com/attachments/837072531420479530/837210836656979988/Ua9ddbc0277b84e37b4395c2dfe5eb40aV.jpg ')
      time.sleep(0.5)
      await message.channel.send('chees e')

client.run(os.getenv('TOKEN'))    