import sys, csv
import glob
from sokoban_game import Sokoban
# from sokoban_state import State
from heuristics import Heuristic

'''
Runs experiment
'''

PUZZLES = ['easy4.txt', 'minicosmos1.txt', 'minicosmos2.txt',
           'minicosmos3.txt', 'simple1.txt', 'original1.txt', 'original1a.txt', 'original1b.txt']

def run_search(s, filename, search_selection, h_method = None, path_limit = None):
    board = s.new_game(filename)
    # print('Intializing Board...')
    # s.print_board_lists(board)
    # s.print_board(board)

    if search_selection == 1:
        search_method = 'dfs'
    else:
        search_method = 'IDA*'

    print('\nSolving ' + filename + ' with ' + search_method + ' using heuristic function '
         + str(h_method) + ' with path_limit_increment ' + str(path_limit)) 
    
    if h_method is not None:
        h_val = str(s.get_h_val(board, h_method))
        print('Puzzle has a ' + h_method + ' heuristic value of ' + h_val)

    s.print_2d_board(board)

    return s.search(board, search_selection, h_method, path_limit)

    # try:
        # solved_board = s.search(board, search_selection, h_method, path_limit)
        # print('Puzzle Solved...')
        # s.print_board(solved_board)
        # return s.search(board, search_selection, h_method, path_limit)
        # csvWriter(filename, search_method, h_method, path_limit)
    # except:
        # print('Puzzle could not be solved in 2 minute...')
        # return s.search(board, search_selection, h_method, path_limit)

def generate_results():
    microbans = glob.glob("levels/microban/" + "*.txt")
    miscs = glob.glob("levels/misc/" + "*.txt")
    sokwholes = glob.glob("levels/sokwhole/" + "*.txt")
    sokwholes.sort()
    miscs.sort()
    microbans.sort()


    fNames = ["microbans", "miscs", "sokwholes"]
    folders = [microbans, miscs, sokwholes]
    
    # for folder in folders:
    num_puzzles = 30

    # folderName = folder.replace("levels/", "")
    # folderName = folderName.replace("/*.txt", "-output.csv")
    folderName = fNames[folders.index(sokwholes)]
    folderName = folderName + "-output.csv"
    folderName = "results/" + folderName
    with open(folderName, 'w') as f:
        output = csv.writer(f)
        output.writerow(["Puzzle Name", "Search Method", "Is Solved", "Heuristic", "Iteration Step", "Nodes Generated", "Nodes Repeated", "Fringe Nodes", "Explored Nodes", "Duration", "Path"])

        for puzzle in sokwholes:
            if num_puzzles == 0:
                break
            else:
                puzzleName = puzzle.replace("levels/", "")
                try:
                    soko_game = Sokoban()
                    bfs_output = run_search(soko_game, puzzle, 1) # BFS
                    bfs_list = [puzzleName, "bfs", bfs_output[6], "None", "None", bfs_output[1], bfs_output[2], bfs_output[3], bfs_output[4], bfs_output[5], bfs_output[0].getDirections()]
                    output.writerow(bfs_list)
                except:
                    pass
                
                try:
                    ida_1_output = run_search(soko_game, puzzle, 2, 'm', 1) # IDA*, mahattan, path_limit_incrementer = 1
                    ida_1_list = [puzzleName, "IDA*", ida_1_output[6], "Manhattan", "Fixed (1)", ida_1_output[1], ida_1_output[2], ida_1_output[3], ida_1_output[4], ida_1_output[5], ida_1_output[0].getDirections()]
                    output.writerow(ida_1_list)
                except:
                    pass

                try:
                    ida_2_output = run_search(soko_game, puzzle, 2, 'm', 4) # IDA*, mahattan
                    ida_2_list = [puzzleName, "IDA*", ida_2_output[6], "Manhattan", "Fixed (4)", ida_2_output[1], ida_2_output[2], ida_2_output[3], ida_2_output[4], ida_2_output[5], ida_2_output[0].getDirections()]
                    output.writerow(ida_2_list)
                except:
                    pass

                try:
                    ida_3_output = run_search(soko_game, puzzle, 2, 'm') # IDA*, mahattan, path_limit_incrementer = dynamic
                    ida_3_list = [puzzleName, "IDA*", ida_3_output[6], "Manhattan", "Dynamic", ida_3_output[1], ida_3_output[2], ida_3_output[3], ida_3_output[4], ida_3_output[5], ida_3_output[0].getDirections()]
                    output.writerow(ida_3_list)
                except:
                    pass

                try:
                    ida_4_output = run_search(soko_game, puzzle, 2, 'e', 1) # IDA*, mahattan, path_limit_incrementer = 1
                    ida_4_list = [puzzleName, "IDA*", ida_4_output[6], "Euclidean", "Fixed (1)", ida_4_output[1], ida_4_output[2], ida_4_output[3], ida_4_output[4], ida_4_output[5], ida_4_output[0].getDirections()]
                    output.writerow(ida_4_list)
                except:
                    pass
                
                try:
                    ida_5_output = run_search(soko_game, puzzle, 2, 'e', 4) # IDA* with euclidean
                    ida_5_list = [puzzleName, "IDA*", ida_5_output[6], "Euclidean", "Fixed (4)", ida_5_output[1], ida_5_output[2], ida_5_output[3], ida_5_output[4], ida_5_output[5], ida_5_output[0].getDirections()]
                    output.writerow(ida_5_list)
                except:
                    pass
                    
                try:
                    ida_6_output = run_search(soko_game, puzzle, 2, 'e') # IDA* with euclidean
                    ida_6_list = [puzzleName, "IDA*", ida_6_output[6], "Euclidean", "Dynamic", ida_6_output[1], ida_6_output[2], ida_6_output[3], ida_6_output[4], ida_6_output[5], ida_6_output[0].getDirections()]
                    output.writerow(ida_6_list)

                    # run_search(soko_game, puzzle, 2, 'max', 1) # IDA*, mahattan, path_limit_incrementer
                    # run_search(soko_game, puzzle, 2, 'max', 4) # IDA* with euclidean
                    # run_search(soko_game, puzzle, 2, 'max') # IDA* with max between m & e
                except:
                    pass

                num_puzzles -= 1

