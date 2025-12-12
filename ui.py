import os


def display_board(board):
    """
    Displays complete game board on the screen

    Returns:
    Nothing
    """
    for row in board:
        print("".join(row))


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
