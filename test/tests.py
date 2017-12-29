import sys
sys.path.insert(0, '..')
from loader import load, parse
from solver import solve
from delayed_assert import expect, assert_expectations

def solve_it(arg):
	file = load(arg)
	parsed = parse(file)
	return solve(parse(file))[1]

def check_pass(arg):
	expect(solve_it('../boards/' + arg) == True)

def test_one():
	check_pass('board_one.txt')

def test_two():
	check_pass('board_two.txt')

def test_three():
	check_pass('board_three.txt')

def test_four():
	check_pass('board_four.txt')

def test_five():
	check_pass('board_five.txt')

def test_six():
	check_pass('board_six.txt')
	
def test_seven():
	check_pass('board_seven.txt')

assert_expectations()
