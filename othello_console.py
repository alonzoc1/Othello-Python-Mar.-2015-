#Alonzo Castanon 94339018
import othello

def print_board(game_object):
    game_board = game_object.game_board()
    row_ticker = (game_object.columns_and_rows()[1] - 9)
    for i in range(len(game_board[0])):
        line2 = ''
        line = ''
        if row_ticker > 0:
            line += (str((len(game_board[0])-i)) + ' ')
        else:
            line += (str((len(game_board[0])-i)) + '  ')
            line2 = ' '
        row_ticker = row_ticker - 1
        for y in game_board:
            if y[i] == '':
                line = line + '[ ]'
            else:
                if y[i] == 'b':
                    line = line + '[' + 'B' + ']'
                elif y[i] == 'w':
                    line = line + '[' + 'W' + ']'
        print(line)
    columns = len(game_board)
    for z in range(columns):
        if (z+1) >= 10:
            line2 += (str(z+1)+' ')
        else:
            line2 += (' '+str(z+1)+' ')
        line3 = '  ' + line2
    print(line3)
    print()

def print_score(score_list):
    print('White: '+str(score_list[0]))
    print('Black: '+str(score_list[1]))
    print()

def create_game(columns, rows, first, corner, win):
    return othello.othello_gamestate(columns, rows, first, corner, win)

def core_program():
    while True:
        try:
            rows = int(input('How many rows do you want on the board? (4-16): '))
        except:
            print("That doesn't look like an integer. Please try again.")
            continue
        if rows < 4:
            print("That value is less than 4. Please try again.")
            continue
        if rows > 16:
            print("That value is more than 16. Please try again.")
            continue
        break
    while True:
        try:
            columns = int(input('How many columns do you want on the board? (4-16): '))
        except:
            print("That doesn't look like an integer. Please try again.")
            continue
        if columns < 4:
            print("That value is less than 4. Please try again.")
            continue
        if columns > 16:
            print("That value is more than 16. Please try again.")
            continue
        break
    color_list = ['black','white']
    while True:
        start = str(input('Which color should go first? (black or white): '))
        if start not in color_list:
            print("Be sure you type in either 'black' or 'white' with no punctuation. Please try again.")
            continue
        break
    while True:
        corner_disk = str(input('Which color should be in the top left position? (black or white): '))
        if corner_disk not in color_list:
            print("Be sure you type in either 'black' or 'white' with no punctuation. Please try again.")
            continue
        break
    while True:
        win_cond = str(input('Should the player with most pieces left or fewest pieces left at the end of the game win? (most or fewest): '))
        if win_cond not in ['most','fewest']:
            print("Be sure you type in either 'most' or 'fewest' without punctuation. Please try again.")
            continue
        break
    print()
    print('The game will now begin \n')
    if corner_disk == 'white':
        patch = 'black'
    if corner_disk == 'black':
        patch = 'white'
    game = create_game(columns, rows, start, patch, win_cond)
    turn_ticker = start[0]
    while True:
        print_board(game)
        print_score(game.score_count())
        winner = game.check_win()
        if winner == 'white':
            print('White wins!')
            break
        if winner == 'black':
            print('Black wins!')
            break
        if winner == 'tie':
            print("It's a tie!")
            break
        if turn_ticker[0] == 'b':
            print("Black's turn\n")
            if game.check_black_moves() == False:
                print('\nBut Black has no possible moves! Skipping to White...\n')
                turn_ticker = 'w'
                continue
        if turn_ticker[0] == 'w':
            print("White's turn\n")
            if game.check_white_moves() == False:
                print('\nBut White has no possible moves! Skipping to Black...\n')
                turn_ticker = 'b'
                continue

        while True:
            if turn_ticker[0] == 'b':
                turn = 'black'
            if turn_ticker[0] == 'w':
                turn = 'white'
            try:
                move_col = int(input('Enter the number of the column you would like to place your piece: '))
            except:
                print("That doesn't look like a valid integer. Please try again.")
                continue
            try:
                move_row = input('Enter the number of the row you would like to place your piece OR type "cancel" to enter your column again: ')
                if move_row == 'cancel':
                    print()
                    continue
                move_row = int(move_row)
            except:
                print("That doesn't look like a valid integer or 'cancel'. Please try again.")
                continue
            if game.is_valid(move_col,move_row, turn) != True:
                print("That doesn't look like a valid move. Please try again.")
                continue
            break
        game.make_move(move_col,move_row, turn)
        turn_ticker = game.turn_switch()
    print('Game over!')
            
if __name__ == '__main__':
    core_program()
