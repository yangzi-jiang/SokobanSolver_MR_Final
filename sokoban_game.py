import bfs
from sokoban_state import State
from location import Location

class Sokoban:

    def __init__(self):
        self.col_size = 0
        self.row_size = 0

    def new_game(self, filename):
        ''' Creates new Sokoban game from specified file '''
        move_list = []
        new_board = State(move_list)

        with open(filename, 'r') as f:
            reader = f.read()
            lines = reader.split('\n')
            x = 0
            y= 0

            # x is column, and yis row
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
                    elif char == ' ':
                        new_board.add_space(x, y)
                    x += 1
                    self.col_size = x
                y+= 1
                x = 0
                self.row_size = y            
            # Adding static deadlocks after building the walls
            x = 0
            y= 0
            for line in lines:
                for char in line:
                    if char == '@' or char == ' ':
                        # Check deadlocks here
                        new_board.add_static_deadlock(x, y)
                    x += 1
                y+= 1
                x = 0

        return new_board
            # if hasattr(b, 'player'):
            #     return b
            # else:
            #     print "No player on board"
            #     return None    

    def search(self, board, mode):
        if mode == 1:
            return bfs.search(board)
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

    def print_board_lists(self, board):
        print('Walls Locations:')
        print(*board.walls)
        print('Boxes Locations:')
        print(*board.boxes)
        print('Fboxes Locations:')
        print(*board.fboxes)
        print('Player Locations:')
        print(board.player)
        print('Spaces Locations:')
        print(*board.spaces)
        print('Deadlocks Locations:')
        print(*board.deadlocks)
        print('Goal Locations')
        print(*board.goals)

    def print_board(self, board):
        b = [None] * (self.col_size * self.row_size)

        for element in board.walls:
            x = Location.__x_cord__(element)
            y = Location.__y_cord__(element)
            b[x*self.col_size + y]= '#'

        for element in board.goals:
            x = Location.__x_cord__(element)
            y= Location.__y_cord__(element)
            b[x*self.col_size + y]= '.'

        for element in board.boxes:
            x = Location.__x_cord__(element)
            y= Location.__y_cord__(element)
            b[x*self.col_size + y]= '$'
        
        for element in board.spaces:
            x = Location.__x_cord__(element)
            y= Location.__y_cord__(element)
            b[x*self.col_size + y]= ' '
        
        for element in board.deadlocks:
            x = Location.__x_cord__(element)
            y = Location.__y_cord__(element)
            b[x*self.col_size + y]= 'X'
        
        x = Location.__x_cord__(board.player)
        y = Location.__y_cord__(board.player)
        b[x*self.col_size + y]= '@'

        print(self.row_size, self.col_size)

        for row in range(self.row_size):
            for col in range(self.col_size):
                print(b[row + col * (self.col_size)], end = "")
            print()