import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('chees e'):
      await message.channel.send('c')
      await message.channel.send('h')
      await message.channel.send('e')
      await message.channel.send('e')
      await message.channel.send('s')
      await message.channel.send('e')

my_secret = os.environ['TOKEN']

client.run(os.getenv('TOKEN'))    