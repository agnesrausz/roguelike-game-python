import random


def create_board(width, height):
    border = "🌳"
    fill = "🎋"
    board = []
    obstacle = "🗻"
    obstacle_counter = 0
    obstacle_max = (width * height) // 100 * 15
    board.append(border * width)
    for i in range(height - 2):
        board.append(border + (fill * (width - 2)) + border)
    board.append(border * width)
    random_line_index = 0
    random_row_index = 0
    while obstacle_counter != obstacle_max:
        random_line_index = random.randint(1, height - 2)
        random_row_index = random.randint(1, width - 2)
        if board[random_line_index][random_row_index] != obstacle:
            board[random_line_index] = list(board[random_line_index])
            board[random_line_index][random_row_index] = obstacle
            board[random_line_index] = "".join((board[random_line_index]))
            obstacle_counter += 1
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
