import os
import sys
import math

# Hi Yangzi!
class sokoBoard:
    # TILE_BLOCK = '$'
    # TILE_GOAL = '.'
    # TILE_PLAYER = '@'
    # TILE_SPACE = ' '
    # TILE_WALL = '#'
    # TILE_BLOCK_ON_GOAL = '*'
    # TILE_PLAYER_ON_GOAL = '!'
    # TILE_DEADLOCK = 'x'
    # TILE_PLAYER_ON_DEADLOCK = '+'

    # Given no input generate most basic board
    # Otherwise, 
    def __init__(self, filename = None):
        self.board = []
        self.h1Val = None

        self.moves = []
        self.boxPositions = []

        if filename:
            # Work with specific boardmap
            pass
        else:
            # Generic board
            for i in range(6):
                temp = []
                for j in range(6):
                    if (i == 0 or i == 5):
                        temp.append('#')
                    elif (j == 0 or j == 5):
                        temp.append('#')
                    else: 
                        temp.append(' ')
                self.board.append(temp)
                
            
            # player starting position
            self.board[3][3] = '@'

            # Box starting position
            self.board[2][2] = '$'

            # Goal position
            self.board[4][4] = '.'

    # def initPuzzle(board, player):
    #     self.board = board
    #     self.player = player

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

    def readFile(self, filename):
        sokomap = open(filename, "r")
            

        # call initPuzzle
    
    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # temp = temp + 
                print(self.board[i][j], end = "")
            print()

def main():
   test = sokoBoard()
   print(test.calculateH1())
   test.printBoard()
        

if __name__ == "__main__":
    main()