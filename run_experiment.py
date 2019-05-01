import sys
from sokoban_game import Sokoban

'''
Runs experiment
'''

def run_search(s, filename, search_selection):
    board = s.new_game(filename)
    print('Intializing Board:')
    print_board_lists(board)
    print('\nSolving ' + filename + '...')
    s.search(board, search_selection)

def print_board_lists(board):
    print('Walls Locations:')
    print(*board.walls)
    print('Boxes Locations:')
    print(*board.boxes)
    print('Fboxes Locations:')
    print(*board.fboxes)
    print('Player Locations:')
    print(board.player)
    print('Spaces Locations:')
    print(*board.spaces)
    print('Deadlocks Locations:')
    print(*board.deadlocks)

# def print_board(s, filename):
#     board=[]
#     board_array = s.new_game(filename)
#     for element in *board_array.walls

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

    if len(sys.argv) == 2:
        run_search(soko_game, sys.argv[1], search_selection)
    # Need to specify puzzleboards files
    else:
        run_search(soko_game, 'levels/misc/easy4.txt', search_selection)

if __name__ == "__main__":
    main()