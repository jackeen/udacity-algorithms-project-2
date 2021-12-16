# Square Root of an Integer

import math


def sqrt(n):
	"""
    Calculate the floored square root of a number.

    Args:
       n(int): Number to find the floored squared root
    
	Returns:
       int: Floored Square Root
    """
	
	if n == 0 or n == 1:
		return n

	min_border = 0
	max_border = n
	middle = None

	while True:
		middle = (min_border + max_border) // 2
		
		if min_border == middle:
			break
		
		if n > middle ** 2:
			min_border = middle
		elif n < middle ** 2:
			max_border = middle
		else:
			break

	return middle


class Test:

	count = 0

	def run(self, input):
		self.count += 1

		expected = math.floor(math.sqrt(input))
		output = sqrt(input)

		print('test {}, input: {}'.format(self.count, input))
		print('output: {}, expected: {}'.format(output, expected))

		if expected == output:
			print("Pass")
		else:
			print("Fail")

		print('\n')


# test
test = Test()

test.run(9)
test.run(0)
test.run(16)
test.run(1)
test.run(27)



