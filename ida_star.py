from time import time
from copy import deepcopy
from hash_table import HashTable
import heapq, sys


def print_results(board, gen, rep, fri, expl, dur):
    print("\n2. Iterative Deepening A* Search (IDA*)")
    print("Solution: " + board.getDirections())
    print("Nodes generated: " + str(gen))
    print("Nodes repeated: " + str(rep))
    print("Fringe nodes: " + str(fri))
    print("Explored nodes: " + str(expl))
    print('Duration: ' + str(dur) + ' secs')

# Manhattan Distance between two points
def manDistance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def heuristic(sm):
    # generate all possible combinations of goals for each block
    solutions = []
    for b in sm.boxes:
        solution = []
        for g in sm.goals:
            sol = (b, g, manDistance(b,g))
            solution.append(sol)
        solutions.append(solution)

    # for sol in solutions:
    #     print sol
    # print "------"

    # Select the best
    best = sys.maxsize
    for s in solutions[0]:
        usedGoal = []
        usedBlock = []
        solution = []

        usedGoal.append(s[1])
        usedBlock.append(s[0])
        solution.append(s)
        h = s[2]
        for lin in solutions:
            for col in lin:
                if col[1] not in usedGoal and col[0] not in usedBlock:
                    solution.append(col)
                    usedGoal.append(col[1])
                    usedBlock.append(col[0])
                    h = h + col[2]
                    break
        if h < best:
            best = h
            result = solution

    # print "-------"
    # print result
    # print best

    w = sm.getPlayer()
    d = sys.maxsize
    v = (-1,-1)
    for x in sm.getUnplacedBlocks():
        if manDistance(w, x) < d:
            d = manDistance(w, x)
            v = x
    if v is not (-1,-1):
        best = best + d

    return best

def isClosed(closedSet, x):
    for y in closedSet:
        if x == y:
            return True
    return False


def IDAstar(sm, h):
    MAXNODES = 20000000
    openSet = []
    closedSet = []
    visitSet = []
    pathLimit = h(sm) - 1
    sucess = False
    it = 0

    while True:
        pathLimit = pathLimit + 1
        print ("current pathLimit = ", pathLimit)
        sm.setG(0)
        openSet.insert(0, sm)
        ht = HashTable()
        nodes = 0

        while len(openSet) > 0:
            currentState = openSet.pop(0)
            #currentState.printMap()

            nodes = nodes + 1
            if currentState.isSolution():
                return currentState # SOLUTION FOUND!!!

            if nodes % 1000000 == 0:
                print ((nodes/1000000), "M nodes checked")
            if nodes == MAXNODES:
                print("Limit of nodes reached: exiting without a solution.")
                sys.exit(1)

            if currentState.getF() <= pathLimit:
                closedSet.insert(0, currentState)
                # get the sucessors of the current state
                for x in currentState.children():
                    # test if node has been "closed"
                    if isClosed(closedSet,x):
                        continue

                    # check if this has already been generated
                    if ht.checkAdd(x):
                        continue

                    # compute G for each
                    x.setG(currentState.getG() + 1)
                    x.setF(x.getG()+ h(x))
                    #x.setParent(currentState)
                    openSet.insert(0, x) # push
            else:
                visitSet.insert(0, currentState)

        #print "Nodes checked = ", nodes
        print("iteration = ", it)
        it = it + 1
        if len(visitSet) == 0:
            print("FAIL")
            return None

        # set a new cut-off value (pathLimit)
        low = visitSet[0].getF()
        for x in visitSet:
            if x.getF() < low:
                low = x.getF()
        pathLimit = low

        # move nodes from VISIT to OPEN and reset closedSet
        openSet.extend(visitSet)
        visitSet = []
        closedSet = []

def IDA_Star(board):
    start = time()
    nodes_generated = 0
    nodes_repeated = 0
    if board.is_win():
        end = time()
        print_results(board, 1, 0, 0, 1, end - start)
        return board
    node = deepcopy(board)
    nodes_generated += 1
    frontier = []
    frontierSet = set()
    heapq.heappush(frontier, node)
    frontierSet.add(node)
    explored = set()
    keepLooking = True
    while keepLooking:
        if len(frontier) == 0:
            print("Solution not found")
            return
        else:
            currNode = heapq.heappop(frontier)
            frontierSet.remove(currNode)
            if currNode.is_win():
                end = time()
                print_results(currNode, nodes_generated, nodes_repeated, len(
                              frontier), len(explored), end - start)
                return currNode
            moves = currNode.moves_available()
            currNode.fboxes = frozenset(currNode.boxes)
            explored.add(currNode)
            for m in moves:
                child = deepcopy(currNode)
                nodes_generated += 1
                child.move(m)
                if child.is_win():
                    end = time()
                    print_results(child, nodes_generated, nodes_repeated, len(
                                  frontier), len(explored), end - start)
                    return child
                if child not in explored:
                    if child not in frontierSet:
                        heapq.heappush(frontier, child)
                        frontierSet.add(child)
                elif child in frontierSet:
                    count = frontier.count(child)
                    i = 0
                    while i <= count:
                        a = frontier.pop((frontier.index(child)))
                        if child.cost < a.cost:
                            heapq.heappush(frontier, child)
                            child = a
                            i = count + 1
                        else:
                            heapq.heappush(frontier, a)
                            i += 1
                    nodes_repeated += 1
