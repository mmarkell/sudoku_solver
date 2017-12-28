import sys
sys.path.insert(0, '..')
from loader import load, parse
from solver import solve

def solve_it(arg):
	file = load(arg)
	parsed = parse(file)
	return solve(parse(file))

class Tester():

	def assert_pass(self, arg):
		assert solve_it('../boards/' + arg) == True

	def test_everything(self):
		self.assert_pass('board_one.txt')
		self.assert_pass('board_two.txt')
		# self.assert_pass('board_three.txt')
		# self.assert_pass('board_four.txt')
		# self.assert_pass('board_five.txt')
		# self.assert_pass('board_six.txt')
		# self.assert_pass('board_seven.txt')

def main():
	tester = Tester()
	tester.test_everything()

main()