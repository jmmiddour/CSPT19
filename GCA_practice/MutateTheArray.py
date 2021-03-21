"""
Given an integer n and an array a of length n, your task is to apply the
	following mutation to `a`:

	* Array a mutates into a new array b of length n.
	* For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
	* If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist,
		it should be set to 0. For example, b[0] should be
		equal to 0 + a[0] + a[1].

Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be
	mutateTheArray(n, a) = [4, 5, -1, 2, 1].

	* b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
	* b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
	* b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
	* b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
	* b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

So, the resulting array after the mutation will be [4, 5, -1, 2, 1].

Input/Output

	[execution time limit] 4 seconds (py3)

	[input] integer n
	An integer representing the length of the given array.

	Guaranteed constraints:
	1 ≤ n ≤ 103.

	[input] array.integer a
	An array of integers that needs to be mutated.

	Guaranteed constraints:
	a.length = n,
	-103 ≤ a[i] ≤ 103.

	[output] array.integer
	The resulting array after the mutation.
"""

"""
Plan:
1. Create a new list `b` with all 0 the length of `n`
2. If at the first index of `b` -> `b[i - 1] = 0`
3. If at the last index of `b` -> `b[i + 1] = 0`
4. For every other index in `b` -> b[i] = a[i-1] + a[i] + a[i+1]
5. Return mutated array `b`
"""


def mutateTheArray(n, a):
	b = [0] * n  # list of 0's the length of n

	if n < 2:  # If there is only one element in array `a`
		return a  # Just return array `a`

	else:  # If there are 2 or more elements in array `a`
		b[0] = a[0] + a[1]  # `b` at the first index, only add first 2
		# elements from array `a`
		b[-1] = a[-2] + a[-1]  # `b` at last index, only add the last 2
		# elements from array `a`

		for i in range(1, len(b) - 1):  # Iterate through the rest of the list
			b[i] = a[i - 1] + a[i] + a[i + 1]  # add `i` plus surrounding
		# elements together from array `a`

	return b  # Returns the mutated array `b`


# Test Cases:
if __name__ == '__main__':
	print(mutateTheArray(5, [4, 0, 1, -2, 3]))      # -> [4, 5, -1, 2, 1]
	print(mutateTheArray(6, [3, 5, 8, 3, 9, 6]))    # -> [8, 16, 16, 20, 18, 15]
