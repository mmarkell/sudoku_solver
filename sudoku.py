import sys
from loader import load, parse
from solver import solve

def main():
	if len(sys.argv) != 2:
		print("USAGE: python3 sudoku.py board")
	else:
		file = load('boards/' + sys.argv[1])
		parsed = parse(file)
		solve(parse(file))

main()
