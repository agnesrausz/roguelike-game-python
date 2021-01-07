import random
import time
from util import clear_screen
from main import create_player

inventory = ['vaccine', 'vaccine', 'pill', 'pill', 'pill', 'toilet paper', 'instant soup','instant soup','instant soup','instant soup']

player = create_player()


#generating inventory as a dictionary for easier printing
def inventory_dictionary():
    collectable = ["💉","💊","🧼","🧻","🍜"]
    #counting the occurances in the inventory list
    sum_vaccine = inventory.count("vaccine")
    sum_pill = inventory.count("pill")
    sum_soap = inventory.count("soap")
    sum_tp = inventory.count("toilet paper")
    sum_instant = inventory.count("instant soup")
    #making the inventory dictionary
    inventory_with_values = {
        'vaccine': {
                    "icon": collectable[0],
                    "name": "vaccine",
                    "amount": sum_vaccine,
                    "description": "+15 health"
                    },
        'pill': {
                    "icon": collectable[1],
                    "name": "pill",
                    "amount": sum_pill,
                    "description": "+10 health"
                    },
        'soap': {
                    "icon": collectable[2],
                    "name": "soap",
                    "amount": sum_soap,
                    "description": "+5 health"
                    },
        'toilet paper': {
                    "icon": collectable[3],
                    "name": "toilet paper",
                    "amount": sum_tp,
                    "description": "ATK + 5"
                    },
        'instant soup': {
                    "icon": collectable[4],
                    "name": "instant soup",
                    "amount": sum_instant,
                    "description": "ATK +10"
                    }
    }
    return inventory_with_values

#printing inventory
def print_inventory():
    inventory_with_values = inventory_dictionary()
    print("********************************************************************")
    print("icon","\t","name","\t","\t","amount","","description")
    print("********************************************************************")
    print("",inventory_with_values["vaccine"]["icon"],"\t",inventory_with_values["vaccine"]["name"],"\t",inventory_with_values["vaccine"]["amount"],"\t",inventory_with_values["vaccine"]["description"],"\n",
          inventory_with_values["pill"]["icon"],"\t",inventory_with_values["pill"]["name"],"\t","\t",inventory_with_values["pill"]["amount"],"\t",inventory_with_values["pill"]["description"],"\n",
          inventory_with_values["soap"]["icon"],"\t",inventory_with_values["soap"]["name"],"\t","\t",inventory_with_values["soap"]["amount"],"\t",inventory_with_values["soap"]["description"],"\n",
          inventory_with_values["toilet paper"]["icon"],"\t",inventory_with_values["toilet paper"]["name"],"\t",inventory_with_values["toilet paper"]["amount"],"\t",inventory_with_values["toilet paper"]["description"],"\n",
          inventory_with_values["instant soup"]["icon"],"\t",inventory_with_values["instant soup"]["name"],"\t",inventory_with_values["instant soup"]["amount"],"\t",inventory_with_values["instant soup"]["description"])
    print("********************************************************************")

#using inventory
def use_inventory():
    item_names = inventory_dictionary()
    print_inventory()
    #checking user input
    used_item = input("What would you like to use? (press q to exit the inventory) ")
    if used_item == "q":
        print("You decided to not use anything.")
        exit

    elif used_item in item_names:

        if used_item == 'vaccine':

            if item_names["vaccine"]["amount"] > 0:
                print("You used one vaccine, with the effect:", item_names["vaccine"]["description"])
                inventory.remove('vaccine')
                #applying item effect
                player["Health"] = player["Health"] + 15
            else:
                print("You don't have any", used_item, "to use!")

        if used_item == 'pill':
            if item_names["pill"]["amount"] > 0:
                print("You used one", used_item, "with the effect:", item_names["pill"]["description"])
                inventory.remove('pill')
                #applying item effect
                player["Health"] = player["Health"] + 10
            else:
                print("You don't have any", used_item, "to use!")

        if used_item == 'soap':
            if item_names["soap"]["amount"] > 0:
                print("You used one", used_item, "with the effect:", item_names["soap"]["description"])
                inventory.remove('soap')
                #applying item effect
                player["Health"] = player["Health"] + 5
            else:
                print("You don't have any", used_item, "to use!")

        if used_item == 'toilet paper':
            if item_names["toilet paper"]["amount"] > 0:
                print("You used one", used_item, "with the effect:", item_names["toilet paper"]["description"])
                inventory.remove('toilet paper')
                #applying item effect
                player["Damage"] = player["Damage"] + 5
            else:
                print("You don't have any", used_item, "to use!")

        if used_item == 'instant soup':
            if item_names["instant soup"]["amount"] > 0:
                print("You used one", used_item, "with the effect:", item_names["instant soup"]["description"])
                inventory.remove('instant soup')
                #applying item effect
                player["Damage"] = player["Damage"] + 10
            else:
                print("You don't have any", used_item, "to use!")
    elif used_item not in item_names:
        print("You don't have such an item.")
    time.sleep(3.00)
    clear_screen()

def other_entities():
    mobs = {
        "enemy": {
                "Name": "coronavirus",
                "Type": "enemy",
                "Health": 10,
                "Damage": 2
                },

        "NPC": {
                "Name": "Karen mcHoax",
                "Type": "NPC"
                },

        "Boss": {
                "Name": "SARS CoVid 2055+++",
                "Type": "enemy",
                "Health": 100,
                "Damage": 50
        }

    }

    return mobs


def fight():
    enemy = other_entities()
    print("A wild %s appeared!"%enemy["enemy"]["Name"])
    print(enemy["enemy"]["Name"],"'s stats:\n", 
          "- health:", enemy["enemy"]["Health"],"\n",
          "- damage:", enemy["enemy"]["Damage"],"\n")
    print("Your stats: \n",
          "- health:", player["Health"],"\n",
          "- damage:", player["Damage"],"\n")

    alive = True
    health = enemy["enemy"]["Health"]
    player_health = player["Health"]
    while alive == True:
        print("What do you want to do?")
        print(" 1. fight \n 2. flee")
        hit = input(" ")

        if hit == "1":
            time.sleep(2.00)
            clear_screen()
            health = health - player["Damage"]
            player_health = player_health - enemy["enemy"]["Damage"]
            enemy["enemy"]["Health"] = health
            player["Health"] = player_health

            if health > 0 and player_health > 0:
                print(enemy["enemy"]["Name"],"'s health:", enemy["enemy"]["Health"])
                print("Your health:",player["Health"])

            if health <= 0:
                print("Enemy down, yay!")
                alive = False

            if player_health <= 0:
                print("You died, you absolute disgrace.")
                alive = False

        if hit == "2":
            print("Pussy :|")
            exit()

    time.sleep(3.00)
    clear_screen()



def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
