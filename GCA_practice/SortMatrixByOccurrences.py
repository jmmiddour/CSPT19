"""
Given a square matrix of integers m, your task is to rearrange its numbers
	in the following way:

- First, sort its values in ascending order of how frequently the number
	occurs in m. In the case of a tie, sort the equally frequent numbers
	by their values, in ascending order.

- Second, place the sorted numbers diagonally, starting from the bottom right
	corner, like this:

![element ordering]https://codesignal.s3.amazonaws.com/tasks
/sortMatrixByOccurrences/img/sortMatrixByOccurrences.gif?_tm=1582092096487

Example

For

m = [[ 1, 4, -2],
     [-2, 3,  4],
     [ 3, 1,  3]]
the output should be:
	sortMatrixByOccurrences(m) = [[3,  3,  4],
	                              [3,  4,  1],
	                              [1, -2, -2]]

First we look at the frequency of each number:

- Number 1 occurs 2 times;
- Number -2 occurs 2 times;
- Number 3 occurs 3 times;
- Number 4 occurs 2 times.

Because numbers 1, -2, and 4 occur the same number of times, we sort them
	by their values in ascending order. Number 3 occurs the most numbers
	of times, so it goes after all other numbers. Finally, after sorting we
	get the following array: [-2, -2, 1, 1, 4, 4, 3, 3, 3]

After sorting, the numbers should be placed diagonally starting from the
	bottom right corner, as follows:

[[3,  3,  4],
 [3,  4,  1],
 [1, -2, -2]]

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.array.integer m
	A square matrix of integers.

	Guaranteed constraints:
		1 ≤ m.length ≤ 40,
		m[i].length = m.length,
		-1000 ≤ m[i][j] ≤ 1000.

[output] array.array.integer
	The matrix m rearranged according to the specifications above.
"""

"""
1. Create a list to store the values from the matrix.
2. Sort the values by the number of times they occure.
3. Add the values to a new matrix with the most frequent in the upper left 
corner.
4. Return the new matrix.
"""

from collections import Counter


def sortMatrixByOccurrences(m):
	vals = []
	for i in range(len(m)):
		for j in range(len(m[i])):
			vals.append(m[i][j])

	print(f'vals list: {vals}')

	sort_vals = [item for items,
	                      c in Counter(vals).most_common() for item in [
		items] * c]

	sort_mat = m.copy()

	for i in range(len(sort_vals)):
		for vals in range(len(sort_mat)):
			if sort_vals[i] not in sort_mat[vals]:
				sort_mat[vals].append(sort_vals[i:len(sort_mat[vals])])

	print(f'sort_vals list: {sort_vals}')

	return sort_mat


# Testing:
if __name__ == '__main__':
	m = [[1, 4, -2],
	     [-2, 3, 4],
	     [3, 1, 3]]
	ans = [[3, 3, 4],
	       [3, 4, 1],
	       [1, -2, -2]]
	if sortMatrixByOccurrences(m) == ans:
		print(f'PASSED! The answer is: {ans}')
	else:
		print(f'Your Output: {sortMatrixByOccurrences(m)}')
		print(f'Correct Output: {ans}')

	m = [[3, 2, -2],
	     [-2, 4, 6],
	     [1, 2, 3]]
	ans = [[3, 3, 2],
	       [2, -2, 6],
	       [-2, 4, 1]]
	if sortMatrixByOccurrences(m) == ans:
		print(f'PASSED! The answer is: {ans}')
	else:
		print(f'Your Output: {sortMatrixByOccurrences(m)}')
		print(f'Correct Output: {ans}')
