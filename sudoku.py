import sys
from loader import load, parse
from solver import solve, generate

def main():
	if len(sys.argv) == 2:
		file = load('boards/' + sys.argv[1])
		parsed = parse(file)
		solve(parse(file))
	elif len(sys.argv) == 1:
		file = load('boards/zeros.txt')
		parsed = parse(file)
		generate(parse(file))
	else:
		print("USAGE: python3 sudoku.py board")

main()
