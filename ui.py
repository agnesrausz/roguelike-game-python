def display_board(board):
    for row in board:
        for col in row:
            print(col, end='')
        print()
    print()
