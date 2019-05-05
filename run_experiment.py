import sys
from sokoban_game import Sokoban

'''
Runs experiment
'''

PUZZLES = ['easy4.txt', 'simple1.txt']

def run_search(s, filename, search_selection):
    board = s.new_game(filename)
    print('Intializing Board...')
    # s.print_board_lists(board)
    s.print_2d_board(board)
    # s.print_board(board)
    print('\nSolving ' + filename + '...')
    solved_board = s.search(board, search_selection)
    s.print_board(solved_board)
    print('Puzzle Solved...')

def main():
    soko_game = Sokoban()

    print("Which search algorithm would you like to run?")
    print("1: Breadth first search")
    print("2: Iterative Deepening A* (IDA*)")
    print("3: Simplified Memory Bounded A* (SMA*)")
    print("4: Monte Carlo Tree Search (MCST)")

    # Should protect against illegal input
    user_input = input("Input a number from above: ")
    search_selection = int(user_input)

    print("Which puzzle would you like to run?")
    print("0: easy4")
    print("1: simple1")
    user_input2 = input("Input a number from above: ")
    puzzle_selection = int(user_input2)

    if len(sys.argv) == 2:
        run_search(soko_game, sys.argv[1], search_selection)
    # Need to specify puzzleboards files
    else:
        run_search(soko_game, 'levels/misc/' + PUZZLES[puzzle_selection], search_selection)

if __name__ == "__main__":
    main()