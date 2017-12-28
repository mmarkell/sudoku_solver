from pos import Position

def load(arg):
	return open(arg).readlines()[0].strip('\n')

def prepare(board):
	return [[Position(value) for value in i] for i in board]

def parse(board):
	count = 0
	board = [int(b) for b in board]
	b = []
	i = 0
	while i <= len(board):
		b += [board[i:i+9]]
		i += 9
	return prepare(b[:-1])
