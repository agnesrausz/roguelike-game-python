def create_board(width, height):
    border = "🌳"
    fill = "🎋"
    board = []
    board.append(border * width)
    for i in range(height - 2):
        board.append(border + (fill * (width - 2)) + border)
    board.append(border * width)
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
