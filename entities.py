import ui

PLAYER_START_COL = 3
PLAYER_START_ROW = 3


def create_player():
    """
    Creates a 'player' dictionary for storing all player related information - i.e. player icon, player position.

    Returns:
    dictionary
    """
    player = {
        "icon": ui.PLAYER_ICON,
        "position": (PLAYER_START_ROW, PLAYER_START_COL),
        "inventory": []
    }
    return player


def create_item(type):
    """
    Creates an item dictionary for storing item related information - i.e. item icon, item position.

    Returns:
    dictionary
    """
    item = {
        "icon": ui.ITEM_ICON,
        "position": (5, 5),
        "name": "Health Potion"
    }
    return item
