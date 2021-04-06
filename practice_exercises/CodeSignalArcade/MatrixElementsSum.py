"""
After becoming famous, the CodeBots decided to move into a new building
	together. Each of the rooms has a different cost, and some of them are
	free,
	but there's a rumour that all the free rooms are haunted! Since the
	CodeBots
	are quite superstitious, they refuse to stay in any of the free rooms, or
	any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the
	cost of the room, your task is to return the total sum of all rooms that
	are
	suitable for the CodeBots (ie: add up all the values
	that don't appear below a 0).

Example:

For matrix = [[0, 1, 1, 2],
              [0, 5, 0, 0],
              [2, 0, 3, 3]]

	the output should be:
		matrixElementsSum(matrix) = 9.

https://codesignal.s3.amazonaws.com/tasks/matrixElementsSum/img/example1.png
?_tm=1582038746746

	There are several haunted rooms, so we'll disregard them as well as any
		rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.

For matrix = [[1, 1, 1, 0],
              [0, 5, 0, 1],
              [2, 1, 3, 10]]

	the output should be:
		matrixElementsSum(matrix) = 9.

https://codesignal.s3.amazonaws.com/tasks/matrixElementsSum/img/example2.png
?_tm=1582038747009

	Note that the free room in the final column makes the full column
		unsuitable for bots (not just the room directly beneath it). Thus,
		the answer is 1 + 1 + 1 + 5 + 1 = 9.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix
	A 2-dimensional array of integers representing the cost of each room in
		the building. A value of 0 indicates that the room is haunted.

	Guaranteed constraints:
		1 ≤ matrix.length ≤ 5,
		1 ≤ matrix[i].length ≤ 5,
		0 ≤ matrix[i][j] ≤ 10.

[output] integer
	The total price of all the rooms that are suitable for
		the CodeBots to live in.
"""

"""
Test Cases:
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
OUTPUT --> 9
Expanation --> 1 + 1 + 2 + 5 = 9 (these are the only values not below a 0 in 
the matrix above)

matrix = [[0, 8, 3, 9],
          [7, 0, 6, 5],
          [1, 1, 0, 9]]
OUTPUT --> 40
Expanation --> 8 + 3 + 9 + 6 + 5 + 9 = 40 (these are the only values not 
below a 0 in the matrix above)

Plan:
1. Create a list to hold the sum.
2. Iterate through the rows and columns of the matrix.
3. If the value is not 0 or positioned below a 0 in the matrix, increament 
the sum by the value at that position.
4. Return the final sum of the valid rooms.
"""


def matrixElementsSum(matrix):
	# Create a variable to hold the current sum
	result = 0
	# Create a list to hold the columns that already saw a 0
	bad_col = []

	# Iterate through the matrix rows
	for row in range(len(matrix)):
		# Iterate through the matrix columns
		for col in range(len(matrix[row])):
			# If the current value is 0
			if matrix[row][col] == 0:
				# Add it to the bad column list
				bad_col.append(col)

			# If the current value is not 0 and
			#   the column is not in the bad column list
			if matrix[row][col] != 0 and col not in bad_col:
				# Increase the total sum by the current value
				result += matrix[row][col]

	# Return the total sum of valid rooms
	return result


# Testing:
if __name__ == '__main__':
	m = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
	ans = 9
	if matrixElementsSum(m) == ans:
		print(f'Test 1 PASSED! Answer is: {ans}')
	else:
		print(f'Test 1 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[1,1,1,0], [0,5,0,1], [2,1,3,10]]
	ans = 9
	if matrixElementsSum(m) == ans:
		print(f'Test 2 PASSED! Answer is: {ans}')
	else:
		print(f'Test 2 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[1,1,1], [2,2,2], [3,3,3]]
	ans = 18
	if matrixElementsSum(m) == ans:
		print(f'Test 3 PASSED! Answer is: {ans}')
	else:
		print(f'Test 3 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[0]]
	ans = 0
	if matrixElementsSum(m) == ans:
		print(f'Test 4 PASSED! Answer is: {ans}')
	else:
		print(f'Test 4 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[1, 0, 3], [0, 2, 1], [1, 2, 0]]
	ans = 5
	if matrixElementsSum(m) == ans:
		print(f'Test 5 PASSED! Answer is: {ans}')
	else:
		print(f'Test 5 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[1], [5], [0], [2]]
	ans = 6
	if matrixElementsSum(m) == ans:
		print(f'Test 6 PASSED! Answer is: {ans}')
	else:
		print(f'Test 6 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[1, 2, 3, 4, 5]]
	ans = 15
	if matrixElementsSum(m) == ans:
		print(f'Test 7 PASSED! Answer is: {ans}')
	else:
		print(f'Test 7 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[2], [5], [10]]
	ans = 17
	if matrixElementsSum(m) == ans:
		print(f'Test 8 PASSED! Answer is: {ans}')
	else:
		print(f'Test 8 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[4, 0, 1], [10, 7, 0], [0, 0, 0], [9, 1, 2]]
	ans = 15
	if matrixElementsSum(m) == ans:
		print(f'Test 9 PASSED! Answer is: {ans}')
	else:
		print(f'Test 9 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')

	m = [[1]]
	ans = 1
	if matrixElementsSum(m) == ans:
		print(f'Test 10 PASSED! Answer is: {ans}')
	else:
		print(f'Test 10 FAILED!\nYour Output: {matrixElementsSum(m)}\n '
		      f'Correct: {ans}')
