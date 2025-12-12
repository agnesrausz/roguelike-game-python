import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_COL = 3
PLAYER_START_ROW = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    """
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    """
    player = {
        "icon": PLAYER_ICON,
        "position": (PLAYER_START_ROW, PLAYER_START_COL)
    }
    return player


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key in ['w', 'a', 's', 'd']:
            engine.move_player(board, player, key)
        else:
            pass

        util.clear_screen()


if __name__ == '__main__':
    main()
