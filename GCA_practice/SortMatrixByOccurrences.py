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
2. Sort the values by the number of times they occur.
3. Add the values to a new matrix with the most frequent in the upper left 
corner.
4. Return the new matrix.

For a 3 x 3 matrix:
The order for each value to be replaced by sorted value:
    0 | 1 | 2
0 [ 9 | 8 | 6 ]
1 [ 7 | 5 | 3 ]
2 [ 4 | 2 | 1 ]

For row[i] col[j] = [i][j] starting at [2][2]
1. [2][2] = [i]   [j]
2. [2][1] = [i]   [j-1]
3. [1][2] = [i-1] [j]
4. [2][0] = [i]   [j-2]
5. [1][1] = [i-1] [j-1]
6. [0][2] = [i-2] [j]
7. [1][0] = [i-1] [j-2]
8. [0][1] = [i-2] [j-1]
9. [0][0] = [i-2] [j-2]

For a 5 x 5 matrix:
The order for each value to be replaced by sorted value:
    0  | 1  | 2  | 3  | 4
0 [ 25 | 24 | 22 | 19 | 15 ]
1 [ 23 | 21 | 18 | 14 | 10 ]
2 [ 20 | 17 | 13 | 9  | 6  ]
3 [ 16 | 12 | 8  | 5  | 3  ]
4 [ 11 | 7  | 4  | 2  | 1  ]

For row[i] col[j] = [i][j] starting at [4][4]
1 . [4][4] = [i]   [j]
2 . [4][3] = [i]   [j-1]
3 . [3][4] = [i-1] [j]
4 . [4][2] = [i]   [j-2]
5 . [3][3] = [i-1] [j-1]
6 . [2][4] = [i-2] [j]
7 . [4][1] = [i]   [j-3]
8 . [3][2] = [i-1] [j-2]
9 . [2][3] = [i-2] [j-1]
10. [1][4] = [i-3] [j]
11. [4][0] = [i]   [j-4]
12. [3][1] = [i-1] [j-3]
13. [2][2] = [i-2] [j-2]
14. [1][3] = [i-3] [j-1]
15. [0][4] = [i-4] [j]
16. [3][0] = [i-1] [j-4]
17. [2][1] = [i-2] [j-3]
18. [1][2] = [i-3] [j-2]
19. [0][3] = [i-4] [j-1]
20. [2][0] = [i-2] [j-4]
21. [1][1] = [i-3] [j-3]
22. [0][2] = [i-4] [j-2]
23. [1][0] = [i-3] [j-4]
24. [0][1] = [i-4] [j-3]
25. [0][0] = [i-4] [j-4]
"""

from collections import Counter


def sortMatrixByOccurrences(m):
	no_rows = len(m)
	no_cols = len(m[0])

	print(f'Rows: {no_rows} x Columns: {no_cols}\n')

	vals = []
	for row in range(no_rows):
		for col in range(no_cols):
			vals.append(m[row][col])

	print(f'vals list: {vals}\n')

	sort_vals = sorted(sorted(vals), key=Counter(vals).get)

	print(f'sort_vals list: {sort_vals}\n')

	sort_mat = [[0] * no_cols] * no_rows

	print(f'Sorted Matrix: {sort_mat}\n')

	for i in range(len(sort_vals)):
		# for vals in range(len(sort_mat)):
		# 	if sort_vals[i] not in sort_mat[vals]:
		# 		sort_mat[vals] = sort_vals[i:no_cols]


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
		print(f'PASSED! The answer is: {ans}\n')
	else:
		print(f'Your Output: {sortMatrixByOccurrences(m)}')
		print(f'Correct Output: {ans}\n')

	m = [[3, 2, -2, 5],
	     [-2, 4, 6, 5],
	     [1, 2, 3, 3],
	     [2, 5, 6, 1]]
	ans = [[2, 2, 2, 5],
	       [2, 5, 3, 6],
	       [5, 3, 6, 1],
	       [3, 1, 4, -2]]
	if sortMatrixByOccurrences(m) == ans:
		print(f'PASSED! The answer is: {ans}\n')
	else:
		print(f'Your Output: {sortMatrixByOccurrences(m)}')
		print(f'Correct Output: {ans}\n')
