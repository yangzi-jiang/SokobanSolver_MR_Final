from time import time
from copy import deepcopy
from hash_table import HashTable
from location import Location
from sokoban_state import State
import math
import heuristics

FOUND = -1
NOT_FOUND = -2

'''
Executes Iterative Deepening A* (IDA*)
'''

class IDA:

    # Global variables, would be helpful to keep them class level
    path = ""
    node = None
    g = -1
    f = -1

    @staticmethod
    def h(board):
        return heuristics.get_heuristics(board)

    @staticmethod
    def costFrom(board, successor):
        pass

    @staticmethod
    def successors(board):
        return board.moves_available()
    
    @staticmethod
    def is_goal(board):
        return True

    @staticmethod
    def ida_star(board):
        # Bookkeeping
        start = time()
        nodes_generated = 0
        nodes_repeated = 0

        # Create copy of og board to modify
        node = deepcopy(board)
        nodes_generated += 1

        bound = IDA.h(board)
        path = [root]

        while (True):
            t = IDA.search(path, 0, bound)
            if (t == FOUND):
                return FOUND
            if (t == math.inf):
                return NOT_FOUND
            bound = t

    @staticmethod
    def search(path, g, bound):
        node = path.last
        f = g + IDA.h(node)
        if (f > bound):
            return f
        if (IDA.is_goal(node)):
            print("Solution found")
            return FOUND
        
        min = math.inf
        for succ in IDA.successors(node):
            if (succ not in path):
                path.append(succ)
                t = IDA.search(path, g + IDA.costFrom(node, succ), bound)
                if (t == FOUND):
                    FOUND
                if (t < min):
                    min = t
                path.pop()
        return min