import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    male_nurse = {
                "Name": "Tyson",
                "Race": "Bodybuilder male-nurse",
                "Type": "Warrior",
                "Health": "10",
                "Damage": "3",
    }
    not_crazy_scientist = {
                "Name": "Cili",
                "Race": "Consistent female orator",
                "Type": "Mage",
                "Health": "7",
                "Damage": "5"
    }
    pali_gyorfi = {
                "Name": "Pal Gyorfi",
                "Race": "Make you stay at home kind of man",
                "Type": "Archer",
                "Health": "5",
                "Damage": "5"
    }
    op_char = {
                "Name": "Achilles Lakatos",
                "Race": "Definitely not c-type",
                "Type": "Rogue",
                "Health": "999",
                "Damage": "999"
    }


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
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
