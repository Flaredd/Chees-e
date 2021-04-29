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
      await message.channel.send('https://cdn.discordapp.com/attachments/837072531420479530/837244529282646016/Cheese_meme.gif')
      time.sleep(1.5)
      await message.channel.send(':cheese: chees e')
      time.sleep(10)
    

    if message.content.startswith('cumman'):
      await message.channel.send('plch')
      await message.channel.send('he is dat feta chees e')
      await message.channel.send('https://cdn.discordapp.com/attachments/837072531420479530/837255143179157524/unknown.png')   

    if message.content.startswith('disect plch'):
      await message.channel.send('disecting plch...')
      time.sleep(2)
      await message.channel.send('here are his body parts:')   
      await message.channel.send(':white_large_square: :white_medium_small_square::white_medium_square::white_small_square::white_medium_small_square::white_large_square::white_medium_small_square::white_small_square::white_small_square::white_medium_square::white_medium_small_square::white_large_square::white_medium_small_square::white_medium_square::white_small_square: ')    
    if message.content.startswith('e seehc'):
      await message.channel.send('https://cdn.discordapp.com/attachments/837072531420479530/837244529282646016/Cheese_meme.gif')
      time.sleep(1.5)
      await message.channel.send(':cheese: chees e')



client.run(os.getenv('TOKEN'))    