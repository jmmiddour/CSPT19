"""
You are given three arrays of integers `a`, `b`, and `c`, and an array of
	characters signs consisting of '+' and '-' signs.
	All of these arrays have the same length.

Your task is to return a boolean array output of the same length,
	where output[i] = true if the result of applying signs[i] to a[i] and b[i]
	is equal to c[i], and false otherwise.
	In other words, for each index i, check if a[i] signs[i] b[i] = c[i].

Example:

For a = [3, 2, -1, 4],
	signs = ['+', '-', '-', '+'],
	b = [2, 7, -5, 2], and
	c = [5, 5, 4, 2], the output should be:
		checkOperations(a, signs, b, c) = [true, false, true, false].

a  |	signs |	b  | c        |	Result
3  |	+     |	2  |	=	5 |	true
2  |	-	  | 7  |	≠	5 |	false
-1 | -        | -5 |	=	4 |	true
4  | +        |	2  |	≠	2 |	false

- signs[0] = '+', and a[0] + b[0] = 3 + 2 = 5 = c[0];
- signs[1] = '-', and a[1] - b[1] = 2 - 7 = -5 ≠ c[1];
- signs[2] = '-', and a[2] - b[2] = (-1) - (-5) = 4 = c[2];
- signs[3] = '+', and a[3] + b[3] = 4 + 2 = 6 ≠ c[3].

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.integer a
	The first array of integers.

	Guaranteed constraints:
		0 ≤ a.length ≤ 1000,
		-1000 ≤ a[i] ≤ 1000.

[input] array.char signs
	An array consisting of signs '+' and '-'.

	Guaranteed constraints:
		signs.length = a.length.

[input] array.integer b
	The second array of integers.

	Guaranteed constraints:
		b.length = a.length,
		-1000 ≤ b[i] ≤ 1000.

[input] array.integer c
	The third array of integers.

	Guaranteed constraints:
		c.length = a.length,
		-2000 ≤ c[i] ≤ 2000.

[output] array.boolean
	A boolean array,
		where the ith element is true if a[i] sign[i] b[i] = c[i]
		and false otherwise.
"""

"""
1. Create an `output` list to boolean values.
2. Iterate through all the list to find out it a[i] signs[i] b[i] = c[i]
3. append True or False to the output list based on condition from 2
4. Return the bool list `output`
"""


def checkOperations(a, signs, b, c):
	output = []
	signs = ''.join(signs)
	print(signs)

	for i in range(len(a)):
		# print(f'signs at i: {signs[i]}')
		if signs[i] == '+':
			if (a[i] + b[i]) == c[i]:
				output.append(True)

			else:
				output.append(False)

		elif signs[i] == '-':
			if (a[i] - b[i]) == c[i]:
				output.append(True)

			else:
				output.append(False)

	return output
