from web_server_alive import stay_running
import discord
import os
import random

client = discord.Client()

#Flips an amount of coins and returns the amount of both heads and tails along with the percentage of heads
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

      msg = message.content.split(' ', 1) #Splits the user's input to get the amount of flips
      if len(msg) > 1: #Checks to see if the user gave an amount
        count = int(msg[1]) #if they did, set it to count
      else:
        count = 10 #if not, set the count to 10
      await message.channel.send(coinFlipper(count)) #make the bot send a message with the results of the coin flipping

    if message.content.startswith('$test'):
        await message.channel.send('Test!')

    if message.content.startswith('$KillDevin'):
      await message.channel.send(':susgun: @Dodo/Devin')

stay_running() #Starts the webserver to keep the bot running
client.run(os.environ['Token']) #Turns the bot on