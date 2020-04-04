def print_board(board):
    print(f'\n\n\n\n\n\n\n'
          f' {board[7]} | {board[8]} | {board[9]} \n'
          f'---+---+---\n'
          f' {board[4]} | {board[5]} | {board[6]} \n'
          f'---+---+---\n'
          f' {board[1]} | {board[2]} | {board[3]} \n')


def board_setup():
    return {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}


def count_moves(board):

    board_items = board.values()
    moves = 0

    for item in board_items:
        if item == 'X' or item == 'O':
            moves +=1

    return moves s


def user_move(board):
    user_move = input('Enter number (1-9):  ')

    #asks for an number between 1 and 9
    while(user_move not in '123456789' or user_move == '' or board[int(user_move)] != ' '):
        user_move = input('Enter number (1-9):  ')


    moves_done = count_moves(board)

    #even number of moves means its X player's move
    if moves_done % 2 == 0:
        board[int(user_move)] = 'X'
    else:
        board[int(user_move)] = 'O'

    return board


def win_check(board):
    wining_patterns =[ [1,4,7], [2,5,8], [3,6,9],
                       [1,2,3], [4,5,6], [7,8,9],
                       [1,5,9], [3,5,7] ]

    for pattern in wining_patterns:
        board_pattern_extract = ''

        for board_key in pattern:
            board_pattern_extract += board[board_key]

        if 'OOO' in board_pattern_extract or 'XXX' in board_pattern_extract:
            return True
    else:
        return False


def user_decision():
    decision = input('Do you want to play again? (Y/N): ').lower()

    while (decision != 'y' and decision != 'n') or decision == '':
        decision = input('Do you want to play again? (Y/N): ').lower()

    return decision


#game board initialization
game_board = {}
game_board = board_setup()

#game loop
while True:

    print_board(game_board)

    #takes current game_board and returns the one updated with user's move
    game_board = user_move(game_board)

    game_won = win_check(game_board)

    if game_won == True:
        print_board(game_board)
        print('You have won :)')

        if user_decision() == 'n':
            break
        else:
            game_board = board_setup()

    if count_moves(game_board) == 10 and not game_won:
        print('Nobody won! Do you want to play again? (Y/N): ')

        if user_decision() == 'n':
            break
        else:
            game_board = board_setup()
