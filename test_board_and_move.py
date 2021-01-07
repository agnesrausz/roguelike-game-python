import random


def create_rectangle(width=4, height=6, border_color="🟫", fill_color="⬛", border_width=1):
    board = []
    for h in range(height):
        board.append([])
        for w in range(width):
            if h < border_width or h > height-border_width-1:
                board[h].append(border_color)
            else:
                if w < border_width or w >= width-border_width:
                    board[h].append(border_color)
                else:
                    board[h].append(fill_color)
    # creat wall
    return board


def create_board(width=30, height=20):
    #  creat rectangle board
    board = create_rectangle(width, height, border_color="🟫", fill_color="🟫")
    start_end_place_grund = create_rectangle(4, 4, border_color="⬛", fill_color="⬛")
    #  creat start end ground
    rectangle_place_to_board(board, start_end_place_grund, 1, 1)
    rectangle_place_to_board(board, start_end_place_grund, height-5, width-5)
    #  creat reach start-end
    rectangle_place_to_board(board, create_rectangle(1, height-2, border_color="⬛", fill_color="⬛"), 1, 1)
    rectangle_place_to_board(board, create_rectangle(width-2, 1, border_color="⬛", fill_color="⬛"), 1, 1)
    rectangle_place_to_board(board, create_rectangle(width-2, 1, border_color="⬛", fill_color="⬛"), height-2, 1)
    rectangle_place_to_board(board, create_rectangle(1, height-2, border_color="⬛", fill_color="⬛"), 1, width-2)
    # random elem ground
    elem_quantity = width // 5
    while elem_quantity:
        try:
            rectangle_place_to_board(board, 
                                    (create_rectangle(  random.randint(3, 5), 
                                                        random.randint(3, 5), 
                                                        border_color="⬛", 
                                                        fill_color="⬛")), 
                                    random.randint(1, height-6), 
                                    random.randint(1, width-6))
            elem_quantity -= 1
        except IndexError:
            continue
    elem_quantity = 7 + height // 5
    while elem_quantity:
        try:
            rectangle_place_to_board(board, 
                                    (create_rectangle(  1, 
                                                        random.randint(8, 12), 
                                                        border_color="⬛", 
                                                        fill_color="⬛")), 
                                    random.randint(1, height-8), 
                                    random.randint(1, width-8))
            elem_quantity -= 1
        except IndexError:
            continue
    elem_quantity = 7 + width // 5
    while elem_quantity:
        try:
            rectangle_place_to_board(board, 
                                    (create_rectangle(  random.randint(8, 12), 
                                                        1, 
                                                        border_color="⬛", 
                                                        fill_color="⬛")), 
                                    random.randint(1, height-8), 
                                    random.randint(1, width-8))
            elem_quantity -= 1
        except IndexError:
            continue
    # correct border
    rectangle_place_to_board(board, create_rectangle(width, 1, border_color="🟫", fill_color="🟫"), height-1, 0)
    rectangle_place_to_board(board, create_rectangle(1, height, border_color="🟫", fill_color="🟫"), 0, width-1)
    # creat gate
    board[height-4][width-1] = "⛩️"
    return board


def rectangle_place_to_board(board, rectangle, place_row, place_col):
    for row in range(len(rectangle)):
        for col in range(len(rectangle[row])):
            board[row + place_row][col + place_col] = rectangle[row][col]


def creat_grund_elem(elem_quantity, board, rectangle, place_row=random.randint(1, 29), place_col=random.randint(1, 29)):
    while elem_quantity:
        try:
            rectangle_place_to_board(board, rectangle, place_row, place_col)
            elem_quantity -= 1
        except IndexError:
            continue


def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()
    print()


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    player_coord_stand = ""
    for row in board:
        try:
            player_coord_stand = board.index(row), row.index(player["icon"])
        except ValueError:
            pass
    for row in range(len(board)):
        for col in range(len(board[row])):
            if player["coord"][0] == row and player["coord"][1] == col:
                field = board[row][col]

    if field == "🟫":
        return None
    elif field == "⬛":
        item = None
    elif field == "💉":
        item = "💉"

    print(player_coord_stand)
    print(field)
    board[player_coord_stand[0]][player_coord_stand[1]] = "⬛"
    x = player["coord"][0]
    y = player["coord"][1]
    board[y][x] = player["icon"]
    return item


player = {"icon": "🦦", "coord": (2, 2)}
board = create_board()
display_board(board)
board[1][1] = "🦦"
display_board(board)
put_player_on_board(board, player)
display_board(board)