import sys, csv
import glob
from sokoban_game import Sokoban
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

    print('\nSolving ' + filename + ' with ' + search_method + ' using ' + str(h_method) + ' with path_limit_increment ' + str(path_limit)) 
    
    if h_method is not None:
        h_val = str(s.get_h_val(board, h_method))
        print('Puzzle has a ' + h_method + ' heuristic value of ' + h_val)

    s.print_2d_board(board)

    try:
        solved_board = s.search(board, search_selection, h_method, path_limit)
        print('Puzzle Solved...')
        s.print_board(solved_board)
        csvWriter(filename, search_method, h_method, path_limit)
    except:
        print('Puzzle could not be solved in 2 minute...')


def csvWriter(filename, search_method, h_method = None, path_limit = None):
    write_file_name = filename + '.csv'
    with open(write_file_name, 'w') as f:
        output = csv.writer(f)
        output.writerow(['Hi', 'MD'])
        # 's_' + search_method + 'h_' + h_method + '_pl_' + path_limit + 
        # data = 'some data to be written to the file'
    

def generate_results():
    microbans = glob.glob("levels/microban/" + "*.txt")
    miscs = glob.glob("levels/misc/" + "*.txt")
    sokwholes = glob.glob("levels/sokwhole/" + "*.txt")
    sokwholes.sort()
    miscs.sort()
    microbans.sort()

    folders = [microbans, miscs, sokwholes]
    
    for folder in folders:
        num_puzzles = 2
        for puzzle in folder:
            if num_puzzles == 0:
                break
            else:
                soko_game = Sokoban()
                run_search(soko_game, puzzle, 1) # BFS

                run_search(soko_game, puzzle, 2, 'm', 1) # IDA*, mahattan, path_limit_incrementer = 1
                run_search(soko_game, puzzle, 2, 'm', 4) # IDA*, mahattan
                run_search(soko_game, puzzle, 2, 'm') # IDA*, mahattan, path_limit_incrementer = dynamic

                run_search(soko_game, puzzle, 2, 'e', 1) # IDA*, mahattan, path_limit_incrementer = 1
                run_search(soko_game, puzzle, 2, 'e', 4) # IDA* with euclidean
                run_search(soko_game, puzzle, 2, 'e') # IDA* with euclidean, 

                # run_search(soko_game, puzzle, 2, 'max', 1) # IDA*, mahattan, path_limit_incrementer
                # run_search(soko_game, puzzle, 2, 'max', 4) # IDA* with euclidean
                # run_search(soko_game, puzzle, 2, 'max') # IDA* with max between m & e
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