"""
For two arrays of the same length `a` and `b`, let's say `a` is a
	"cyclic shift" of `b` if it's possible for `a` to become equal to `b`
	by moving 0 or more last elements to the beginning of the array,
	without changing the internal order.

Demonstration:

You are given an array of integers `elements`.
Your task is to check whether `elements` is a "cyclic shift" of the
	"identity array" [1, 2, ..., elements.length] or the
	"reversed identity array" [elements.length, elements.length - 1, ..., 1].
	Return `True` if `elements` is a `cyclic shift` of the `identity` or
	`reversed identity` array, otherwise return `False`.

Example:

For `elements = [1, 4, 2, 3]`, the output should be:
	arrayShift(elements) = False.

Let's consider all the cyclic shifts of elements:

- Moving 0 elements from the end to the beginning, we get [1, 4, 2, 3].
- Moving 1 elements from the end to the beginning, we get [3, 1, 4, 2].
- Moving 2 elements from the end to the beginning, we get [2, 3, 1, 4].
- Moving 3 elements from the end to the beginning, we get [4, 2, 3, 1].
- None of these cyclic shifts equal the identity array [1, 2, 3, 4] or
	the reversed identity array [4, 3, 2, 1]. So the answer is False.

For `elements = [3, 4, 1, 2]`, the output should be:
	arrayShift(elements) = True.

- If we move the last 2 elements of the given array from the end to the
	beginning, we get [1, 2, 3, 4], which is the identity array,
	so the answer is True.

For `elements = [3, 2, 1, 4]`, the output should be:
	arrayShift(elements) = True.

- If we move the last element of the given array to the beginning, we get
	[4, 3, 2, 1], which is the reversed identity array, so the answer is True.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.integer elements
	An array of integers.

	Guaranteed constraints:
		3 ≤ elements.length ≤ 100,
		1 ≤ elements[i] ≤ elements.length.

[output] boolean
	Return True if elements is a cyclic shift of either identity array
		[1, 2, ..., elements.length] or reversed identity array
		[elements.length, elements.length - 1, ..., 1]. Otherwise, return False.
"""

"""
1. Create a identity array ranging from 1 to len(elements) + 1
2. Create a reverse identity array ranging from len(elements) + 1 to 1
3. Iterate over the list of elements move the last value to the beginning one 
by one while checking if it is equal to one of my identity arrays.
4. Return True or False based on the condition
"""


def arrayShift(elements):
	id_arr = [x for x in range(1, len(elements) + 1, 1)]
	rev_id_arr = id_arr[::-1]

	for i in range(len(elements)):
		keep = elements
		keep = keep[0:-1]
		print(f'Keep arr: {keep}')
		new = [elements[-1]] + keep
		print(f'New arr: {new}')

		if new == id_arr or new == rev_id_arr:
			return True

		else:
			elements = new
			continue

	return False
