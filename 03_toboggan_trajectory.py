from functools import reduce
import operator

def build_board(path):
    """takes a path and returns the board"""
    board = []
    with open(path, "r") as f:
        for line in f:
            board.append(line.replace("\n", ""))
    return board


def traverse(board, row, col, delta_r, delta_c):
    """takes a board, with starting posiiton row, col
    moves down delta_r and across delta_c.
    returns 1 if there is a tree, 0 otherwise, and new
    position tuple (r, c)"""
    numcols = len(board[0])
    row += delta_r
    col = (col + delta_c) % numcols
    if board[row][col] == "#":
        tree = 1
    else:
        tree = 0
    return tree, row, col


def fly_sled(board, startrow, startcol, delta_r, delta_c):
    numtrees = 0
    numrows = len(board)
    row, col = startrow, startcol

    while row < numrows - 1:
        tree, row, col = traverse(board, row, col, delta_r, delta_c)
        numtrees += tree
    return numtrees



def run_tree_scenarios():
    results = {}

    scenarios = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    for scenario in scenarios:
        delta_r, delta_c = scenario
        numtrees = fly_sled(board, 0, 0, delta_r, delta_c)
        results[scenario] = numtrees
    return reduce(operator.mul, results.values(), 1)


board = build_board("input_files/problem3.txt")

numtrees = fly_sled(board, 0, 0, 1, 3)
print(f"part 1 number of trees is {numtrees}")

trees_multiplied = run_tree_scenarios()
print(f"part 2 answer is {trees_multiplied}")