from time import time
from mcts import mcts
# from copy import deepcopy
# from hash_table import HashTable
# from location import Location
from sokoban_state import State
# import math
# from heuristics import Heuristic
# import sys

'''
Executes Monte Carlo Tree Search (MCTS)
'''

def print_results(board, gen, rep, fri, expl, dur):
    print("\n2. Iterative Deepening A* Search (IDA*)")
    print("Solution: " + board.getDirections())
    print("Nodes generated: " + str(gen))
    print("Nodes repeated: " + str(rep))
    print("Fringe nodes: " + str(fri))
    print("Explored nodes: " + str(expl))
    print('Duration: ' + str(dur) + ' secs')

def do_mcts(board):
    # initialState = State()
    start = time()
    test = mcts(timeLimit=1000)
    bestAction = test.search(board)
    end = time()
    print_results(bestAction, 0, 0, 0, 0, end - start)