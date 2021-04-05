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


# ### NEW SOLUTION 04-05-2021 ### #
"""
- Create a new list `b` that is empty
- Check for edge case of only one value in `a`
- If `a[i]` at index 0, then `b[i] = a[i] + a[i + 1]`, append the sum to `b`
- If `a[i]` at the last index, then `b[i] = a[i - 1] + a[i]`, append the sum 
to `b`
- Else, `b[i] = a[i - 1] + a[i] + a[i + 1]`, append the sum to `b`
- Return the mutated array `b`
"""


def mutateTheArray(n, a):
	# Create an empty list to store the resulting sums
	b = []

	# If there is only one element in `a`
	if n < 2:
		return a

	# If at the first element in the list
	if a[0]:
		# Append the sum of the first 2 elements in the list
		b.append(a[0] + a[1])

	# Iterate through the list from the second element to the next to last
	# element
	for i in range(1, len(a) - 1):
		# Append the sum to the list fro results
		b.append(a[i - 1] + a[i] + a[i + 1])

	# If at the last element in the list
	if a[-1]:
		# Append the sum of the last 2 elements
		b.append(a[-2] + a[-1])

	# Return the results list
	return b


# Test Cases:
if __name__ == '__main__':
	print(mutateTheArray(5, [4, 0, 1, -2, 3]))      # -> [4, 5, -1, 2, 1]
	print(mutateTheArray(6, [3, 5, 8, 3, 9, 6]))    # -> [8, 16, 16, 20, 18, 15]


"""
Test from CodeSignal:

Test 1
Input:
n: 5
a: [4, 0, 1, -2, 3]
Expected Output:
[4, 5, -1, 2, 1]

Test 2
Input:
n: 1
a: [9]
Expected Output:
[9]

Test 3
Input:
n: 4
a: [1, 2, 3, 4]
Expected Output:
[3, 6, 9, 7]

Test 4
Input:
n: 9
a: [-9, -8, 7, 7, 7, 6, -6, 4, 6]
Expected Output:
[-17, -10, 6, 21, 20, 7, 4, 4, 10]

Test 5
Input:
n: 10
a: [6, -5, -5, 5, 10, 5, 1, 8, 6, -2]
Expected Output:
[1, -4, -5, 10, 20, 16, 14, 15, 12, 4]

Test 6
Input:
n: 10
a: [1, 10, 10, -6, 5, -3, -7, 10, 9, 10]
Expected Output:
[11, 21, 14, 9, -4, -5, 0, 12, 29, 19]

Test 7
Input:
n: 4
a: [-6, -5, -7, -1]
Expected Output:
[-11, -18, -13, -8]

Test 8
Input:
n: 8
a: [-4, -5, 0, -6, -5, -4, -7, 9]
Expected Output:
[-9, -9, -11, -11, -15, -16, -2, 2]

Test 9
Input:
n: 1
a: [-5]
Expected Output:
[-5]

Test 10
Input:
n: 5
a: [-9, -6, 10, -6, -10]
Expected Output:
[-15, -5, -2, -6, -16]
"""