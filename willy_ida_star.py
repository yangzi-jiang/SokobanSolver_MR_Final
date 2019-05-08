from time import time
from copy import deepcopy
from hash_table import HashTable
from location import Location
from sokoban_state import State
import math
from heuristics import Heuristic
import sys

FOUND = -1
NOT_FOUND = -2

'''
Executes Iterative Deepening A* (IDA*)
'''

def print_results(board, gen, rep, fri, expl, dur):
    print("\n2. Iterative Deepening A* Search (IDA*)")
    print("Solution: " + board.getDirections())
    print("Nodes generated: " + str(gen))
    print("Nodes repeated: " + str(rep))
    print("Fringe nodes: " + str(fri))
    print("Explored nodes: " + str(expl))
    print('Duration: ' + str(dur) + ' secs')

def h(board):
    h = Heuristic()
    return h.get_heuristics(board)

def successors(board):
    moves = board.moves_available()
    succ_list = []

    for step in moves:
        cpy = deepcopy(board)
        cpy.move(step)
        succ_list.append(cpy)

    return succ_list

def isClosed(closedSet, x):
    for y in closedSet:
        if x == y:
            return True
    return False

def IDAstar(b):
    # Bookkeeping
    start = time()
    nodes_generated = 0
    nodes_repeated = 0
    
    fringe_nodes = 0
    nodes_explored = 0

    MAXNODES = 20000000
    openSet = []
    closedSet = []
    visitSet = []
    pathLimit = h(b) - 1
    success = False
    it = 0

    while True:
        pathLimit = pathLimit + 1
        # print ("current pathLimit = ", pathLimit)
        b.g_cost = 0
        openSet.insert(0, b)
        fringe_nodes += 1
        ht = HashTable()
        nodes = 0

        while len(openSet) > 0:
            currentState = openSet.pop(0)
            fringe_nodes -= 1

            nodes = nodes + 1
            if currentState.is_win():
                end = time()
                print_results(currentState, nodes, nodes_repeated, fringe_nodes, nodes_explored, end - start)
                return currentState # SOLUTION FOUND!!!

            if nodes % 1000000 == 0:
                print ((nodes/1000000), "M nodes checked")
            if nodes == MAXNODES:
                print("Limit of nodes reached: exiting without a solution.")
                sys.exit(1)

            if currentState.f_cost <= pathLimit:
                closedSet.insert(0, currentState)
                nodes_explored += 1

                # get the sucessors of the current state
                for x in successors(currentState):
                    # test if node has been "closed"
                    if isClosed(closedSet,x):
                        continue

                    # check if this has already been generated
                    if ht.checkAdd(x):
                        nodes_repeated += 1
                        continue

                    # compute G for each
                    x.g_cost = currentState.g_cost + 1
                    # x.setG(currentState.getG() + 1)

                    x.f_cost = x.g_cost + h(x)
                    # x.setF(x.getG()+ h(x))
                    #x.setParent(currentState)
                    openSet.insert(0, x) # push
                    fringe_nodes += 1
            else:
                visitSet.insert(0, currentState)

        #print "Nodes checked = ", nodes
        # print("iteration = ", it)
        it = it + 1
        if len(visitSet) == 0:
            print("FAIL")
            return None

        # set a new cut-off value (pathLimit)
        low = visitSet[0].f_cost
        # low = visitSet[0].getF()
        for x in visitSet:
            if x.f_cost < low:
            # if x.getF() < low:
                low = x.f_cost
                # low = x.getF()
        pathLimit = low

        # move nodes from VISIT to OPEN and reset closedSet
        openSet.extend(visitSet)
        fringe_nodes += len(visitSet)
        visitSet = []
        closedSet = []