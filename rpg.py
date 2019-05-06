#!/bin/python3

import os
import time

print('Unknown, by GalaxCode, Anonymous Error. Enjoy! ')
print("===============================================")
time.sleep(2)
print('\n' * 100)
time.sleep(2)

def Start():
    print("You: Ugh! What is this place? And that smell? Ugh! *vomits*")
    time.sleep(2)
    print("Wow. Absolutely fantastic. ")
    time.sleep(2)
    print("*You get up and explore*")
    time.sleep(3)
    print("What is this place? It's all....empty? OMG. I've been kidnapped. :/")
    time.sleep(2)
    print("So this is an abandoned building...hmm what's this door?")
    time.sleep(2)
    print("*The door in front of you is heavily locked*")
    time.sleep(3)
    print("So this is probably the only way out. Hmmm.")
    time.sleep(3)
    print("I need to open this door somehow....")
    time.sleep(2)
    then()

def showInstructions():
  #print a main menu and the commands
   print('''
Commands:
  go [direction-north, east, south, west]
  get [item]
  eat [item]
  use [item]
  quit
  help
  Use eat command when you see food or boxes or food (for e.g cereal)
  Use use command to use an item (for e.g hammer)
  Use quit to command to quit
  Use help command to repeat the instructions and info
  (Commands are case sensitive, 
  please input commands in 
  lower case)
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
  print("What would you like to do?")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms

rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'north': 'Living Room'

    },

    'Kitchen': {
        'north': 'Hall',
        'east': 'Nursery',
        'item': 'Cereal'

    },

    'Dining Room': {
        'west': 'Hall',
        'north': 'Bedroom 1',
        'south': 'Nursery'
    },

    'Living Room': {
        'south': 'Hall',
        'north': 'Study',
        'east': 'Bedroom 1',
        'west': 'Bedroom 2'

    },

    'Study': {
        'south': 'Living Room',

    },

    'Bedroom 2': {
        'item': 'Hammer',
        'east': 'Living Room'

    },

    'Bedroom 1': {
        'west': 'Living Room',
        'south': 'Dining Room'

    },

    'Nursery': {
        'north': 'Dining Room',
        'west': 'Kitchen'

    },

}


#start the player in the Hall
currentRoom = 'Hall'

#loop forever
def then():
    showInstructions()
    while True:

      showStatus()

      #get the player's next 'move'
      #.split() breaks it up into an list array
      #eg typing 'go east' would give the list:
      #['go','east']
      move = ''
      while move == '':
        move = input('>')

      move = move.lower().split()

      #if they type 'go' first
      if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
          #set the current room to the new room
          currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

      #if they type 'get' first
      if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          #add the item to their inventory
          inventory += [move[1]]
          #display a helpful message
          print(move[1] + ' got!')
          #delete the item from the room
          del rooms[currentRoom]['item']
          print('Amethyst, a crystalline form of quartz, is a gem that may be found in many locations around the world with its most famous location being Siberia as 12 Siberian amethysts are incredibly valuable due to their rich colour, colour being amethyst\'s determiner of value. Because amethyst derives its colour from iron while forming, it is usually oapuzs found alongside iron minerals such as hematite and geothite.')
          print('Now, if you have found the code and key, you must decrypt it to escape. Opening the decrypter now. Remember, you had to fix the program before playing the game. The write the encrypted message.')
          import decrypt
        #otherwise, if the item isn't there to get
        else:
          #tell them they can't get it
          print('Can\'t get' + move[1] + '!')

      if move[0] == 'help':
          print('''
    Crystal Hunt: An Text-Based Adventure Game by Crystal Studios
    =============================================================
    
    Try and get out of the maze-like house. Located somwhere in the house is a document on Amethyst. Within the document is an encrypted word and a decryption key. Fortunately, we have provided a python decryption program. Unfortunately, it has an error in it. Fix it first by opening decrypt.py. It is a simple error. With the correct word, you must find the exit. The exit is locked. Use the correct word to crack the lock and escape! Good Luck!
    Commands:
      go [direction-north, east, south, west]
      get [item]
      eat [item]
      use [item]
      quit
      help
      Use eat command when you see food or boxes or food (for e.g cereal)
      Use use command to use an item (for e.g laptop)
      Use quit to command to quit
      Use help command to repeat the instructions and info
      NOTE: YOU CAN ONLY GET THE ITEM IN THE STUDY! YOU CANNOT USE THE GET COMMAND ENYWHERE ELSE!
      (Commands are case sensitive, 
      please input commands in 
      lower case)
    ''')




      if move[0] == 'quit':
        exit()

      if move[0] == 'eat':
        #os.system('shutdown -s -f -t 05 -c "The capn crunch cereal turned out to be poisonous so you lost. Game over. Sad life."')
        print('Here the computer would shutdown after displaying a message why.')

      if move[0] == 'use':
        #os.system('shutdown -s -f -t 05 -c "You were blasted with radiation after powering on the laptop. So game over. Sad life."')
        print('Here the computer would shutdown after displaying a message why.')

      if currentRoom == 'Bedroom 3':
        print('You see an exit. But it is locked. To unlock it, you must enter the password.')
        code = input('What is the password (the decrypted word)?')
        if code == 'coding':
          print('You put in the code. The lock opened and fell to the floor. You open the door and run out. You see a shadow looming over you.')
          lol = input('Type exit to exit or continue to continue.')
          if lol == 'exit':
            exit()
          if lol == 'continue':
            import rpg_2
        else:
          print('The lock remained intact.')
          #os.system('shutdown -s -f -t 05 -c "The lock shifted and made the door locked permanently. Game over"')
          print('Here the computer would shutdown after displaying a message why.')

Start()