def main():
    soko_game = Sokoban()

    print("Which search algorithm would you like to run?")
    print("0: Generate Report")
    print("1: Breadth first search")
    print("2: Iterative Deepening A* (IDA*)")
    print("3: Simplified Memory Bounded A* (SMA*)")
    print("4: Monte Carlo Tree Search (MCST)")

    # Should protect against illegal input
    user_input = input("Input a number from above: ")
    search_selection = int(user_input)

    if search_selection == 0: # Generate Result
        generate_results()
    else: # solve specific puzzles using specific algorithm
        if search_selection == 2:
            print("which Heuristic function would you like to use for IDA*?")
            print("m: manhattan distance")
            print("e: euclidean distance")
            print("max: the max between manhattan distance and euclidean distance")
            h_method = input("Input a choice from above: ")
        else:
            h_method = None

        print("Which puzzle would you like to run?")
        print("0: easy4")
        print("1: minicosmos1") 
        print("2: minicosmos2")
        print("3: minicosmos3")
        print("4: simple1")
        print("5: original1")
        user_input2 = input("Input a number from above: ")
        puzzle_selection = int(user_input2)

        # pth = glob.glob('levels/misc/')
        if len(sys.argv) == 2:
            run_search(soko_game, sys.argv[1], search_selection, h_method)
        # Need to specify puzzleboards files
        else:
            # puzzle_file = [path.basename(f) for f in glob.iglob(pth+"*.")]
            if puzzle_selection < 8:
                run_search(soko_game, 'levels/misc/' + PUZZLES[puzzle_selection], search_selection, h_method)
            elif puzzle_selection == 9:
                run_search(soko_game, 'levels/sokwhole/sokwhole_10.txt', search_selection, h_method)
            else:
                run_search(soko_game, 'levels/microban/microban_5.txt', search_selection, h_method)

if __name__ == "__main__":
    main()