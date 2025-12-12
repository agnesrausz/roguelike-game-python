import random


def create_board(width, height):
    """
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    """
    board = []

    # Create empty board
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(" ")
        board.append(row)

    # Add walls around the edges
    for col in range(width):
        board[0][col] = "#"  # Top wall
        board[height - 1][col] = "#"  # Bottom wall

    for row in range(height):
        board[row][0] = "#"  # Left wall
        board[row][width - 1] = "#"  # Right wall

    # Add gates
    board[random.randint(1, height - 2)][0] = "G"  # Start gate
    board[random.randint(1, height - 2)][width - 1] = "G"  # End gate

    return board


def put_player_on_board(board, player):
    """
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    """
    row, col = player["position"]
    board[row][col] = player["icon"]


def remove_player_from_board(board, player):
    """
    Modifies the game board by removing the player icon from its previous coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    """
    row, col = player["position"]
    board[row][col] = " "


def move_player(board, player, key):
    """
    Modifies the player coordinates based on the input key.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates
    str: The input key

    Returns:
    Nothing
    """
    remove_player_from_board(board, player)
    row, col = player["position"]
    new_row, new_col = row, col

    if key == 'w':
        new_row -= 1
    elif key == 's':
        new_row += 1
    elif key == 'a':
        new_col -= 1
    elif key == 'd':
        new_col += 1

    # Check for out-of-bounds
    if new_row >= len(board) or new_col >= len(board[0]) or new_row < 0 or new_col < 0:
        return

    # Check for wall collision
    if board[new_row][new_col] != "#":
        player["position"] = (new_row, new_col)
