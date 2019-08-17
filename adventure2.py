instructions = ("\nHELP\n\nTo exit a room, type: east, west, south or west.\n"
                "If a room has multiple doors along one side\n   to exit through the 1st door on the east side\ntype: east door 1\n"
                "To enter the house type: go inside, enter house, or examine house.\n"
                "To quit the game type: quit.\n\n"
                "The following is a list of all the commands in the game:\n"
                "close - door, drawer, refrigerator\n"
                "examine - desk, dresser, letter, nightstand, note, table, refrigerator, sink\n"
                "go to - desk, dresser, nightstand, table, refrigerator, sink\n"
                "look at - desk, dresser, letter, nightstand, note, refrigerator, table, sink\n"
                "look in - drawer, refrigerator\n"
                "look inside - drawer, refrigerator\n"
                "look under sink\n"
                "open - door, drawer, refrigerator\n"
                "read - letter, note\n")

note = { "read note" : "The note says : Eat cake to grow bigger. Drink potion to shrink.\n",
              "look at note" : "The note says : Eat cake to grow bigger. Drink potion to shrink.\n",
              "examine note" : "The note says : Eat cake to grow bigger. Drink potion to shrink.\n"}

letter = { "read letter" : "A puppy is being held prisoner in this house. Free the puppy and return it to it's rightful place in front of the fireplace in the living room.\n",
                "examine letter" : "A puppy is being held prisoner in this house. Free the puppy and return it to it's rightful place in front of the fireplace in the living room.\n",
                "look at letter" : "A puppy is being held prisoner in this house. Free the puppy and return it to it's rightful place in front of the fireplace in the living room.\n"}

rooms = { "front" : "You are in front of an old farmhouse. The front door is open.\n",
                  "entry" : "You are in the entry way. There are 3 doors to the west and 3 doors to east. There is also one door to the north and one to the south.\n",
                  "living" : "You are in the living room. There is a letter on the coffee table. There is a fireplace with a large dog bed in front. There is a door to the west  and another door to the north.\n",
                  "library" : "You are in the library. There is a desk with a drawer. There are 3 doors, one to the west, one to the north, and one to the south.\n",
                  "bedroom" : "You are in the bedroom. There is a dresser on one side of the room and a nightstand beside the bed. The is a door to the west and another door to the south.\n",
                  "dining" : "You are in the dining room. There is a dining table in the middle of the room. There is a door to the east and another door the north.\n",
                  "kitchen" : "You are in the kitchen there is a refrigerator and a knife on the kitchen counter. There are 3 doors, one to the east, on to the north, and one to the south.\n",
                  "bathroom" : "You are in the bathroom. There is a tiny door under the sink. There is a door to the east and another to the south.\n",
                  "backyard" : "You are in the backyard. There is a well and not much else.\n"}

entry = {  "east door 1" : "dining",
                "east door 2" : "kitchen",
                "east door 3" : "bedroom",
                "west door 1" : "living",
                "west door 2" : "library",
                "west door 3" : "bathroom",
                "north" : "backyard",
                "south" : "front",
                "east" : "There are 3 doors to the east. \n You must indicate which door you wish to enter. \n (example: east door 1)",
                "west" : "There are 3 doors to the east. \n You must indicate which door you wish to enter. \n (example: west door 1)" }

living = { "east" : "entry",
                "north" : "library",
                "south" : "There is no door to the south. \n",
                "west" : "There is no door to the west. \n",
                "examine coffee table" : "It is a Greyleigh Elleton coffee table. \nThere is a letter on the coffee table. \n",
                "look at table" : "It is a Greyleigh Elleton coffee table. \nThere is a letter on the coffee table. \n",
                "examine table" : "It is a Greyleigh Elleton coffee table. \nThere is a letter on the coffee table. \n",
                "examine fireplace" : "It is a grand black marble fireplace with a large dog bed in front. \n There is nothing in the dog bed. \n",
                "look at fireplace" : "It is a grand black marble fireplace with a large dog bed in front. \n There is nothing in the dog bed. \n",
                "take letter" : "The letter is now in your inventory.\n",
                "put puppy" : "Thank you for freeing and  returning the puppy to its rightful place. \nYou have won the game!",
                "place puppy" : "Thank you for freeing and returning the puppy to its rightful place. \nYou have won the game!" }

