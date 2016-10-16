# Alonzo Castanon 94339018

class othello_gamestate:
    def __init__(self, columns, rows, start_color, top_left_color, win_cond):
        try:
            self._columns = int(columns)
        except:
            raise InitialSetupError('Column not a valid integer')
        try:
            self._rows = int(rows)
        except:
            raise InitialSetupError('Row not a valid integer')
        if start_color in ['white','black']:
            self._start_color = start_color
        else:
            raise InitialSetupError('Starting player color not matching "white" or "black"')
        if top_left_color in ['white','black']:
            self._top_left_color = top_left_color #The self._start_color is also going to function
                                                  #as a turn tracker, saying whose turn it is.
        else:
            raise InitialSetupError('Top left color not matching "white" or "black"')
        if win_cond in ['most','fewest']:
            self._win_cond = win_cond
        else:
            raise InitialSetupError('Win condition not matching "most" or "fewest"')
        if self._columns <= 3:
            raise InitialSetupError('Column is less than 4! Must be 4 or greater.')
        if self._columns <= 3:
            raise InitialSetupError("Row is less than 4! Must be 4 or greater.")
        self._game_board = []
        # Game board is going to be a nested list as follows:
        # 1st level is going to represent columns. Each list inside of the main list
        # is going to be a different column.
        # 2nd level is going to represent individual cells. The first object in the list
        # is the cell in the first row, etc...
        for column in range(self._columns):
            row = []
            for cell in range(self._rows):
                row.append('')
            self._game_board.append(row)
        top_left_pos = [int(self._columns/2)-1,int(self._rows/2-1)]
        self._game_board[top_left_pos[0]][top_left_pos[1]+1] = self._top_left_color[0]
        self._game_board[top_left_pos[0]+1][top_left_pos[1]] = self._top_left_color[0]
        if self._top_left_color[0] == 'w':
             self._game_board[top_left_pos[0]+1][top_left_pos[1]+1] = 'b'
             self._game_board[top_left_pos[0]][top_left_pos[1]] = 'b'
        elif self._top_left_color[0] == 'b':
             self._game_board[top_left_pos[0]+1][top_left_pos[1]+1] = 'w'
             self._game_board[top_left_pos[0]][top_left_pos[1]] = 'w'
        
    def columns_and_rows(self):
        '''Returns a list of two integers, the number of columns followed by the number of
        rows'''
        return [self._columns,self._rows]

    def whose_turn(self):
        '''Returns a string that is either 'black' or 'white' describing whose turn it is'''
        return self._start_color

    def check_win(self):
        '''Returns 'white' if white won, 'black' if black won, and None if there is no winner yet
        ALSO returns 'tie' if there are no moves left, but the score is equal'''
        if othello_gamestate.check_black_moves(self) == True:
            return None
        if othello_gamestate.check_white_moves(self) == True:
            return None
        score = othello_gamestate.score_count(self)
        if self._win_cond == 'most':
            if score[0] > score[1]:
                return 'white'
            if score[1] > score[0]:
                return 'black'
            if score[0] == score[1]:
                return 'tie'
        elif self._win_cond == 'fewest':
            if score[0] < score[1]:
                return 'white'
            if score[1] < score[0]:
                return 'black'
            if score[0] == score[1]:
                return 'tie'
    def check_black_moves(self):
        max_x = self._columns
        max_y = self._rows
        while max_y != 0:
            while max_x != 0:
                if othello_gamestate.is_valid(self, max_x, max_y, 'black') == True:
                    return True
                max_x = max_x - 1
            max_x = self._columns
            max_y = max_y - 1
        return False

    def turn_switch(self):
        '''switches self._start color to the opposite one, then returns the new color'''
        if self._start_color == 'white':
            self._start_color = 'black'
        elif self._start_color == 'black':
            self._start_color = 'white'
        return self._start_color

    def check_white_moves(self):
        max_x = self._columns
        max_y = self._rows
        while max_y != 0:
            while max_x != 0:
                if othello_gamestate.is_valid(self, max_x, max_y, 'white') == True:
                    return True
                max_x = max_x - 1
            max_x = self._columns
            max_y = max_y - 1
        return False

    def _get_adjacent(self, column_index, row_index)->list:
        '''Takes in the index numbers of the middle cell, and returns a list of
        strings that say either 'b' or 'w', depending on what color disk is on
        the cell. If there is no disk, the value of the list object is None'''
        try:
            check_left = True
            check_right = True
            check_bottom = True
            check_top = True
            check_top_left = True
            check_bottom_left = True
            check_top_right = True
            check_bottom_right = True
            if column_index == 0:
                check_left = False
            if row_index == 0:
                check_top = False
            if (column_index) == (self._columns-1):
                check_right = False
            if (row_index) == (self._rows-1):
                check_bottom = False
            if check_left == False:
                check_top_left = False
                check_bottom_left = False
            if check_right == False:
                check_top_right = False
                check_bottom_right = False
            if check_top == False:
                check_top_right = False
                check_top_left = False
            if check_bottom == False:
                check_bottom_left = False
                check_bottom_right = False
            left_cell = None
            right_cell = None
            top_cell = None
            bottom_cell = None
            top_left_cell = None
            bottom_left_cell = None
            top_right_cell = None
            bottom_right_cell = None
            if check_left == True:
                left_cell = self._game_board[column_index-1][row_index]
            if check_right == True:
                right_cell = self._game_board[column_index+1][row_index]
            if check_top == True:
                top_cell = self._game_board[column_index][row_index-1]
            if check_bottom == True:
                bottom_cell = self._game_board[column_index][row_index+1]
            if check_top_left == True:
                top_left_cell = self._game_board[column_index-1][row_index-1]
            if check_top_right == True:
                top_right_cell = self._game_board[column_index+1][row_index-1]
            if check_bottom_left == True:
                bottom_left_cell = self._game_board[column_index-1][row_index+1]
            if check_bottom_right == True:
                bottom_right_cell = self._game_board[column_index+1][row_index+1]
            cell_list = [left_cell, right_cell, top_cell, bottom_cell, top_left_cell,
                         bottom_left_cell, top_right_cell, bottom_right_cell]
            for cell in range(len(cell_list)):
                if cell_list[cell] == '':
                    cell_list[cell] = None
            return cell_list
        except:
            raise WrongInputError('Index out of range')
    def is_valid(self, x, y, color):
        '''Returns True if valid move, False if invalid move. Takes in
        coordinates the such as 1,1 or 8,8. Takes in a color of the move,
        a string that is either 'black' or 'white' '''
        indexes = othello_gamestate._convert_coord_to_index(self,x,y)
        column_index = indexes[0]
        row_index = indexes[1]
        try:
            if self._game_board[column_index][row_index] in ['w','b']:
                return False
        except:
            return False

        cell_list = othello_gamestate._get_adjacent(self, column_index, row_index)
        if color == 'black':
            if 'w' not in cell_list:
                return False
            else:
                for j in range(len(cell_list)):
                    if cell_list[j] == 'w':
                        pair = None
                        if j == 0:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'left', color)
                        if j == 1:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'right', color)
                        if j == 2:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'top', color)
                        if j == 3:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'bottom', color)
                        if j == 4:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'top_left', color)
                        if j == 5:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'bottom_left', color)
                        if j == 6:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'top_right', color)
                        if j == 7:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'bottom_right', color)
                        if pair != None:
                            return True
                return False
        if color == 'white':
            if 'b' not in cell_list:
                return False
            else:
                for j in range(len(cell_list)):
                    if cell_list[j] == 'b':
                        pair = None
                        if j == 0:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'left', color)
                        if j == 1:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'right', color)
                        if j == 2:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'top', color)
                        if j == 3:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'bottom', color)
                        if j == 4:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'top_left', color)
                        if j == 5:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'bottom_left', color)
                        if j == 6:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'top_right', color)
                        if j == 7:
                            pair = othello_gamestate._search_for_pair(self, column_index, row_index, 'bottom_right', color)
                        if pair != None:
                            return True
                return False
        else:
            raise WrongInputError('"black or white" color input not detected')

    def _search_for_pair(self, column_index, row_index, direction, color):
        '''searches for a same color disk in the direction indicated (not including
        adjacent) and returns a list of the index for the pair, or None if not found'''
        directions = ['top','bottom','left','right','top_left','bottom_left',
                      'top_right','bottom_right']
        if direction not in directions:
            raise WrongInputError('Direction is not in',directions)
        if direction == 'top':
            if (row_index - 2) < 0:
                return None
        if direction == 'bottom':
            if (row_index + 2) > (self._rows-1):
                return None
        if direction == 'left':
            if (column_index - 2) < 0:
                return None
        if direction == 'right':
            if (column_index + 2) > (self._columns-1):
                return None
        if direction == 'top_left':
            if (row_index - 2) < 0:
                return None
            if (column_index - 2) < 0:
                return None
        if direction == 'bottom_left':
            if (row_index + 2) > (self._rows-1):
                return None
            if (column_index - 2) < 0:
                return None
        if direction == 'top_right':
            if (row_index - 2) < 0:
                return None
            if (column_index + 2) > (self._columns-1):
                return None
        if direction == 'bottom_right':
            if (row_index + 2) > (self._rows-1):
                return None
            if (column_index + 2) > (self._columns-1):
                return None
        try:
            if direction == 'top':
                row_index = row_index - 2
                while True:
                    if row_index < 0:
                        raise InternalError()
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    row_index = row_index - 1
            if direction == 'bottom':
                row_index = row_index + 2
                while True:
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    row_index = row_index + 1
            if direction == 'left':
                column_index = column_index - 2
                while True:
                    if column_index < 0:
                        raise InternalError()
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    column_index = column_index - 1
            if direction == 'right':
                column_index = column_index + 2
                while True:
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    column_index = column_index + 1
            if direction == 'top_left':
                row_index = row_index - 2
                column_index = column_index - 2
                while True:
                    if row_index < 0:
                        raise InternalError()
                    if column_index < 0:
                        raise InternalError()
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    row_index -= 1
                    column_index -= 1
            if direction == 'bottom_left':
                column_index = column_index - 2
                row_index = row_index + 2
                while True:
                    if column_index < 0:
                        raise InternalError()
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    row_index += 1
                    column_index -= 1
            if direction == 'top_right':
                row_index = row_index - 2
                column_index = column_index + 2
                while True:
                    if row_index < 0:
                        raise InternalError()
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    column_index += 1
                    row_index -= 1
            if direction == 'bottom_right':
                row_index = row_index + 2
                column_index = column_index + 2
                while True:
                    if self._game_board[column_index][row_index] == color[0]:
                        return [column_index, row_index, direction]
                    elif self._game_board[column_index][row_index] == '':
                        return None
                    row_index += 1
                    column_index += 1
        except:
            return None
    def _convert_coord_to_index(self, x, y):
        column_index = (x - 1)
        row_index = int(abs(y - self._rows))
        return [column_index,row_index]

    def make_move(self, x, y, color):
        if othello_gamestate.is_valid(self, x, y, color) == False:
            raise WrongInputError('Invalid move!')
        indexes = othello_gamestate._convert_coord_to_index(self, x, y)
        adjacent_cells = othello_gamestate._get_adjacent(self, indexes[0], indexes[1])
        poss_directions = ['left','right','top','bottom','top_left','bottom_left','top_right','bottom_right']
        directions = []
        for cell_number in range(len(adjacent_cells)):
            if adjacent_cells[cell_number] != None:
                directions.append(poss_directions[cell_number])
        pair_indexes_raw = []
        for direction in directions:
            pair_indexes_raw.append(othello_gamestate._search_for_pair(self, indexes[0], indexes[1], direction, color[0]))
        pair_indexes = []
        for g in pair_indexes_raw:
            if g != None:
                pair_indexes.append(g)
        flip = [indexes]
        for h in pair_indexes:
            if h[2] == 'top':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_row != target_row:
                    current_row -= 1
                    flip.append([current_column,current_row])
            if h[2] == 'bottom':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_row != target_row:
                    current_row += 1
                    flip.append([current_column,current_row])
            if h[2] == 'left':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_column != target_column:
                    current_column -= 1
                    flip.append([current_column,current_row])
            if h[2] == 'right':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_column != target_column:
                    current_column += 1
                    flip.append([current_column,current_row])
            if h[2] == 'top_left':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_column != target_column:
                    current_column -= 1
                    current_row -= 1
                    flip.append([current_column,current_row])
            if h[2] == 'bottom_left':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_column != target_column:
                    current_column -= 1
                    current_row += 1
                    flip.append([current_column,current_row])
            if h[2] == 'top_right':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_column != target_column:
                    current_column += 1
                    current_row -= 1
                    flip.append([current_column,current_row])
            if h[2] == 'bottom_right':
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                index_list = othello_gamestate._strip_direction(self, h)
                target_column = index_list[0]
                target_row = index_list[1]
                current_column = indexes[0]
                current_row = indexes[1]
                while current_column != target_column:
                    current_column += 1
                    current_row += 1
                    flip.append([current_column,current_row])
        othello_gamestate._flip_disk(self, flip, color)

    def _flip_disk(self, flip, color):
        for i in flip:
            self._game_board[i[0]][i[1]] = color[0]
                    
    def _strip_direction(self, index_list):
        '''removes the direction string object from the index list'''
        return [index_list[0],index_list[1]]
        

    def game_board(self):
        '''Returns the gameboard nested list'''
        return self._game_board
        
    def score_count(self):
        '''Returns a list of two integers, first one is how many disks white has, second is how many
        disks black has'''
        w = 0
        b = 0
        for column in self._game_board:
            for row in column:
                if row == 'w':
                    w += 1
                if row == 'b':
                    b += 1
        return [w,b]

class InitialSetupError(Exception):
    pass

class WrongInputError(Exception):
    pass

class InternalError(Exception):
    pass
