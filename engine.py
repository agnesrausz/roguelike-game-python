import random


def create_board(width=30, height=20):
    board = []
    # icon section
    border = "🌳"
    fill = "🎋"
    collectable = "💉"
    obstacle = "🗻"
    enemy = "🧬"
    player = "🦦"
    # icon section
    # counter section
    enemy_counter = 0
    obstacle_counter = 0
    collectable_counter = 0
    # counter section
    # max section
    collectable_max = 2
    obstacle_max = (width * height) // 100 * 15
    enemy_max = (width * height) // 100 * 2
    # max section
    board.append(border * width)
    for i in range(height - 2):
        board.append(border + (fill * (width - 2)) + border)
    board.append(border * width)
    random_line_index = 0
    random_row_index = 0
    # this section fills the board with obstacles
    while obstacle_counter != obstacle_max:
        random_line_index = random.randint(1, height - 2)
        random_row_index = random.randint(1, width - 2)
        if board[random_line_index][random_row_index] != obstacle:
            board[random_line_index] = list(board[random_line_index])
            board[random_line_index][random_row_index] = obstacle
            board[random_line_index] = "".join((board[random_line_index]))
            obstacle_counter += 1
    # this section fills the board with collectables
    while collectable_max > collectable_counter:
        random_line_index = random.randint(1, height - 2)
        random_row_index = random.randint(1, width - 2)
        if board[random_line_index][random_row_index] != obstacle:
            board[random_line_index] = list(board[random_line_index])
            board[random_line_index][random_row_index] = collectable
            board[random_line_index] = "".join((board[random_line_index]))
            collectable_counter += 1
    # this section fills the board with enemies
    while enemy_max > enemy_counter:
        random_line_index = random.randint(1, height - 2)
        random_row_index = random.randint(1, width - 2)
        if board[random_line_index][random_row_index] != obstacle and board[random_line_index][random_row_index] != collectable:
            board[random_line_index] = list(board[random_line_index])
            board[random_line_index][random_row_index] = enemy
            board[random_line_index] = "".join((board[random_line_index]))
            enemy_counter += 1
    # this section places the player
    board[2] = list(board[2])
    board[2][2] = player
    board[2] = "".join(board[2])
    return board

def inventory():
    #generating inventory
    board = create_board()
    inventory = []
    collectable = ["💉","💊","🧼","🧻","🍜"]
    #filling the inventory list with the name of the items
    for index in range(len(board)):
        for index_2 in range(len(board)):
            if board[index][index_2] == collectable[0]:
                inventory.append("vaccine")
            elif board[index][index_2]  == collectable[1]:
                inventory.append("pill")
            elif board[index][index_2]  == collectable[2]:
                inventory.append("soap")
            elif board[index][index_2]  == collectable[3]:
                inventory.append("toilet paper")
            elif board[index][index_2]  == collectable[4]:
                inventory.append("instant soup")
    return inventory

def inventory_dictionary():
    #printing inventory
    inv = inventory()
    collectable = ["💉","💊","🧼","🧻","🍜"]
    #counting the occurances in the inventory list
    sum_vaccine = inv.count("vaccine")
    sum_pill = inv.count("pill")
    sum_soap = inv.count("soap")
    sum_tp = inv.count("toilet paper")
    sum_instant = inv.count("instant soup")
    #making the inventory dictionary
    inventory_with_values = {
        'vaccine': {
                    "icon": collectable[0],
                    "name": "vaccine",
                    "amount": sum_vaccine,
                    "description": "gives you +50 health"
                    },
        'pill': {
                    "icon": collectable[1],
                    "name": "pill",
                    "amount": sum_pill,
                    "description": "gives you +10 health"
                    },
        'soap': {
                    "icon": collectable[2],
                    "name": "soap",
                    "amount": sum_soap,
                    "description": "grants immunity for 2 rounds"
                    },
        'tp': {
                    "icon": collectable[3],
                    "name": "toilet paper",
                    "amount": sum_tp,
                    "description": "grants immunity for 1 round"
                    },
        'instant soup': {
                    "icon": collectable[4],
                    "name": "instant soup",
                    "amount": sum_instant,
                    "description": "ATK +50"
                    }
    }
    return inventory_with_values

def print_inventory():
    inventory_with_values = inventory_dictionary()
    print("********************************************************************")
    print("icon","\t","name","\t","\t","amount","","description")
    print("********************************************************************")
    print("",inventory_with_values["vaccine"]["icon"],"\t",inventory_with_values["vaccine"]["name"],"\t",inventory_with_values["vaccine"]["amount"],"\t",inventory_with_values["vaccine"]["description"],"\n",
          inventory_with_values["pill"]["icon"],"\t",inventory_with_values["pill"]["name"],"\t","\t",inventory_with_values["pill"]["amount"],"\t",inventory_with_values["pill"]["description"],"\n",
          inventory_with_values["soap"]["icon"],"\t",inventory_with_values["soap"]["name"],"\t","\t",inventory_with_values["soap"]["amount"],"\t",inventory_with_values["soap"]["description"],"\n",
          inventory_with_values["tp"]["icon"],"\t",inventory_with_values["tp"]["name"],"\t",inventory_with_values["tp"]["amount"],"\t",inventory_with_values["tp"]["description"],"\n",
          inventory_with_values["instant soup"]["icon"],"\t",inventory_with_values["instant soup"]["name"],"\t",inventory_with_values["instant soup"]["amount"],"\t",inventory_with_values["instant soup"]["description"])
    print("********************************************************************")
    
def enemies():
    health = 20
    enemy = {
        "name": "coronavirus",
        "type": "enemy",
        "health": health
    }
    print(enemy["name"], enemy["type"], enemy["health"])
    print("A wild %s appeared!"%enemy["name"])
    enemy_alive = True
    while enemy_alive == True:
        hit = input("hit ")
        if hit == "hit":
            health = health - 10
            enemy["health"] = health
            print(enemy["name"], enemy["type"], enemy["health"])
            if health == 0:
                print("Enemy down, yay!")
                enemy_alive = False

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
