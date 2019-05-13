import os, sys, math, location
from location import Location
from direction import Direction

L = Direction(Location(-1, 0), 'l')
R = Direction(Location(1, 0), 'r')
U = Direction(Location(0, -1), 'u')
D = Direction(Location(0, 1), 'd')
DIRECTIONS = [U, D, L, R]

class State:
    TILE_BOX = '$'
    TILE_GOAL = '.'
    TILE_PLAYER = '@'
    TILE_SPACE = ' '
    TILE_WALL = '#'
    TILE_BLOCK_ON_GOAL = '*'
    TILE_PLAYER_ON_GOAL = '+'
    TILE_DEADLOCK = 'x'
    # TILE_PLAYER_ON_DEADLOCK = '+'

    def __init__(self, move_history):
        self.move_history = move_history
        self.full_board = []
        self.walls = []
        self.boxes = []
        self.goals = []
        self.fgoals = frozenset()
        self.fboxes = frozenset()  # since list is not hashable
        self.player = None
        self.spaces = []
        self.deadlocks = []
        self.cost = 1
        self.g_cost = 0
        self.f_cost = 0
        self.boxes_on_goal = []

    def __eq__(self, other):
        ''' Equality check by box positions and player positions '''
        if (self.player == other.player and all(elem in other.boxes for elem in self.boxes)):
            return True
        else:
            return False
    
    def __hash__(self):
        ''' hashes by frozenset of box positions '''
        return hash((self.fboxes, self.player))

    def __gt__(self, other):
        ''' Greater than, comparison by cost '''
        if self.cost > other.cost:
            return True
        else:
            return False

    def __lt__(self, other):
        ''' Less than, comparison by cost '''
        if self.cost < other.cost:
            return True
        else:
            return False

    def add_full_board(self, row):
        self.full_board.append(row)

    def add_wall(self, x, y):
        self.walls.append(Location(x, y))

    def add_goal(self, x, y):
        self.goals.append(Location(x, y))

    def add_box(self, x, y):
        self.boxes.append(Location(x, y))

    def add_space(self, x, y):
        self.spaces.append(Location(x, y))

    def set_player(self, x, y):
        self.player = Location(x, y)

    def add_static_deadlock(self, x, y, row_size, col_size):
        ''' Add deadlock based on the board alone, not including the dynamic deadlocks among boxes'''

        def _place_deadlock(x, delta_x, y, delta_y):
            # check whether a spot is in the wall corner
            try:
                if Location((x + delta_x), y) in self.walls and Location(x, (y + delta_y)) in self.walls:
                    self.deadlocks.append(Location(x, y))
                    return True
            except IndexError:
                pass
            return False
        
        _place_deadlock(x, -1, y, -1) or _place_deadlock(x, -1, y, 1) or \
        _place_deadlock(x, 1, y, -1) or _place_deadlock(x, 1, y, 1)
        
        def _dead_row(row_size, x, y):
            if (y == 1) or (y == row_size - 2):
                if Location(x, y) in self.spaces:
                    self.deadlocks.append(Location(x, y))
                    return True
                return False
            return False

        def _dead_col(col_size, x, y):
            if (x == 1) or (x == col_size - 2):
                if Location(x, y) in self.spaces:
                    self.deadlocks.append(Location(x, y))
                    return True
                return False
            return False

        _dead_row(row_size, x, y)
        _dead_col(col_size, x, y)

        # If goal is in dead_row or dead_col, remove it from deadlocks
        def _remove_deadlocks(x, y):
            for goal in self.goals:
                x_cord = Location.__x_cord__(goal)
                y_cord = Location.__y_cord__(goal)
                if Location(x, y) in self.deadlocks:
                    if (x == x_cord and (x == 1 or x == col_size - 2)) \
                        or (y == y_cord and (y == 1 or y == row_size -2)):
                        self.deadlocks.remove(Location(x, y))

        _remove_deadlocks(x, y)

    def moves_available(self):
        moves_available= []

        # This thing is slow, should be reverse back to a 2-d array representation?
        for d in DIRECTIONS:
            if self.player + d.location not in self.walls:
                if self.player + d.location in self.boxes:
                # Check if box can be pushed to next space
                    if self.player + d.location.space_past_box() not in self.boxes + self.walls + self.deadlocks:
                        moves_available.append(d)
                else:
                    moves_available.append(d)
        return moves_available

    # def moves_available1(self):
    #     moves_available= []

    #     # This thing is slow, should be reverse back to a 2-d array representation?
    #     for d in DIRECTIONS:
    #         # Box's current cordinates
    #         x_cord = Location.__x_cord__(self.player + d.location)
    #         y_cord = Location.__y_cord__(self.player + d.location)

    #         # Box's new cordinates
    #         new_x_cord = Location.__x_cord__(self.player + d.location.space_past_box())
    #         new_y_cord = Location.__y_cord__(self.player + d.location.space_past_box())
            
    #         if self.full_board[y_cord][x_cord] is not self.TILE_WALL:
    #             if self.full_board[y_cord][x_cord] is self.TILE_BOX:
    #                 # Check if box can be pushed to next space
    #                 if self.full_board[new_y_cord][new_x_cord] is not self.TILE_BOX + self.TILE_WALL + self.TILE_DEADLOCK:
    #                     moves_available.append(d)
    #             else:
    #                 moves_available.append(d)
    #     return moves_available

    def move(self, direction):
        ''' moves player and box '''
        player_new = self.player + direction.location
        box_new = self.player + direction.location.space_past_box()

        # This thing is slow, should be reverse back to a 2-d array representation?
        if player_new in self.boxes:
            self.boxes.remove(player_new)
            self.boxes.append(box_new)
        #     if box_new in self.spaces:
        #         self.boxes.append(box_new)
        #     elif box_new in self.goals:
        #         self.boxes_on_goal.append(box_new)
        #     else:
        #         print("WTF at ", player_new)
        #     # self.ucsCost = 2
        # self.spaces.append(self.player)
        self.player = player_new
        self.move_history.append(direction)

    def is_win(self):
        ''' Checks for winning/final state '''
        if all(elem in self.boxes for elem in self.goals):
            for elem in self.boxes:
                self.boxes_on_goal.append(elem)
            return True
        else:
            return False

    def getDirections(self):
        ''' Outputs the list of directions taken for the solution '''
        chars = ''
        for m in self.move_history:
            chars += m.character
            chars += '|'
        return chars

    '''
    # Heuristics 1 uses manhattan distance
    def calculateH1(self):
        manhattanD = 0

        boxLocations = []
        goalLocations = []

        for i in range(len(self.board)):
            # tempCoordinates = []
            for j in range(len(self.board[i])):
                if (self.board[i][j] == '$'):
                    boxLocations.append([i, j])
                if (self.board[i][j] == '.'):
                    goalLocations.append([i, j])
        # print(boxLocations)
        # print(goalLocations)
        
        manhattanD = math.fabs(boxLocations[0][0] - goalLocations[0][0]) + math.fabs(boxLocations[0][1] - goalLocations[0][1]) 

        return manhattanD
    '''