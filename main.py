from web_server_alive import stay_running
import discord
import os
import random

#I live here now

intents = discord.Intents.all()
client = discord.Client(intents=intents)

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

  result = "Heads: " + str(heads) + "\nTails: " + str(tails) + "\nPercentage of Heads: " + str(round((heads/(heads+tails)*100), 2)) + "%"

  return result

#Using the member list of the server, creates a list of all the current users and some basic information
def getUsers(message):
  memberData = '' #Cretes an emptry string to hold all values. This could be done better with an array handling values but... :/
  for member in message.guild.members: #Finds all the members that are currently in the server/guild
          
    memberData += 'ID: ' + str(member.id) #Adds the user's ID to the list !THIS IS FINE TO BE PUBLIC 
    memberData += '\nDisplayName: ' + member.display_name
    #Adds the user's server nickname to the list
    memberData += '\nUserName: ' + member.name + '#' + member.discriminator + '\n\n'
    #Adds the user's discord name and the 4 digit discriminator

  return memberData

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    #Checks if the current message was written by the bot or not, prevents an infinite loop
    if message.author == client.user:
        return


    #COINFLIP GAME
    if message.content.startswith('$flip'):
      msg = message.content.split(' ', 1) #Splits the user's input to get the amount of flips
      if len(msg) > 1: #Checks to see if the user gave an amount
        count = int(msg[1]) #if they did, set it to count
      else:
        count = 10 #if not, set the count to 10
      await message.channel.send(coinFlipper(count)) #make the bot send a message with the results of the coin flipping

    #A list of all functions that the average user would need
    if message.content.startswith('$functions'):

      functionList = discord.Embed(title = "Functions", description="List of Functions on the Server", color = 0x00ff00) #Starts the embed off with the title and description, there can be other arguments if needed.

      functionList.add_field(name="$flip", value="flips a coin 10 times(if you put a integer after the call, it will flip that many times", inline=True) #This is how you add a line in the embed 


      await message.channel.send(embed=functionList)

    #KILLS DEVIN
    if message.content.startswith('$KillDevin'):
      await message.channel.send('<:susgun:813259245901316097> <@!121443744242335746>')





    #ADMIN FUNCTIONS


    #CREATES USER LIST
    if message.content.startswith('$getUsers'):
      await message.channel.send(getUsers(message))

stay_running() #Starts the webserver to keep the bot running
client.run(os.environ['Token']) #Turns the bot on