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
    def h(node):
        return heuristics.get_heuristics()

    @staticmethod
    def cost(node, successor):
        pass

    @staticmethod
    def successors(node):
        temp_list = []
        return temp_list
    
    @staticmethod
    def is_goal(node):
        return True

    @staticmethod
    def ida_star(root):
        bound = IDA.h(root)
        path = [root]
        t = 0

        while (t != math.inf):
            t = IDA.search(path, 0, bound)
            if (t== FOUND):
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
            return FOUND
        
        min = math.inf
        for succ in IDA.successors(node):
            if (succ not in path):
                path.append(succ)
                t = IDA.search(path, g + IDA.cost(node, succ), bound)
                if (t == FOUND):
                    FOUND
                if (t < min):
                    min = t
                path.pop()
        return min