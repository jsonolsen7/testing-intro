from collections import namedtuple
import datetime
import logging
logging.basicConfig(filename="story_project.log", level=logging.DEBUG)

# Classses (not functional, just for practice with classes)
# class Person():

#     weight_limit = 300
#     time_limit = 0

#     def __init__(self, name):
#         self.name = name
#         self.selected_items = []

#     def select(self, item, quantity):
#         if hasattr(item, 'hours_lasted'):
#             self.time_limit += item.hours_lasted * quantity
#         self.selected_items.extend([(item.name, quantity)])
#         self.weight_limit -= item.weight * quantity


# class Item():
#     def __init__(self, name, weight, quantity):
#         self.name = name
#         self.weight = weight
#         self.quantity = quantity
    
#     def __repr__(self):
#         return str(self.name) + "; weight = " + str(self.weight) + "; quantity = " + str(self.quantity) + "\n"
    
# class ExtendedItem(Item):
#     def __init__(self, name, weight, quantity, hours_lasted = 10):
#         super().__init__(name, weight, quantity)
#         self.hours_lasted = hours_lasted

#     def __repr__(self):
#         return str(self.name) + "; weight = " + str(self.weight) + "; quantity = " + str(self.quantity) + "; hours_lasted = " + str(self.hours_lasted) + "\n"

# items_list = []
# water = Item("water", 7.5, 6)
# food_capsules = Item("food capsule pack", 5, 5)
# magnetic_compass = Item("magnetic compass", 1, 1)
# box_of_matches = Item("box of matches", .1, 10)
# stellar_map = Item("stellar map", .5, 1)
# rope = Item("50ft nylon rope", 1, 1)
# first_aid_kit = Item("first aid kit", 1, 2)
# parachute = Item("parachute silk", 2, 1)
# life_raft = Item("self-inflating life raft", 15, 1)
# pistol = Item(".45 calibre pistol", .5, 1)
# oxygen_tank = ExtendedItem("100lb oxygen tank", 17, 20)
# items_list.extend([water, food_capsules, magnetic_compass, box_of_matches, stellar_map, rope, first_aid_kit, parachute, life_raft, pistol, oxygen_tank])
# print(items_list)

# jason = Person("jason")
# jason.select(water, 4)
# jason.select(food_capsules, 3)
# jason.select(oxygen_tank, 14)
# print(jason.selected_items)
# print(jason.selected_items[1][1])
# print(jason.weight_limit)
# print(jason.time_limit)

# Named Tuples (functional)
items_list = []
Item = namedtuple("Item", "name weight quantity")
water = Item("water", 7.5, 6)
food_capsules = Item("food capsule pack", 5, 5)
magnetic_compass = Item("magnetic compass", 1, 1)
box_of_matches = Item("box of matches", .1, 10)
stellar_map = Item("stellar map", .5, 1)
rope = Item("50ft nylon rope", 1, 1)
first_aid_kit = Item("first aid kit", 1, 2)
parachute = Item("parachute silk", 2, 1)
life_raft = Item("self-inflating life raft", 15, 1)
pistol = Item(".45 calibre pistol", .5, 1)
ExtendedItem = namedtuple("ExtendedItem", [*Item._fields, "hours_lasted"])
oxygen_tank = ExtendedItem("100lb oxygen tank", 17, 20, 10)
items_list.extend([water, food_capsules, magnetic_compass, box_of_matches, stellar_map, rope, first_aid_kit, parachute, life_raft, pistol, oxygen_tank])


def conclusion():
    print("You successfully made it the rest of the journey and safely made it to base camp.")
    print("-----------------------")
    print("After treating yourself to a nice meal, you venture out and deliver the necessary materials that Opportunity Mars requires to survive and continue collecting precious Moon data.")
    print("-----------------------")
    logging.info(f"You completed your journey at {datetime.datetime.now()}")
    exit()
    
