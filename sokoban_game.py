import bfs
from sokoban_state import State


class Sokoban:

    def new_game(self, filename):
        ''' Creates new Sokoban game from specified file '''
        move_list = []
        new_board = State(move_list)

        with open(filename, 'r') as f:
            reader = f.read()
            lines = reader.split('\n')
            x = 0
            y = 0

            for line in lines:
                for char in line:
                    if char == '#':
                        new_board.add_wall(x, y)
                    elif char == '.':
                        new_board.add_goal(x, y)
                    elif char == '@':
                        new_board.set_player(x, y)
                    elif char == '+':
                        new_board.set_player(x, y)
                        new_board.add_goal(x, y)
                    elif char == '$':
                        new_board.add_box(x, y)
                    elif char == '*':
                        new_board.add_box(x, y)
                        new_board.add_goal(x, y)
                    x += 1
                y += 1
                x = 0
            return new_board
            # if hasattr(b, 'player'):
            #     return b
            # else:
            #     print "No player on board"
            #     return None    
    def search(self, board, mode):
        if mode == 1:
            bfs.search(board)
            # pass
        if mode == 2:
            # dfs.search(board)
            pass
        if mode == 3:
            # ucs.search(board)
            pass
        if mode == 4:
            # gbfs.search(board)
            pass
        if mode == 5:
            # ass.search(board)
            pass
        if mode == 6:  # all get executed
            # bfs.search(board)
            # dfs.search(board)
            # ucs.search(board)
            # gbfs.search(board)
            # ass.search(board)
            pass