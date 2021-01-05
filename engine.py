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