def startJourney():
    print("You and Mr. Jingles are all suited-up and ready to go. Opportunity Mars just tweeted his final tweet and time is running out!")
    print("-----------------------")
    if selected_items[0][0] == "stellar map" or selected_items[1][0] == "stellar map" or selected_items[2][0] == "stellar map" or selected_items[3][0] == "stellar map" or selected_items[4][0] == "stellar map":
        direction = input("Good job selecting a stellar map. Do you want to go North or West first? ")
    else:
        direction = input("Which direction should you go? North, South, East or West? ")
        print("-----------------------")

    if direction.lower() == "south" or direction.lower() == "east":
        logging.info(f"You chose the wrong direction at {datetime.datetime.now()}")
        print("This is the wrong direction. Did you read the intro directions?")
        print("-----------------------")
        print("-----------------------")
        startJourney()
    elif direction.lower() == "north" or direction.lower() == "west":
        logging.info(f"You chose the right direction at {datetime.datetime.now()}")
        print("You start heading in the correct direction. You moon-jump your way across craters and large moonrocks. There aren't any major obstacles ahead of you, so you and Mr. Jingles are actually having a lot of fun despite Opportunity Mars's impending doom (and possibly yours).")
        print("-----------------------")

    print("You successfully make it half-way through your journey but come across a very large mass of boulders.")
    print("-----------------------")
    print("You notice there is a cave in the middle, which might be a shortcut. Otherwise, you have to travel around the boulders.")
    print("-----------------------")
    choice = input("Input 1 for the cave and 2 to travel around them. ")
    print("-----------------------")
    if choice == "2":
        logging.info(f"You got delayed in a storm at {datetime.datetime.now()}")
        print("You decided to travel around and got caught in a dust storm. You got delayed by 48 hours.")
        print("-----------------------")
        global time_limit
        time_limit -= 48
        print("You have ", time_limit, " hours left.")
        print("-----------------------")
        if time_limit >= 25:
            conclusion()
        else:
            print("You don't have enough time to finish the journey. You should have prepared better. Have fun suffocating.")
            print("-----------------------")
    elif choice == "1":
        logging.info(f"You entered the cave at {datetime.datetime.now()}")
        print("You decided to enter the cave. It is dark but luckily your fancy spacesuit has nightvision.")
        print("-----------------------")
        print("After you walkthrough the cave for awhile, you notice there is an opening on the other end. However, you also notice a shadowy figure move across the opening. Mr. Jingles in cowering in fear and climbs onto your back.")
        print("-----------------------")
        print("You comfort Mr. Jingles, but continue to travel through the cave.")
        print("-----------------------")
        print("All the sudden, a terrifying alien (the one from Prometheus) drops from the ceiling and unleashes a deafening screech. His snake-like tongue darts out of his mouth, nearly 5 inches from your face.")
        print("-----------------------")
        if selected_items[0][0] == ".45 calibre pistol" or selected_items[1][0] == ".45 calibre pistol" or selected_items[2][0] == ".45 calibre pistol" or selected_items[3][0] == ".45 calibre pistol" or selected_items[4][0] == ".45 calibre pistol":
            logging.info(f"You shot that b**** in the face at {datetime.datetime.now()}")
            print("You quickly pull out your pistol and shoot that b**** in the face. His purple blood splatters all over the place. The terrified Mr. Jingles runs toward the opening and you chase after him.")
            print("-----------------------")
        else:
            print("Since you do not have a weapon, you throw dirt in his face to distract him and start running away toward the opening. However, Mr. Jingles in weighing you down. The alien is faster than you and closing in.")
            print("-----------------------")
            print("You throw Mr. Jingles ahead of you so you can both survive. However, he is not as fast as a human. As you exit the cave, you hear the horrific screams of Mr. Jingles being eaten.")
            logging.info(f"You got Mr. Jingles killed at {datetime.datetime.now()}")
            print("-----------------------")
            print("After getting as far away as you can, you mourn the life of Mr. Jingles. You are very sad so it took about 4 hours.")
            print("-----------------------")
            print("Luckily, you now have a lot more time because you can use his share of oxygen.")
            print("-----------------------")
        conclusion()