library = { "east" : "entry",
                  "north" : "bathroom",
                  "south" : "living",
                  "west" : "There is no door to the west. \n",
                  "examine desk" : "The desk has one drawer but it appears to be locked. \n",
                  "look at desk" : "The desk has one drawer but it appears to be locked. \n",
                  "go to desk" : "The desk has one drawer but it appears to be locked. \n",
                  "unlock drawer" : "The desk drawer is now unlocked. \n",
                  "open drawer" : "There is a tiny key inside the desk drawer. \n",
                  "take key" : "The tiny key has been added to your inventory. \n" }

bedroom = { "west" : "entry",
                      "south" : "kitchen",
                      "north" : "There is no door to the north. \n",
                      "east" : "There is no door to the east. \n",
                      "examine dresser" : "It is a Chippendale Antique dresser with a large rectangular mirror. The drawers are missing. There is a key laying on top of the dresser. \n",
                       "look at dresser" : "It is a Chippendale Antique dresser with a large rectangular mirror. The drawers are missing. There is a key laying on top of the dresser. \n",
                      "go to dresser" : "It is a Chippendale Antique dresser with a large rectangular mirror. The drawers are missing. There is a key laying on top of the dresser. \n",
                      "examine nightstand" : "It is a Chippendale Antique nightstand with a single drawer. There is a silver antique Dresden clock on the nightstand. \n",
                       "look at nightstand" : "It is a Chippendale Antique nightstand with a single drawer. There is a silver antique Dresden clock on the nightstand. \n",
                       "go to nightstand" : "It is a Chippendale Antique nightstand with a single drawer. There is a silver antique Dresden clock on the nightstand. \n",
                       "open drawer" : "There is a note inside of the drawer. \n",
                       "look in drawer" : "There is a note inside of the drawer. \n",
                       "look inside drawer" : "There is a note inside of the drawer. \n",
                       "examine drawer" : "There is a note inside of the drawer. \n",
                       "close drawer" : "The drawer is now closed. \n",
                       "take key" : "The key has been added to your inventory. \n",
                       "take note" : "The note has been added to your inventory. \n" }

dining = { "north" : "kitchen",
                "east" : "entry",
                "west" : "There is no door to the east. \n",
                "south" : "There is no door to the south. \n",
                "go to table" : "It is an oval oak table with carved ornate legs and claw feet. There is a piece of cake on the table.\n",
                "look at table" : "It is an oval oak table with carved ornate legs and claw feet. There is a piece of cake on the table.\n",
                "examine table" : "It is an oval oak table with carved ornate legs and claw feet. There is a piece of cake on the table.\n",
                "take cake" : "The cake has bee added to your inventory.\n" }

kitchen = { "north" : "bedroom",
                 "south" : "dining",
                 "west" : "entry",
                 "east" : "There is no door to the east. \n",
                 "examine refrigerator" : "It is an early 2000 model refrigerator with sharp angles. It is a shiny silver color with a chrome handle. \n",
                 "look at refrigerator" : "It is an early 2000 model refrigerator with sharp angles. It is a shiny silver color with a chrome handle. \n",
                 "go to refrigerator" : "It is an early 2000 model refrigerator with sharp angles. It is a shiny silver color with a chrome handle. \n",
                 "look inside" : "There is a small bottle of potion inside the refrigerator. \n",
                 "look in refrigerator" : "There is a small bottle of potion inside the refrigerator. \n",
                 "look inside refrigerator" : "There is a small bottle of potion inside the refrigerator. \n",
                 "open refrigerator" : "There is a small bottle of potion inside the refrigerator. \n",
                 "close refrigerator" : "Refrigerator is now closed. \n",
                 "take potion" : "The potion has been added to your inventory. \n",
                 "take knife" : "The knife has been added to your inventory. \n"}

bathroom = { "east" : "entry",
                        "south" : "library",
                        "west" : "There is no door to the west. \n",
                        "north" : "There is no door to the north. \n",
                        "examine sink" : "There is a tiny door under the sink. \n",
                        "look at sink" : "There is a tiny door under the sink. \n",
                        "look under sink" : "There is a tiny door under the sink. \n",
                        "go to sink" : "There is a tiny door under the sink. \n",
                        "unlock door" : "The tiny door is unlocked. \n",
                        "open door" : "You are in a small room. There is a puppy tied up with a rope in the room. \n",
                        "cut rope" : "The puppy is now free. \n",
                        "take puppy" : "The puppy is now in your inventory. \n" }

