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
                "Name:": "Tyson",
                "Race:": "Bodybuilder male-nurse",
                "Type:": "Warrior",
                "Health:": "10",
                "Damage:": "3",
                "Special ability:": "Pumps 2 times with his chest muscles, creating a resonating wave, dealing 2 extra damage."
    }
    not_crazy_scientist = {
                "Name:": "Cili",
                "Race:": "Consistent female orator",
                "Type:": "Mage",
                "Health:": "7",
                "Damage:": "5",
                "Special ability:": "Asks her opponent to only attack if her opponent can win, makes her opponent confused, granting Cili an extra turn"
    }
    pali_gyorfi = {
                "Name:": "Pal Gyorfi",
                "Race:": "Makes you stay at home kind of man",
                "Type:": "Archer",
                "Health:": "5",
                "Damage:": "5",
                "Special ability:": "Asks his opponent to go home, so Pal can evade the fight."
    }
    op_char = {
                "Name:": "Achilles Lakatos",
                "Race:": "Definitely not c-type",
                "Type:": "Rogue",
                "Health:": "999",
                "Damage:": "999",
                "Special ability:": "Makes 3 exact copy of himself during daytime, at nighttime makes 10 copy."
    }
    util.clear_screen()
    print("Please select a character!")
    print("1")
    for key, value in male_nurse.items():
        print(key, value)
    print("\n2")
    for key, value in not_crazy_scientist.items():
        print(key, value)
    print("\n3")
    for key, value in pali_gyorfi.items():
        print(key, value)
    print("\n4 (Can only be chosen If you can enter the correct cheat code!)")
    for key, value in op_char.items():
        print(key, value)
    choice = input("\nEnter the selected character's number(1-4)!")
    if choice == "1":
        return male_nurse
        util.clear_screen()
    elif choice == "2":
        return not_crazy_scientist
        util.clear_screen()
    elif choice == "3":
        return pali_gyorfi
        util.clear_screen()
    elif choice == "4":
        cheatcode = ""
        while cheatcode != "nincs egy cigid?" or cheatcode != "q":
            cheatcode = input("Provide the correct cheat code to continue, or press q to return!")
            if cheatcode == "nincs egy cigid?":
                return op_char
            if cheatcode == "q":
                create_player()    
    else:
        util.clear_screen()
        print("That wasn't an option")
        create_player()


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
