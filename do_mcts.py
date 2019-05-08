from time import time
from my_mcts import mcts
# from copy import deepcopy
# from hash_table import HashTable
# from location import Location
from sokoban_state import State
from time import time
from copy import deepcopy

import sokoban_game
import sys
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
    # start = time()
    test = mcts(timeLimit=50)
    bestAction = test.search(board)
    # print(bestAction)
    # end = time()
    # dur = end - start
    # print('Duration: ' + str(dur) + ' secs')
    # print_results(bestAction, 0, 0, 0, 0, end - start)
    return bestAction

def run(board):
    start = time()
    cpy = deepcopy(board)
    curr_time = start

    time_out = 120

    while (not cpy.is_win() or curr_time - start < time_out):
        print("MCTS iteration")
        action = do_mcts(cpy)
        cpy.move(action)
        print(str(action))
        curr_time = time()

    if (cpy.is_win):
        end = time()
        print_results(cpy, 0, 0, 0, 0, end - start)
        return cpy
    else:
        print("Results not found")
        sys.exit(1)