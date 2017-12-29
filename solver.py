import time
import pickle
import copy
import random
from pos import Position

def solve(board):
	print_board(board)
	start = time.clock()
	board, v = search_for_solution(board)
	t = time.clock() - start
	print("took %f secs to finish" % t)
	if board_full(board):
		print("solution")
		print_board(board)
		return board, True
	else:
		print("couldnt solve")
		return board, False

def generate(board):
	board, _ = solve(board)
	for i in range(8):
		for j in range(8):
			x, y = random.randint(0, 8), random.randint(0, 8)
			board[x][y] = Position(0)
	print_board(board)
	return board
def search_for_solution(board):
	if bad_board(board):
		return board, False
	if board_full(board):
		return board, True

	changed = True
	board = prune_possibilities(board)
	i, j = get_min_move(board)
	if i == -1:
		return board, False

	for v in board[i][j].possible:
		possible, good = search_for_solution(add_piece(pickle.loads(pickle.dumps(board)), v, i, j))
		if good:
			return possible, True
	return board, False

def add_piece(board, v, i, j):
	board[i][j] = Position(v)
	return board

def prune_possibilities(board):
	for i in range(len(board)):
		for j in range(len(board)):
			rows = [v for v in [board[x][j].value for x in range(len(board))] if v != 0]
			cols = [v for v in [board[i][x].value for x in range(len(board))] if v != 0]
			square = [v for v in [[board[((i - i % 3) + di) % 9][((j - j % 3) + dj) % 9].value for di in range(3)] for dj in range(3)]]
			left_over = [x for x in board[i][j].possible if x not in rows and x not in cols and x not in square]
			if len(left_over) >= 1:
				board[i][j].possible = left_over
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
			for a in range(i*3,i*3 + 3):
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
	best = [[-1, -1]]
	for i in range(len(board)):
		for j in range(len(board[i])):
			if len(board[i][j].possible) < curr_best and len(board[i][j].possible) >= 1:
				curr_best = len(board[i][j].possible)
				best = [[i, j]]
			elif len(board[i][j].possible) == curr_best and len(board[i][j].possible) >- 1:
				best += [[i, j]]
	random.shuffle(best)
	to_return = best[0]
	return to_return[0], to_return[1]

def print_board(board):
	print("*" * 27)
	bufff = ""
	for idx, row in enumerate(board):
		if idx % 3 == 0:
			print("-" * 27)
		buff = ""
		for idx2, col in enumerate(row):
			if idx2 % 3 == 0 and idx2 != 0:
				buff += " | "
			buff += " " + str(col.value) #+ " p " + str(col.possible)
		print(buff)
		bufff += buff + "\n"
	return bufff