selected_items = []
weight_limit = 300
def selectItems():
    print("-----------------------")
    print("First, you must prepare for your trek across the cold, dark surface of the Moon. WARNING: Unknown dangers lie ahead.")
    print("-----------------------")
    print("You must select essential items to bring with you, however, because you don't work out as much as you should, you cannot carry more than 250 pounds. Also, as your partner is a monkey, he cannot carry more than 50 pounds.")
    print("-----------------------")
    print("There is some good news: Objects on the Moon weight 1/6th than they do on Earth.")
    print("-----------------------")
    print("Therefore, you must consider weight limit, but also time limit. You are 200 miles away and most people walk 4 miles per hour, thus you have a 50 hour journey ahead of you - assuming no delays ;).")
    print("-----------------------")
    print("Think it over for a moment. Just remember that every moment you spend preparing, Opportunity Mars is closer to dying. Tick tock!")
    print("-----------------------")
    print("Choose 5 items from the following list of items (be careful not to exceed quantity limit):")
    for item in items_list:
        print("----------------------------------")
        for field, value in zip(item._fields, item):
            print(field, " - ", value)
    global weight_limit
    print("-----------------------")
    print("-----------------------")
    item1, quantity1 = input("Choose your first item (enter the full item description, separated by a comma): ").split(",")
    print("-----------------------")
    logging.info(f"You chose your first item at {datetime.datetime.now()}")
    selected_items.append([item1.strip(), int(quantity1.strip())])
    print("You've successfully chosen:")
    print("-----------------------")
    print(selected_items)
    print("-----------------------")
    # OXYGEN TANK
    if selected_items[0][0] != "100lb oxygen tank":
        print("However, you really should consider switching careers if oxygen wasn't your first choice...Try again.")
        print("-----------------------")
        exit()
    elif selected_items[0][1] < 10:
        print("I take it math wasn't your favorite subject? Either you or Mr. Jingles will die a most painful death...Try again.")
        print("-----------------------")
        exit()
    elif weight_limit >= 0 and selected_items[0][0] == "100lb oxygen tank" and selected_items[0][1] <= oxygen_tank[2]:
        weight_limit -= (int(quantity1) * oxygen_tank[1])
        global time_limit
        time_limit = int(quantity1) * 10 / 2
        print("Ah, yes. Precious life molecules. Hope you brought enough in case of unexpected delays ;)")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left", " and ", time_limit, "hours of oxygen.")
    elif selected_items[0][0] == "100lb oxygen tank" and selected_items[0][1] > oxygen_tank[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # WATER
    elif weight_limit >= 0 and selected_items[0][0] == "water" and selected_items[0][1] <= water[2]:
        weight_limit -= (int(quantity1) * water[1])
        print("Good choice! You're gonna get thirsty.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "water" and selected_items[0][1] > water[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FOOD CAPSULE PACK
    elif weight_limit >= 0 and selected_items[0][0] == "food capsule pack" and selected_items[0][1] <= food_capsules[2]:
        weight_limit -= (int(quantity1) * food_capsules[1])
        print("Good choice! You're gonna get hungry.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "food capsule pack" and selected_items[0][1] > food_capsules[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # MAGNETIC COMPASS
    elif selected_items[0][0] == "magnetic compass":
        print("The Moon does not have a magnetic field. I thought you were a trained professional??? Start over.")
        print("-----------------------")
        exit()
    # BOX OF MATCHES
    elif weight_limit >= 0 and selected_items[0][0] == "box of matches" and selected_items[0][1] <= box_of_matches[2]:
        weight_limit -= (int(quantity1) * box_of_matches[1])
        print("These are basically useless! Good job I guess.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "box of matches" and selected_items[0][1] > box_of_matches[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()   
    # STELLAR MAP
    elif weight_limit >= 0 and selected_items[0][0] == "stellar map" and selected_items[0][1] <= stellar_map[2]:
        weight_limit -= (int(quantity1) * stellar_map[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "stellar map" and selected_items[0][1] > stellar_map[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # ROPE
    elif weight_limit >= 0 and selected_items[0][0] == "50ft nylon rope" and selected_items[0][1] <= rope[2]:
        weight_limit -= (int(quantity1) * rope[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "50ft nylon rope" and selected_items[0][1] > rope[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FIRST AID KIT
    elif weight_limit >= 0 and selected_items[0][0] == "first aid kit" and selected_items[0][1] <= first_aid_kit[2]:
        weight_limit -= (int(quantity1) * first_aid_kit[1])
        print("Smart idea to prepare for the worst!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "first aid kit" and selected_items[0][1] > first_aid_kit[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PARACHUTE
    elif weight_limit >= 0 and selected_items[0][0] == "parachute silk" and selected_items[0][1] <= parachute[2]:
        weight_limit -= (int(quantity1) * parachute[1])
        print("This will help protect from dust and provide shelter. Nice!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "parachute silk" and selected_items[0][1] > parachute[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # LIFE RAFT
    elif weight_limit >= 0 and selected_items[0][0] == "life raft" and selected_items[0][1] <= life_raft[2]:
        weight_limit -= (int(quantity1) * life_raft[1])
        weight_limit += 50
        print("This will help you carry things and serve as protection. Good job! You increased your weight limit by 50 pounds.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == "life raft" and selected_items[0][1] > life_raft[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PISTOL
    elif weight_limit >= 0 and selected_items[0][0] == ".45 calibre pistol" and selected_items[0][1] <= pistol[2]:
        weight_limit -= (int(quantity1) * pistol[1])
        print("Someone's scared of aliens...")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[0][0] == ".45 calibre pistol" and selected_items[0][1] > pistol[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()

    print("-----------------------")
    if weight_limit < 0:
        print("You exceeded your weight limit! Please rethink and try again.")
        print("-----------------------")
        exit()
    print("-----------------------")
    print("-----------------------")
    item2, quantity2 = input("Choose your second item (enter the full item description, separated by a comma): ").split(",")
    selected_items.append([item2.strip(), int(quantity2.strip())])
    print("-----------------------")
    print("You've successfully chosen:")
    print("-----------------------")
    print(selected_items)
    print("-----------------------")

    # WATER
    if weight_limit >= 0 and selected_items[1][0] == "water" and selected_items[1][1] <= water[2]:
        weight_limit -= (int(quantity2) * water[1])
        print("Good choice! You're gonna get thirsty.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "water" and selected_items[1][1] > water[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FOOD CAPSULE PACK
    elif weight_limit >= 0 and selected_items[1][0] == "food capsule pack" and selected_items[1][1] <= food_capsules[2]:
        weight_limit -= (int(quantity2) * food_capsules[1])
        print("Good choice! You're gonna get hungry.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "food capsule pack" and selected_items[1][1] > food_capsules[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # MAGNETIC COMPASS
    elif selected_items[1][0] == "magnetic compass":
        print("The Moon does not have a magnetic field. I thought you were a trained professional??? Start over.")
        print("-----------------------")
        exit()
    # BOX OF MATCHES
    elif weight_limit >= 0 and selected_items[1][0] == "box of matches" and selected_items[1][1] <= box_of_matches[2]:
        weight_limit -= (int(quantity2) * box_of_matches[1])
        print("These are basically useless! Good job I guess.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "box of matches" and selected_items[1][1] > box_of_matches[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()   
    # STELLAR MAP
    elif weight_limit >= 0 and selected_items[1][0] == "stellar map" and selected_items[1][1] <= stellar_map[2]:
        weight_limit -= (int(quantity2) * stellar_map[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "stellar map" and selected_items[1][1] > stellar_map[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # ROPE
    elif weight_limit >= 0 and selected_items[1][0] == "50ft nylon rope" and selected_items[1][1] <= rope[2]:
        weight_limit -= (int(quantity2) * rope[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "50ft nylon rope" and selected_items[1][1] > rope[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FIRST AID KIT
    elif weight_limit >= 0 and selected_items[1][0] == "first aid kit" and selected_items[1][1] <= first_aid_kit[2]:
        weight_limit -= (int(quantity2) * first_aid_kit[1])
        print("Smart idea to prepare for the worst!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "first aid kit" and selected_items[1][1] > first_aid_kit[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PARACHUTE
    elif weight_limit >= 0 and selected_items[1][0] == "parachute silk" and selected_items[1][1] <= parachute[2]:
        weight_limit -= (int(quantity2) * parachute[1])
        print("This will help protect from dust and provide shelter. Nice!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "parachute silk" and selected_items[1][1] > parachute[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # LIFE RAFT
    elif weight_limit >= 0 and selected_items[1][0] == "life raft" and selected_items[1][1] <= life_raft[2]:
        weight_limit -= (int(quantity2) * life_raft[1])
        weight_limit += 50
        print("This will help you carry things and serve as protection. Good job! You increased your weight limit by 50 pounds.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == "life raft" and selected_items[1][1] > life_raft[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PISTOL
    elif weight_limit >= 0 and selected_items[1][0] == ".45 calibre pistol" and selected_items[1][1] <= pistol[2]:
        weight_limit -= (int(quantity2) * pistol[1])
        print("Someone's scared of aliens...")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[1][0] == ".45 calibre pistol" and selected_items[1][1] > pistol[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()

    print("-----------------------")
    if weight_limit < 0:
        print("You exceeded your weight limit! Please rethink and try again.")
        print("-----------------------")
        exit()
    print("-----------------------")
    print("-----------------------")
    item3, quantity3 = input("Choose your third item (enter the full item description, separated by a comma): ").split(",")
    selected_items.append([item3.strip(), int(quantity3.strip())])
    print("-----------------------")
    print("You've successfully chosen:")
    print("-----------------------")
    print(selected_items)
    print("-----------------------")
    
    # WATER
    if weight_limit >= 0 and selected_items[2][0] == "water" and selected_items[2][1] <= water[2]:
        weight_limit -= (int(quantity3) * water[1])
        print("Good choice! You're gonna get thirsty.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "water" and selected_items[2][1] > water[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FOOD CAPSULE PACK
    elif weight_limit >= 0 and selected_items[2][0] == "food capsule pack" and selected_items[2][1] <= food_capsules[2]:
        weight_limit -= (int(quantity3) * food_capsules[1])
        print("Good choice! You're gonna get hungry.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "food capsule pack" and selected_items[2][1] > food_capsules[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # MAGNETIC COMPASS
    elif selected_items[2][0] == "magnetic compass":
        print("The Moon does not have a magnetic field. I thought you were a trained professional??? Start over.")
        print("-----------------------")
        exit()
    # BOX OF MATCHES
    elif weight_limit >= 0 and selected_items[2][0] == "box of matches" and selected_items[2][1] <= box_of_matches[2]:
        weight_limit -= (int(quantity3) * box_of_matches[1])
        print("These are basically useless! Good job I guess.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "box of matches" and selected_items[2][1] > box_of_matches[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()   
    # STELLAR MAP
    elif weight_limit >= 0 and selected_items[2][0] == "stellar map" and selected_items[2][1] <= stellar_map[2]:
        weight_limit -= (int(quantity3) * stellar_map[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "stellar map" and selected_items[2][1] > stellar_map[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # ROPE
    elif weight_limit >= 0 and selected_items[2][0] == "50ft nylon rope" and selected_items[2][1] <= rope[2]:
        weight_limit -= (int(quantity3) * rope[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "50ft nylon rope" and selected_items[2][1] > rope[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FIRST AID KIT
    elif weight_limit >= 0 and selected_items[2][0] == "first aid kit" and selected_items[2][1] <= first_aid_kit[2]:
        weight_limit -= (int(quantity3) * first_aid_kit[1])
        print("Smart idea to prepare for the worst!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "first aid kit" and selected_items[2][1] > first_aid_kit[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PARACHUTE
    elif weight_limit >= 0 and selected_items[2][0] == "parachute silk" and selected_items[2][1] <= parachute[2]:
        weight_limit -= (int(quantity3) * parachute[1])
        print("This will help protect from dust and provide shelter. Nice!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "parachute silk" and selected_items[2][1] > parachute[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # LIFE RAFT
    elif weight_limit >= 0 and selected_items[2][0] == "life raft" and selected_items[2][1] <= life_raft[2]:
        weight_limit -= (int(quantity3) * life_raft[1])
        weight_limit += 50
        print("This will help you carry things and serve as protection. Good job! You increased your weight limit by 50 pounds.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == "life raft" and selected_items[2][1] > life_raft[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PISTOL
    elif weight_limit >= 0 and selected_items[2][0] == ".45 calibre pistol" and selected_items[2][1] <= pistol[2]:
        weight_limit -= (int(quantity3) * pistol[1])
        print("Someone's scared of aliens...")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[2][0] == ".45 calibre pistol" and selected_items[2][1] > pistol[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()

    print("-----------------------")
    if weight_limit < 0:
        print("You exceeded your weight limit! Please rethink and try again.")
        print("-----------------------")
        exit()
    print("-----------------------")
    print("-----------------------")
    item4, quantity4 = input("Choose your fourth item (enter the full item description, separated by a comma): ").split(",")
    selected_items.append([item4.strip(), int(quantity4.strip())])
    print("-----------------------")
    print("You've successfully chosen:")
    print("-----------------------")
    print(selected_items)
    print("-----------------------")
    
    # WATER
    if weight_limit >= 0 and selected_items[3][0] == "water" and selected_items[3][1] <= water[2]:
        weight_limit -= (int(quantity4) * water[1])
        print("Good choice! You're gonna get thirsty.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "water" and selected_items[3][1] > water[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FOOD CAPSULE PACK
    elif weight_limit >= 0 and selected_items[3][0] == "food capsule pack" and selected_items[3][1] <= food_capsules[2]:
        weight_limit -= (int(quantity4) * food_capsules[1])
        print("Good choice! You're gonna get hungry.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "food capsule pack" and selected_items[3][1] > food_capsules[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # MAGNETIC COMPASS
    elif selected_items[3][0] == "magnetic compass":
        print("The Moon does not have a magnetic field. I thought you were a trained professional??? Start over.")
        print("-----------------------")
        exit()
    # BOX OF MATCHES
    elif weight_limit >= 0 and selected_items[3][0] == "box of matches" and selected_items[3][1] <= box_of_matches[2]:
        weight_limit -= (int(quantity4) * box_of_matches[1])
        print("These are basically useless! Good job I guess.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "box of matches" and selected_items[3][1] > box_of_matches[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()   
    # STELLAR MAP
    elif weight_limit >= 0 and selected_items[3][0] == "stellar map" and selected_items[3][1] <= stellar_map[2]:
        weight_limit -= (int(quantity4) * stellar_map[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "stellar map" and selected_items[3][1] > stellar_map[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # ROPE
    elif weight_limit >= 0 and selected_items[3][0] == "50ft nylon rope" and selected_items[3][1] <= rope[2]:
        weight_limit -= (int(quantity4) * rope[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "50ft nylon rope" and selected_items[3][1] > rope[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FIRST AID KIT
    elif weight_limit >= 0 and selected_items[3][0] == "first aid kit" and selected_items[3][1] <= first_aid_kit[2]:
        weight_limit -= (int(quantity4) * first_aid_kit[1])
        print("Smart idea to prepare for the worst!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "first aid kit" and selected_items[3][1] > first_aid_kit[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PARACHUTE
    elif weight_limit >= 0 and selected_items[3][0] == "parachute silk" and selected_items[3][1] <= parachute[2]:
        weight_limit -= (int(quantity4) * parachute[1])
        print("This will help protect from dust and provide shelter. Nice!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "parachute silk" and selected_items[3][1] > parachute[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # LIFE RAFT
    elif weight_limit >= 0 and selected_items[3][0] == "life raft" and selected_items[3][1] <= life_raft[2]:
        weight_limit -= (int(quantity4) * life_raft[1])
        weight_limit += 50
        print("This will help you carry things and serve as protection. Good job! You increased your weight limit by 50 pounds.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == "life raft" and selected_items[3][1] > life_raft[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PISTOL
    elif weight_limit >= 0 and selected_items[3][0] == ".45 calibre pistol" and selected_items[3][1] <= pistol[2]:
        weight_limit -= (int(quantity4) * pistol[1])
        print("Someone's scared of aliens...")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[3][0] == ".45 calibre pistol" and selected_items[3][1] > pistol[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    
    print("-----------------------")
    if weight_limit < 0:
        print("You exceeded your weight limit! Please rethink and try again.")
        print("-----------------------")
        exit()
    print("-----------------------")
    print("-----------------------")
    item5, quantity5 = input("Choose your fifth and final item (enter the full item description, separated by a comma): ").split(",")
    logging.info(f"You selected all your items at {datetime.datetime.now()}")
    selected_items.append([item5.strip(), int(quantity5.strip())])
    print("-----------------------")
    print("You've successfully chosen:")
    print("-----------------------")
    print(selected_items)
    print("-----------------------")

    # WATER
    if weight_limit >= 0 and selected_items[4][0] == "water" and selected_items[4][1] <= water[2]:
        weight_limit -= (int(quantity5) * water[1])
        print("Good choice! You're gonna get thirsty.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "water" and selected_items[4][1] > water[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FOOD CAPSULE PACK
    elif weight_limit >= 0 and selected_items[4][0] == "food capsule pack" and selected_items[4][1] <= food_capsules[2]:
        weight_limit -= (int(quantity5) * food_capsules[1])
        print("Good choice! You're gonna get hungry.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "food capsule pack" and selected_items[4][1] > food_capsules[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # MAGNETIC COMPASS
    elif selected_items[4][0] == "magnetic compass":
        print("The Moon does not have a magnetic field. I thought you were a trained professional??? Start over.")
        print("-----------------------")
        exit()
    # BOX OF MATCHES
    elif weight_limit >= 0 and selected_items[4][0] == "box of matches" and selected_items[4][1] <= box_of_matches[2]:
        weight_limit -= (int(quantity5) * box_of_matches[1])
        print("These are basically useless! Good job I guess.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "box of matches" and selected_items[4][1] > box_of_matches[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()   
    # STELLAR MAP
    elif weight_limit >= 0 and selected_items[4][0] == "stellar map" and selected_items[4][1] <= stellar_map[2]:
        weight_limit -= (int(quantity5) * stellar_map[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "stellar map" and selected_items[4][1] > stellar_map[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # ROPE
    elif weight_limit >= 0 and selected_items[4][0] == "50ft nylon rope" and selected_items[4][1] <= rope[2]:
        weight_limit -= (int(quantity5) * rope[1])
        print("Amazing choice! You'll definitely need this.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "50ft nylon rope" and selected_items[4][1] > rope[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # FIRST AID KIT
    elif weight_limit >= 0 and selected_items[4][0] == "first aid kit" and selected_items[4][1] <= first_aid_kit[2]:
        weight_limit -= (int(quantity5) * first_aid_kit[1])
        print("Smart idea to prepare for the worst!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "first aid kit" and selected_items[4][1] > first_aid_kit[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PARACHUTE
    elif weight_limit >= 0 and selected_items[4][0] == "parachute silk" and selected_items[4][1] <= parachute[2]:
        weight_limit -= (int(quantity5) * parachute[1])
        print("This will help protect from dust and provide shelter. Nice!")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "parachute silk" and selected_items[4][1] > parachute[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # LIFE RAFT
    elif weight_limit >= 0 and selected_items[4][0] == "life raft" and selected_items[4][1] <= life_raft[2]:
        weight_limit -= (int(quantity5) * life_raft[1])
        weight_limit += 50
        print("This will help you carry things and serve as protection. Good job! You increased your weight limit by 50 pounds.")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == "life raft" and selected_items[4][1] > life_raft[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    # PISTOL
    elif weight_limit >= 0 and selected_items[4][0] == ".45 calibre pistol" and selected_items[4][1] <= pistol[2]:
        weight_limit -= (int(quantity5) * pistol[1])
        print("Someone's scared of aliens...")
        print("-----------------------")
        print("You have ", weight_limit, " pounds left.")
    elif selected_items[4][0] == ".45 calibre pistol" and selected_items[4][1] > pistol[2]:
        print("You cannot exceed the quantity limit. Please start over.")
        print("-----------------------")
        exit()
    print("-----------------------")
    print("All 5 items selected!")
    print("-----------------------")
    startJourney()

def start():
    print("-----------------------")
    print("-----------------------")
    print("Welcome to Moon Rescue!")
    print("-----------------------")
    print("-----------------------")
    print("You are an astronaut. You are flying to the Moon with your partner/monkey, Mr. Jingles, in order to deliver a new battery to NASA's Opportunity Mars and save him from dying.")
    print("-----------------------")
    print("However, during the landing phase, high-speed winds kick up and blow you way off-course. You are forced to land 100 miles South-East from base camp.")
    print("-----------------------")
    print("You do not have enough fuel to take off again AND be able to leave the Moon once the mission is completed.")
    print("-----------------------")
    print("Also, your all-terrain vehicle was damaged during landing, so you must travel by ground.")
    print("-----------------------")
    name = input("Let's start with your name: ")
    print("-----------------------")
    print("Good luck, " + name + " and Mr. Jingles! You'll need it.")
    print("-----------------------")
    logging.info(f"You started your journey at {datetime.datetime.now()}")
    selectItems()

if __name__ == "__main__":
    start()