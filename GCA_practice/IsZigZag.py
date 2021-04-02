"""
Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

Example

For numbers = [1, 2, 1, 3, 4], the output should be isZigzag(numbers) = [1, 1, 0].

(numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
(numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
(numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;
For numbers = [1, 2, 3, 4], the output should be isZigzag(numbers) = [0, 0];

Since all the elements of numbers are increasing, there are no zigzags.

For numbers = [1000000000, 1000000000, 1000000000], the output should be isZigzag(numbers) = [0].

Since all the elements of numbers are the same, there are no zigzags.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer numbers

An array of integers.

Guaranteed constraints:
3 ≤ numbers.length ≤ 100,
1 ≤ numbers[i] ≤ 109.

[output] array.integer

Return an array, where the ith element equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.
"""

"""
Plan:
1. Create an empty list to hold binary 1's and 0's for the results of each 
triple.
2. Iterate over the given list 3 at a time, checking if it is a valid zigzag 
pattern.
3. Return the binary result list.
"""


def isZigzag(numbers):
	res = []

	for i in range(len(numbers) - 2):
		if numbers[i] < numbers[i + 1] > numbers[i + 2] or numbers[i] > \
				numbers[
			i + 1] < numbers[i + 2]:
			res.append(1)

		else:
			res.append(0)

	return res


# Testing:
if __name__ == '__main__':
	print(f'Test 1 Output: {isZigzag([1, 2, 1, 3, 4])}')
	print(f'Test 1 Expected Output: [1, 1, 0]\n')

	print(f'Test 2 Output: {isZigzag([1, 2, 3, 4])}')
	print(f'Test 2 Expected Output: [0, 0]\n')

	print(f'Test 3 Output: {isZigzag([1000000000, 1000000000, 1000000000])}')
	print(f'Test 3 Expected Output: [0]\n')

	print(f'Test 4 Output: {isZigzag([1, 2, 4, 3, 1])}')
	print(f'Test 4 Expected Output: [0, 1, 0]\n')

	print(f'Test 5 Output: {isZigzag([3, 5, 2, 6, 10])}')
	print(f'Test 5 Expected Output: [1, 1, 0]\n')

	print(f'Test 6 Output: {isZigzag([1, 3, 4, 5, 6, 14, 14])}')
	print(f'Test 6 Expected Output: [0, 0, 0, 0, 0]\n')

	print(f'Test 7 Output: {isZigzag([1, 5, 7, 3, 10, 2, 4, 9, 8, 6])}')
	print(f'Test 7 Expected Output: [0, 1, 1, 1, 1, 0, 1, 0]\n')

	print(f'Test 8 Output: {isZigzag([11, 14, 3, 17, 16, 13, 3, 7, 19, 8])}')
	print(f'Test 8 Expected Output: [1, 1, 1, 0, 0, 1, 0, 1]\n')
