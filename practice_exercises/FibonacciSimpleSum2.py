"""
For a given positive integer n determine if it can be represented as a sum
	of two Fibonacci numbers (possibly equal).

Example:

For n = 1, the output should be:
	fibonacciSimpleSum2(n) = true.

	Explanation: 1 = 0 + 1 = F0 + F1.

For n = 11, the output should be:
	fibonacciSimpleSum2(n) = true.

	Explanation: 11 = 3 + 8 = F4 + F6.

For n = 60, the output should be:
	fibonacciSimpleSum2(n) = true.

	Explanation: 60 = 5 + 55 = F5 + F10.

For n = 66, the output should be:
	fibonacciSimpleSum2(n) = false.

	Explanation: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
		- Can not add only two ints to get 66.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n
	Guaranteed constraints:
	1 ≤ n ≤ 2 · 109.

[output] boolean
	true if n can be represented as Fi + Fj, false otherwise.
"""

"""
Test Cases:
n = 37
output --> True
Explaination --> f4 = 3, F9 = 34 (3 + 34 = 37)

n = 66
output --> False
Explanation --> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
                 Can not add only two ints to get 66.

Plan:
1. Create a helper function to get fibonacci numbers up to n using recursion
2. While there are values in the fibonacci numbers, find two number only that 
add up to n.
3. Return True if only two fib numbers add up to the n number.
"""


def fibonacciSimpleSum2(n):
	# Check if n is 1 or less
	if n <= 1:
		return True

	# Create an empty list to hold fibonacci numbers
	nums_list = []
	# Create a counter to increament for each fib number
	count = 0

	# Iterate while fib_nums value is less than n
	while fib_nums(count) < n:
		# Add fib_nums value to the list I created above
		nums_list.append(fib_nums(count))
		# Increament the counter
		count += 1

	# Iterate through the num_list values
	for dig in nums_list:
		# If n - current digit in fib_nums is in the list
		if n - dig in nums_list:
			# Only 2 values add up to n, return True
			return True

	# If the condition is not met, return False
	return False


# Define a function to get the fibonacci numbers up to value n
def fib_nums(num):
	# Formula to get a list of fibonacci values up to num
	return round(pow(((1 + math.sqrt(5)) / 2), num) / math.sqrt(5))


