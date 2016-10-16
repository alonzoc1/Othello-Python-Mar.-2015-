#Alonzo Castanon 94339018

import tkinter
import othello

class OptionPicker:
    '''OptionPicker is a class that opens a window with drop down options required to set up
    an othello board. When the button is pressed, it stores the values and closes the window'''
    def __init__(self):
        self._values = None
        row_or_column_oplist = ('4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14' , '15', '16')
        first_or_corner_oplist = ('black','white')
        win_oplist = ('most','fewest')
        self._root_window = tkinter.Tk()
        self._row_value = tkinter.StringVar()
        self._row_value.set(row_or_column_oplist[0])
        self._row = tkinter.OptionMenu(self._root_window, self._row_value, *row_or_column_oplist)
        self._column_value = tkinter.StringVar()
        self._column_value.set(row_or_column_oplist[0])
        self._column = tkinter.OptionMenu(self._root_window, self._column_value, *row_or_column_oplist)
        self._first_value = tkinter.StringVar()
        self._first_value.set(first_or_corner_oplist[0])
        self._first = tkinter.OptionMenu(self._root_window, self._first_value, *first_or_corner_oplist)
        self._corner_value = tkinter.StringVar()
        self._corner_value.set(first_or_corner_oplist[0])
        self._corner = tkinter.OptionMenu(self._root_window, self._corner_value, *first_or_corner_oplist)
        self._win_value = tkinter.StringVar()
        self._win_value.set(win_oplist[0])
        self._win = tkinter.OptionMenu(self._root_window, self._win_value, *win_oplist)
        self._ready = tkinter.Button(self._root_window, font = ('Calibri','12'), text = 'Start!',
                                     command=self.clicked)

        self._row_desc = tkinter.Label(self._root_window, font= ('Calibri', 12),
                                          text='How many rows? ', justify = 'left')
        self._column_desc = tkinter.Label(self._root_window, font= ('Calibri', 12),
                                          text='How many columns? ', justify = 'left')
        self._first_desc = tkinter.Label(self._root_window, font= ('Calibri', 12),
                                          text='What color goes first? ', justify = 'left')
        self._corner_desc = tkinter.Label(self._root_window, font= ('Calibri', 12),
                                          text='What color in top left? ', justify = 'left')
        self._win_desc = tkinter.Label(self._root_window, font= ('Calibri', 12),
                                          text='Most or fewest pieces win? ', justify = 'left')

        self._row_desc.grid(row = 0, column = 0, padx = 1, pady = 1,
                            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._column_desc.grid(row = 1, column = 0, padx = 1, pady = 1,
                            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._first_desc.grid(row = 2, column = 0, padx = 1, pady = 1,
                            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._corner_desc.grid(row = 3, column = 0, padx = 1, pady = 1,
                            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._win_desc.grid(row = 4, column = 0, padx = 1, pady = 1,
                            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._ready.grid(row = 5, column = 0, padx = 1, pady = 1,
                         sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._row.grid(row = 0, column = 1, padx = 1, pady = 1,
                       sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._column.grid(row = 1, column = 1, padx = 1, pady = 1,
                       sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._first.grid(row = 2, column = 1, padx = 1, pady = 1,
                       sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._corner.grid(row = 3, column = 1, padx = 1, pady = 1,
                       sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._win.grid(row = 4, column = 1, padx = 1, pady = 1,
                       sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

    def clicked(self):
        '''sets self._values to the values that were inputted, and closes the window'''
        self._values = self.values()
        self._destroy_window()
        
    def values(self):
        '''returns the inputted values'''
        return (self._row_value.get(),self._column_value.get(),
               self._first_value.get(), self._corner_value.get(), self._win_value.get())
    def _destroy_window(self):
        '''closes the window'''
        self._root_window.destroy()

    def start(self):
        self._root_window.mainloop()


class GameState:
    def __init__(self, disk_list):
        self._disk_list = disk_list
        self._board_x = len(self._disk_list)
        self._board_y = len(self._disk_list[0])
        

                
    def get_board_size(self):
        '''Returns the size of the board in a tuple, (x,y) (as in, a 14 by 8 board, or a 6 by 6 board)'''
        return (self._board_x, self._board_y)

    def get_disk_locations(self):
        return self._disk_list
        

class Board:
    '''Board handles the GUI aspect and communicates with othello to confirm moves are ok'''
    def __init__(self, state: othello.othello_gamestate):
        self._state = state
        self._root_window = tkinter.Tk()
        self._white_score_value = 2
        self._black_score_value = 2
        self._turn_ticker = state.whose_turn()
        if self._turn_ticker == 'black':
            self._black_bg = '#DAD246'
            self._white_bg = '#FFFFFF'
        if self._turn_ticker == 'white':
            self._white_bg = '#DAD246'
            self._black_bg = '#FFFFFF'
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 800, height = 700, background = '#605FAA')
        self._white_score = tkinter.Label(self._root_window, font= ('Calibri', 16),
                                          text='White = '+str(self._white_score_value),
                                          justify = 'left',bg = self._white_bg)
        self._black_score = tkinter.Label(self._root_window, font= ('Calibri', 16),
                                          text='Black = '+str(self._black_score_value),
                                          justify = 'left',bg = self._black_bg)
        self._draw_lines(800, 700, state.columns_and_rows())
        self._draw_disks(800, 700, state.columns_and_rows(), state.game_board())
        self._canvas.grid(
            row = 0, column = 0, padx = 1, pady = 1,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._white_score.grid(
            row = 1, column = 0, padx = 1, pady= 1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._black_score.grid(
            row = 2, column = 0, padx = 1, pady= 1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas.bind('<Configure>', self._on_resize)
        self._canvas.bind('<Button-1>', self._on_click)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._last_click = (0,0)

    def start(self):
        self._root_window.mainloop()

    def refresh(self, turn, white_score, black_score, winner):
        '''redraws the score'''
        self._white_score_value = white_score
        self._black_score_value = black_score
        self._turn_ticker = turn
        if self._turn_ticker == 'black':
            self._black_bg = '#DAD246'
            self._white_bg = '#FFFFFF'
        if self._turn_ticker == 'white':
            self._white_bg = '#DAD246'
            self._black_bg = '#FFFFFF'
        if winner == 'black':
            self._black_bg = '#DAD246'
            self._white_bg = '#FFFFFF'
            self._black_score_value = 'Winner! '+str(black_score)
        if winner == 'white':
            self._white_bg = '#DAD246'
            self._black_bg = '#FFFFFF'
            self._white_score_value = "Winner! "+str(white_score)
        if winner == 'tie':
            self._white_bg = 'green'
            self._black_bg = 'green'
            self._white_score_value = "Tie!? "+str(white_score)
            self._black_score_value = "Tie?! "+str(black_score)
        self._white_score = tkinter.Label(self._root_window, font= ('Calibri', 16),
                                          text='White = '+str(self._white_score_value),
                                          justify = 'left',bg = self._white_bg)
        self._black_score = tkinter.Label(self._root_window, font= ('Calibri', 16),
                                          text='Black = '+str(self._black_score_value),
                                          justify = 'left',bg = self._black_bg)
        self._white_score.grid(
            row = 1, column = 0, padx = 1, pady= 1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._black_score.grid(
            row = 2, column = 0, padx = 1, pady= 1, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        

    def _draw_lines(self, canvas_width, canvas_height, board_size):
        '''draws the lines in the event of resizing (or on boot)'''
        column_spacing = int(canvas_width/board_size[0])
        row_spacing = int(canvas_height/board_size[1])
        column_ticker = column_spacing
        row_ticker = row_spacing
        for line in range(board_size[0]):
            self._canvas.create_line(column_ticker, 0, column_ticker, canvas_height, width = 2)
            column_ticker += column_spacing
        for line in range(board_size[1]):
            self._canvas.create_line(0, row_ticker, canvas_width, row_ticker, width = 2)
            row_ticker += row_spacing

    def _draw_disks(self, canvas_width, canvas_height, board_size, disk_list):
        '''draws the disks in the event of resizing, or change in board (or on boot)'''
        box_size = (int(canvas_width/board_size[0]),int(canvas_height/board_size[1]))
        disk_size = (box_size[0]*.9,box_size[1]*.9)
        disk_locales = []
        for column in range(len(disk_list)):
            for cell in range(len(disk_list[column])):
                if disk_list[column][cell] == 'b':
                    disk_locales.append((column,cell,'b'))
                if disk_list[column][cell] == 'w':
                    disk_locales.append((column,cell,'w'))
        for disk in disk_locales:
            x_orig = disk[0]*box_size[0]
            y_orig = disk[1]*box_size[1]
            x_orig += int((box_size[0]-disk_size[0])/2)
            y_orig += int((box_size[1]-disk_size[1])/2)
            x_new = x_orig + disk_size[0]
            y_new = y_orig + disk_size[1]

            if disk[2] == 'w':
                self._canvas.create_oval(x_orig, y_orig, x_new, y_new, fill = 'white')
            if disk[2] == 'b':
                self._canvas.create_oval(x_orig, y_orig, x_new, y_new, fill = 'black')

    def _redraw(self):
        '''uses the two previously defined draw functions to redraw the canvas'''
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self._draw_lines(canvas_width, canvas_height, self._state.columns_and_rows())
        self._draw_disks(canvas_width, canvas_height, self._state.columns_and_rows(),self._state.game_board())
        
    def _on_resize(self, event: tkinter.Event):
        '''calls the redraw function when window is resized'''
        self._redraw()

    def _on_click(self, event: tkinter.Event):
        '''tries to do a move whenever a click happens. First verifies the move is legal, then does it'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        click = (event.x, event.y, width, height)
        self._last_click = self._handle_click(click)
        coords = self._conv_index_to_coord(self._last_click[0],self._last_click[1])
        if self._state.is_valid(coords[0],coords[1],self._turn_ticker):
            self._state.make_move(coords[0],coords[1], self._turn_ticker)
            self._redraw()
            self._turn_ticker = self._state.turn_switch()
            score = self._state.score_count()
            self.refresh(self._turn_ticker,score[0],score[1],self._state.check_win())
            if self._state.check_win() == None:
                if self._turn_ticker == 'white':
                    if self._state.check_white_moves() == False:
                        self._turn_ticker = 'black'
                        self.refresh(self._turn_ticker,score[0],score[1],self._state.check_win())
                elif self._turn_ticker == 'black':
                    if self._state.check_black_moves() == False:
                        self._turn_ticker = 'white'
                        self.refresh(self._turn_ticker,score[0],score[1],self._state.check_win())

    def _conv_index_to_coord(self, x, y):
        '''converts the list indexes to coordinates (which the othello module prefers to use)'''
        return ((x+1),abs(((y-self._state.columns_and_rows()[1]))))
    
    def _handle_click(self, click):
        '''turns a click pixel coordinate into a tuple with the indexes of the cell'''
        pix_x = click[0]
        pix_y = click[1]
        canvas_x = click[2]
        canvas_y = click[3]
        column_spacing = canvas_x/self._state.columns_and_rows()[0]
        row_spacing = canvas_y/self._state.columns_and_rows()[1]
        column_ticker = column_spacing
        row_ticker = row_spacing
        x_index_ticker = 0
        y_index_ticker = 0
        while column_ticker <= canvas_x:
            if pix_x <= column_ticker:
                break
            else:
                column_ticker += column_spacing
                x_index_ticker += 1
        while row_ticker <= canvas_y:
            if pix_y <= row_ticker:
                break
            else:
                row_ticker += row_spacing
                y_index_ticker += 1
        return (x_index_ticker, y_index_ticker)
