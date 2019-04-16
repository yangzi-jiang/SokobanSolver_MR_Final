import os
import sys

# Hi Yangzi!
class sokoBoard:

    def __init__(self):
        self.board = []
        self.heuristicCost = 0
        self.functionCost = 0
        self.pathCost = 0

        self.moves = []

    def initPuzzle(board, player):
        self.board = board
        self.player = player

    def readFile(filename):
        sokomap = open(filename, "r")
            

        # call initPuzzle