outside = ["go inside", "enter house", "open door", "examine house"]

inventory = [ ]
room = "front"
direction = None
lockedDrawer = True
lockedDoor = True
cutRope = True
frigOpen = False
size = "normal"
won = False

print("This is a text based adventuregame. \nCommands will be a short 1 - 3 word commands")
print("To quit the game, enter 'quit' \n")

print(rooms[room])
while direction != "quit" and won == False:
     direction = input("\nWhat should I do?: ")
     if direction == "help":
          print(instructions)
     elif direction == "Where am I" :
          print(rooms[room])
     elif direction in note:
          if "note" in inventory:
               print(note[direction])
          else:
               print("You do not have a note in your inventory. \n")
     elif direction in letter:
          if "letter" in inventory:
               print(letter[direction])
          else:
               print("You do not have a letter in your inventory. \n")
     elif direction == "eat cake" :
          if "cake" in inventory:
               if size == "small" :
                    size == "normal"
                    print("You have returned to normal size. \n")
               elif size == "normal" :
                    size = "big"
                    print("You have grown bigger in size. \n")
               else:
                    print("Hmm... nothing happened. You are already big in size. \n")
     elif direction == "drink potion" :
          if "potion" in inventory:
               if size == "small" :
                    print("Hmm... nothing happened. You are already big in size. \n")
               elif size == "big" :
                    size = "normal"
                    print("You have returned to normal size. \n")
               else:
                    size == "small"
                    print("You have shrunken in size. You are only a few inches tall. \n")
     elif direction in outside and room == "front" or room == "backyard" :
          if size == "normal" or size == "small" :
               room = "entry"
               print(rooms[room])
          else:
               print("You are too big to fit through the door.")
     elif direction in entry and room == "entry" :
           room = entry[direction]
           print(rooms[room])
     elif direction in living and room == "living" :
          if direction == "east" or direction =="north" :
               if size == "normal" or size == "small" :
                    room = living[direction]
                    print(rooms[room])
               else:
                    print("You are to big to fit through the door. \n")
          elif  direction == "put puppy" or direction == "place puppy" :
               if "puppy" in inventory:
                    if size == "normal" or size == "big":
                         print(living[direction])
                         won = True
                    else:
                         print("You are too small to reach the dog bed.")
               else:
                    print("You do not have the puppy in your inventory. \n")
          elif direction == "take letter":
               if "letter" in inventory:
                    print("You already have the letter in your inventory. \n")
               else:
                    print(living[direction])
                    inventory.append("letter")
                    living["look at table"] = "It is a Greyleigh Elleton coffee table. \nThere is a letter on the coffee table. \n"
                    living["examine table"] = "It is a Greyleigh Elleton coffee table. \nThere is a letter on the coffee table. \n"
                    living["examine coffee table"] = "It is a Greyleigh Elleton coffee table. \nThere is a letter on the coffee table. \n"
          else:
                print(living[direction])
     elif direction in library and room == "library" :
          if direction == "east" or direction == "north" or direction == "south" :
               if size == "normal" or size == "small" :
                    room = library[direction]
                    print(rooms[room])
               else:
                    print("You are to big to fit in the door. \n")
          elif direction == "unlock drawer" :
               if "desk key" in inventory:
                    print(library[direction])
                    lockedDrawer = False
               else:
                    print("The do not have the key to unlock the desk drawer in your inventory. \n")
          elif direction == "open drawer" :
               if lockedDrawer == True :
                    print("The drawer is locked. You must find the key to unlock it. \n")
               else:
                    print(library[direction])
          elif direction == "take key" :
               if "tiny key" in inventory:
                    print("The tiny key is already been added to your inventory. \n")
               elif lockedDrawer == False:
                    print(library[direction])
                    inventory.append("tiny key")
                    library["open drawer"] = "The drawer is empty. \n"
               else:
                    print(library[direction])
     elif direction in bedroom and room == "bedroom" :
          if direction == "west" or direction == "south" :
               if size == "normal" or size == "small" :
                    room = bedroom[direction]
                    print(rooms[room])
               else:
                    print("You are too big to fit through the door. \n")
          elif direction == "take key" :
               if "desk key" in inventory:
                    print("You have already taken the key and added it to your inventory. \n")
               else:
                    print(bedroom[direction])
                    inventory.append("desk key")
                    bedroom["go to dresser"] = "It is a Chippendale Antique dresser with a large rectangular mirror. The drawers are missing. \n"
                    bedroom["examine dresser"] = "It is a Chippendale Antique dresser with a large rectangular mirror. The drawers are missing. \n"
                    bedroom["look at dresser"] = "It is a Chippendale Antique dresser with a large rectangular mirror. The drawers are missing. \n"                    
          elif direction ==  "take note" :
               if "note" in inventory:
                    print("The note is already in your inventory. \n")
               else:
                    print(bedroom[direction])
                    inventory.append("note")
          else:
               print(bedroom[direction])
     elif direction in dining and room == "dining" :
          if direction == "north" or direction == "east" :
               if size == "normal" or size == "small" :
                    room = dining[direction]
                    print(rooms[room])
               else:
                    print("You are too big to fit through the door. \n")
          elif direction ==  "take cake" :
               if "cake" in inventory:
                    print("The cake is already in your inventory. \n")
               else:
                    print(dining[direction])
                    inventory.append("cake")
          else:
               print(dining[direction])
     elif direction in kitchen and room == "kitchen" :
          if direction == "south" or direction == "west" or direction == "north" :
               if size == "normal" or size == "small" :
                    room = kitchen[direction]
                    print(rooms[room])
               else:
                    if "potion" in inventory:
                         print("You are too big to fit through the door. \n")
                    else:
                         print("You are too big to fit through the door. You don't have any potions to shrink your size. \n")
                         print("You are eternally stuck. You lose!!! \n")
                         direction = "quit"
          elif direction ==  "take potion" :
               if "potion" in inventory:
                    print("The potion is already in your inventory. \n")
               else :
                    if frigOpen == False :
                         print("I don't see any potion to take. \n")
                    else:
                         print(kitchen[direction])
                         inventory.append("potion")
                         kitchen["open refrigerator"] = "The refrigerator is empty. \n"
                         kitchen["look inside refrigerator"] = "The refrigerator is empty. \n"
                         kitchen["look in refrigerator"] = "The refrigerator is empty. \n"
                         kitchen["look inside"] = "The refrigerator is empty. \n"
          elif direction ==  "take knife" :
               if "potion" in inventory:
                    print("The knife is already in your inventory. \n")
               else :
                         print(kitchen[direction])
                         inventory.append("knife")
          elif direction ==  "open refrigerator" :
               if frigOpen == False :
                    print(kitchen[direction])
                    frigOpen = True
               else:
                    print("The refrigerator is already open. \n")
          elif direction == "close refrigerator" :
               print(kitchen[direction])
               fridOpen = False
          else:
               print(kitchen[direction])
                 
     elif direction in bathroom and room == "bathroom" :
          if direction == "east" or direction == "south" :
               if size == "normal" or size == "small" :
                    room = bathroom[direction]
                    print(rooms[room])
               else:
                    print("You are too big to fit through the door. \n")
          elif direction == "unlock door" :
               if "tiny key" in inventory:
                    print(bathroom[direction])
                    lockedDoor = False
               else:
                    print("You do not have the key to open the door in your inventory. \n")
          elif direction == "open door" :
               if lockedDoor == True :
                    print("The door is locked. You must find the key to unlock it. \n")
               else:
                    if size == "normal" :
                         print(bathroom[direction])
                    else:
                         print("You are too big to fit through the door. \n")                
          elif direction == "cut rope" :
               if "knife" in inventory:
                    print(bathroom[direction])
                    cutRope = False
               else:
                    print("The do not have the knife in your inventory. \n")
          elif direction == "cut rope" :
               if cutRope == True :
                    print("The rope is intact you cannot free the puppy. You must find the knife to cut it. \n")                    
               else:
                    print(bathroom[direction])
          elif direction == "take puppy" :
               if "puppy" in inventory:
                    print("You already have the puppy in your inventory. \n")
               else:
                    print(bathroom[direction])
                    inventory.append("puppy")
          else:
               print(bathroom[direction])
     elif direction == "show inventory" :
          print(inventory)
     elif direction == "give up" :
          print("You lose. \n")
     else:
          print("I can't do that.  /n")
