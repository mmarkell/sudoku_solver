import time
import pickle
import copy
import sys
from pos import Position
def solve(board):
	start = time.clock()
	board = prepare(board)
	print_prepared_board(board)
	board = prune_possibilities(board)
	board, v = search_for_solution(board)
	t = time.clock() - start
	print("took %f secs to finish" % t)
	if board_full(board):
		print("solution")
		print_prepared_board(board)
		return board
	else:
		print("couldnt solve")

def search_for_solution(board):
    if bad_board(board):
    	return board, False
    if board_full(board): 
    	return board, True
    board = prune_possibilities(board)
    i, j = get_min_move(board)
    if i == -1:
    	return board, True
    for d in [x for x in board[i][j].possible]:
    	board2, good = search_for_solution(add_piece(pickle.loads(pickle.dumps(board)), d, i, j))
    	if good:
    		return board2, True
    return board, False

def add_piece(board, v, i, j):
	board[i][j] = Position(v)
	return board

def prune_possibilities(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			for new_j in range(0, len(board)):
				if board[i][new_j].value == 0 and board[i][j].value in board[i][new_j].possible:
					possible = [x for x in board[i][new_j].possible if x != board[i][j].value]
					board[i][new_j].possible = possible
			for new_i in range(0, len(board[j])):
				if board[new_i][j].value == 0 and board[i][j].value in board[new_i][j].possible:
					possible = [x for x in board[new_i][j].possible if x != board[i][j].value]
					board[new_i][j].possible = possible
	for i in range(len(board)):
		for j in range(len(board[i])):
			if len(board[i][j].possible) == 1:
				add_piece(board, board[i][j].possible[0], i,j)
	return board

def bad_board(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j].value != 0:
					for new_j in range(0, len(board)):
						if new_j != j:
							if board[i][new_j].value == board[i][j].value:
								return True
					for new_i in range(0, len(board[j])):
						if new_i != i:
							if board[new_i][j].value == board[i][j].value:
								return True

	for i in range(3):
		for j in range(3):
			elements = []
			for a in range(i*3,i*3 +3 ):
				for b in range(j*3, j*3 + 3):
					if board[a][b].value != 0 and board[a][b].value in elements:
						return True
					elements += [board[a][b].value]

	return False

def board_full(board):
	for r in board:
		for c in r:
			if c.value == 0:
				return False
	return True

def get_min_move(board):
	curr_best = 11
	best_i, best_j = -1, -1
	for i in range(len(board)):
		for j in range(len(board[i])):
			if len(board[i][j].possible) < curr_best and len(board[i][j].possible) >= 1:
				curr_best = len(board[i][j].possible)
				best_i, best_j = i, j
	return best_i, best_j

def prepare(board):
	return [[Position(value) for value in i] for i in board]

def print_prepared_board(board):
	print("*" * 27)
	for idx, row in enumerate(board):
		if idx % 3 == 0:
			print("-" * 27)
		buff = ""
		for idx2, col in enumerate(row):
			if idx2 % 3 == 0 and idx2 != 0:
				buff += " | "
			buff += " " + str(col.value) # + " p " + str(col.possible)
		print(buff)

def main():
	if len(sys.argv) != 2:
		print("USAGE: python3 sudoku.py board")
	else:
		file = open(sys.argv[1]).readlines()[0].strip('\n')
		solve(parse(file))

def parse(board):
	count = 0
	board = [int(b) for b in board]
	b = []
	i = 0
	while i < 82:
		b += [board[i:i+9]]
		i += 9
	return b[:-1]

main()

# board = [[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 0], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]
# board = [[0, 0, 7, 0, 9, 0, 0, 0, 0], [2, 0, 9, 7, 0, 0, 0, 0, 0], [0, 4, 8, 0, 0, 3, 0, 0, 2], [0, 0, 0, 1, 3, 0, 0, 7, 0], [0, 3, 4, 0, 7, 0, 5, 8, 0], [0, 7, 0, 0, 5, 4, 0, 0, 0], [8, 0, 0, 4, 0, 0, 2, 5, 0], [0, 0, 0, 0, 0, 1, 8, 0, 9], [0, 0, 0, 0, 8, 0, 6, 0, 0]]
