# Alonzo Castanon 94339018
import othello
import othello_gui


def options_gui():
    '''Opens the options window and retrieves values when user finishes inputting'''
    quick = OptionInterpret(othello_gui.OptionPicker())
    options = quick.get_value_tuple()
    if options[3][0] == 'w':
        patch = 'black'
    if options[3][0] == 'b':
        patch = 'white'
    return (options[0],options[1],options[2],patch,options[4])

def core_program():
    '''Creates the board and starts the game'''
    options = options_gui()
    game = othello.othello_gamestate(options[0],options[1],options[2],options[3],options[4])
    board_gui = BoardInterpret(othello_gui.Board(game))
    board_gui.start()
    
    
class OptionInterpret:
    '''Allows this module to access data in the other module'''
    def __init__(self, option_obj: othello_gui.OptionPicker):
        self._OptionPicker = option_obj
        self._OptionPicker.start()
        self._values = self._OptionPicker.values()

    def get_value_tuple(self):
        return self._values

class BoardInterpret:
    '''Just meant to give the code a cleaner aesthetic'''
    def __init__(self, board_obj: othello_gui.Board):
        self._board = board_obj

    def start(self):
        self._board.start()

if __name__ == '__main__':
    core_program()
