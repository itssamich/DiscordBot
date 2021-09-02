from web_server_alive import stay_running
import discord
import os
import random

client = discord.Client()

def coinFlipper(counter):
  heads = 0
  tails = 0

  for i in range (counter):
    randomval = random.randint(0, 1)
    if randomval == 0:
      heads +=1
    else:
      tails +=1

  result = "heads: ", heads, " tails: ", tails, " percentage of heads: ", round((heads/(heads+tails)*100), 2), "%"
  return result

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$coinflip'):
      count = 10
      try:
        msg = await client.wait_for('message', timeout = 5.0)
        count = int(msg.content)
      except:
        await message.channel.send("Need to specify amount of flips!")
        return

      await message.channel.send(coinFlipper(count))

    if message.content.startswith('$test'):
        await message.channel.send('Test!')

stay_running()
client.run(os.environ['Token'])