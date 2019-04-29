import os, sys, math, location
from location import Location
from direction import Direction

L = Direction(Location(-1, 0), 'l')
R = Direction(Location(1, 0), 'r')
U = Direction(Location(0, -1), 'u')
D = Direction(Location(0, 1), 'd')
DIRECTIONS = [U, D, L, R]

class State:
    # TILE_BLOCK = '$'
    # TILE_GOAL = '.'
    # TILE_PLAYER = '@'
    # TILE_SPACE = ' '
    # TILE_WALL = '#'
    # TILE_BLOCK_ON_GOAL = '*'
    # TILE_PLAYER_ON_GOAL = '!'
    # TILE_DEADLOCK = 'x'
    # TILE_PLAYER_ON_DEADLOCK = '+'

    def __init__(self, move_list):
        self.move_list = move_list

        self.walls = []
        self.boxes = []
        self.goals = []
        self.player = None
        self.cost = 1

    def __eq__(self, other):
        ''' Equality check by box positions and player positions '''
        if (self.player == other.player and all(elem in other.boxes for elem in self.boxes)):
            return True
        else:
            return False
    
    def __hash__(self):
        ''' hashes by frozenset of box positions '''
        return hash(self.boxes, self.player)

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

    def add_wall(self, x, y):
        self.walls.append(Location(x, y))

    def add_goal(self, x, y):
        self.goals.append(Location(x, y))

    def add_box(self, x, y):
        self.boxes.append(Location(x, y))

    def set_player(self, x, y):
        self.player = Location(x, y)

    def moves_available(self):
        moves = []
        for d in DIRECTIONS:
            if self.player + d.location not in self.walls:
                if self.player + d.location in self.boxes:
                # Check if box can be pushed to next space
                    if self.player + d.location.space_past_box() not in (self.boxes + self.walls):
                        moves.append(d)
                else:
                    moves.append(d)
        return moves

    def move(self, direction):
        ''' moves player and box '''
        p = self.player + direction.location
        if p in self.boxes:
            self.boxes.remove(p)
            self.boxes.append(p + direction.sp)
            # self.ucsCost = 2
        self.player = p
        self.move_list.append(direction)

    def is_win(self):
        ''' Checks for winning/final state '''
        if all(elem in self.boxes for elem in self.goals):
            return True
        else:
            return False

    def getDirections(self):
        ''' Outputs the list of directions taken for the solution '''
        chars = ''
        for m in self.move_list:
            chars += m.character
            chars += ', '
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
    
    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # temp = temp + 
                print(self.board[i][j], end = "")
            print()
    '''

# def main():
#    test = sokoBoard()
#    print(test.calculateH1())
#    test.printBoard()
        

# if __name__ == "__main__":
#     main()