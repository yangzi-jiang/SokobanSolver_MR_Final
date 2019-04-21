import os
import sys

# Hi Yangzi!
class sokoBoard:


    # Given no input generate most basic board
    # Otherwise, 
    def __init__(self, filename = None):
        self.board = []
        self.heuristicCost = 0
        self.functionCost = 0
        self.pathCost = 0

        self.moves = []

    # def initPuzzle(board, player):
    #     self.board = board
    #     self.player = player

    def readFile(self, filename):
        sokomap = open(filename, "r")
            

        # call initPuzzle