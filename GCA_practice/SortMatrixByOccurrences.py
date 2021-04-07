"""
Given a square matrix of integers m, your task is to rearrange its numbers
	in the following way:

- First, sort its values in ascending order of how frequently the number
	occurs in m. In the case of a tie, sort the equally frequent numbers
	by their values, in ascending order.

- Second, place the sorted numbers diagonally, starting from the bottom right
	corner, like this:

![element ordering]https://codesignal.s3.amazonaws.com/tasks/sortMatrixByOccurrences/img/sortMatrixByOccurrences.gif?_tm=1582092096487

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

# from collections import Counter
# # import numpy as np
#
# def sortMatrixByOccurrences(m):
# 	no_rows = len(m)
# 	no_cols = len(m[0])
#
# 	print(f'Rows: {no_rows} x Columns: {no_cols}\n')
#
# 	vals = []
# 	for row in range(no_rows):
# 		for col in range(no_cols):
# 			vals.append(m[row][col])
#
# 	print(f'vals list: {vals}\n')
#
# 	sort_vals = sorted(sorted(vals), key=Counter(vals).get)
# 	sort_vals_rev = sort_vals[::-1]
#
# 	print(f'sort_vals list: {sort_vals}\n')
# 	print(f'sort_vals_rev list: {sort_vals_rev}\n')
#
# 	# sort_mat = [[0] * no_cols] * no_rows
# 	sort_mat = [[] for _ in range(no_rows)]
#
# 	print(f'Sorted Matrix: {sort_mat}\n')
#
# 	counter = 0
# 	for i in range(1, (no_rows * 2)):
# 		len_row = 1
#
# 		if i <= no_rows:
# 			len_row = i
# 			print(f'Length of row in if: {len_row}')
#
# 		else:
# 			len_row = no_rows - (i - no_rows)
# 			print(f'Length of row in else: {len_row}')
#
# 		for j in range(len_row):
# 			sort_mat[i][j] = sort_vals_rev[counter]
# 			counter += 1
# 			print(f'Sorted Matrix: {sort_mat}')
# 		# 	if sort_vals[i] not in sort_mat[vals]:
# 		# 		sort_mat[vals] = sort_vals[i:no_cols]
#
# 	# sort_mat_np = np.fill_diagonal(sort_mat, sort_vals_rev)
# 	# print(f'Sort Matrix with np: {sort_mat_np}')
#
# 	return sort_mat

# from collections import Counter
#
# def sortMatrixByOccurrences(m):
# 	no_rows = len(m)
# 	# no_cols = len(m[0])
# 	vals = []
#
# 	# for row in range(no_rows):
# 	#     for col in range(no_cols):
# 	#         vals.append(m[row][col])
# 	for row in range(no_rows):
# 		vals.extend(m[row])
#
# 	# counted_vals = {}
# 	# for i in vals:
# 	# 	if i in counted_vals:
# 	# 		counted_vals[i] += 1
# 	#
# 	# 	else:
# 	# 		counted_vals[i] = 1
# 	#
# 	# print(counted_vals)
# 	#
# 	# new_dict = {}
# 	# for key, val in counted_vals.items():
# 	# 	if val in new_dict:
# 	# 		new_dict[val].append(key)
# 	#
# 	# 	else:
# 	# 		new_dict[val] = [key]
# 	#
# 	# print(new_dict)
# 	#
# 	# max_items = max(new_dict.keys())
# 	# sort_vals_rev = []
# 	# for i in range(max_items):
# 	# 	if i in new_dict:
# 	# 		print(new_dict)
# 	# 		sorted_vals = sorted(new_dict[i], reverse=True)
# 	# 		print(sorted_vals)
# 	# 		temp_list = []
# 	# 		for j in sorted_vals:
# 	# 			temp_list.extend([j] * i)
# 	# 		sorted_vals_rev2.extend(temp_list)
# 	# 	print(sort_vals_rev)
#
# 	sort_vals = sorted(sorted(vals), key=Counter(vals).get)
# 	sort_vals_rev = sort_vals[::-1]
#
# 	sort_mat = [[] for _ in range(no_rows)]
#
# 	counter = 0
# 	row = 0
#
# 	for i in range(1, (no_rows * 2)):  # 1, 2, 3, 4, 5
# 		if i <= no_rows:  # 1, 2, 3
# 			len_row = i  # 1, 2, 3
#
# 		else:  # 4, 5
# 			len_row = no_rows - (i - no_rows)  # 2, 1
# 			row += 1  # 1, 2
#
# 		for j in range(len_row):  # 1, 2, 3, 2, 1
# 			sort_mat[row + j].append(sort_vals_rev[counter])
# 			counter += 1
#
# 	return sort_mat


# ### Alexis Solution ### #
def order_array(two_d_arr: list) -> list:
	"""
	Sort values of a 2D-array in ascending order of how frequently the number
	occurs in m. In the case of a tie, sort the equally frequent numbers
	by their values, in ascending order.

	:param two_d_array: A 2D-array of any dimension
	:type two_d_array: list
	...
	:return: A flattened properly sorted list
	:rtype: list
	"""

	# Create a dictionary to hold the frequency count as val and
	#   element as the key
	hash_map = {}
	# Essentially doing the same as extend
	flat_list = sum(two_d_arr, [])
	# print(flat_list)

	# counting occurrences
	for num in flat_list:
		# If the num is not already in the dictionary,
		#   it has not been seen yet.
		if num not in hash_map:
			# Add it to the dictionary with num as the key and 1 as the val
			hash_map[num] = 1

		# If the num is already in the dictionary...
		elif num in hash_map:
			# Increment the val by one
			hash_map[num] += 1

	# ordering m hash_map into list
	sort_list = sorted(flat_list, key=lambda num: (hash_map[num], num))
	print(sort_list[::-1])
	return sort_list[::-1]


def calc_diagonals(m: list) -> list:
	"""
	Calculates the diagonals in a symmetrical 2D-array

	:param m: Symmetrical 2D-array
	:type m: list
	...
	:return: ordered list of spots that make up diagonals
	:rtype: list
	"""

	# Get the length of m matrix
	len_m = len(m)
	# Create a counter variable
	counter = 0
	# Get the area of the square matrix m
	num_spots = len_m * len_m
	# Create a pointer for the x axis
	pos_x = 0
	# Create a pointer for the y axis
	pos_y = 0
	# Create a list for the diagonals
	diagonals = []

	# Not sure why this yet?
	is_up = True

	# Continue to iterate while the counter is less than the num_spots
	while counter < num_spots:
		# Not sure why this yet?
		if is_up:
			# Continue iterating while x axis is greater or equal to 0
			#   and y axis is less than the length of m
			while pos_x >= 0 and pos_y < len_m:

				diagonals.append((pos_x, pos_y))
				pos_y += 1
				pos_x -= 1
				counter += 1
				print(f'Dia 1: {diagonals}')

			if pos_x < 0 and pos_y <= (len_m - 1):
				pos_x = 0
				print(f'Dia 2: {diagonals}')

			if pos_y == len_m:
				pos_x += 2
				pos_y -= 1
				print(f'Dia 3: {diagonals}')

		else:
			while pos_y >= 0 and pos_x < len_m:
				diagonals.append((pos_x, pos_y))
				pos_x += 1
				pos_y -= 1
				counter += 1
				print(f'Dia 4: {diagonals}')

			if pos_y < 0 and pos_x <= (len_m - 1):
				pos_y = 0
				# pos_x, pos_y = pos_y, pos_x
				print(f'Dia 5: {diagonals}')

			if pos_x == len_m:
				pos_y += 2
				pos_x -= 1
				print(f'Dia 6: {diagonals}')

		is_up = not is_up

	return diagonals


def sortMatrixByOccurrences(m: list) -> list:
	sorted_array = order_array(m)
	diagonals = calc_diagonals(m)

	# creates empty result array of size m
	result = [[None for i in range(len(m))] for j in range(len(m))]

	index = 0
	for pos_x, pos_y in diagonals:
		try:
			result[pos_x][pos_y] = sorted_array[index]
			index += 1
		except IndexError:
			pass
	return result


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

	# m = [[3, 2, -2, 5],
	#      [-2, 4, 6, 5],
	#      [1, 2, 3, 3],
	#      [2, 5, 6, 1]]
	# ans = [[5, 5, 3, 2],
	#        [5, 3, 2, 6],
	#        [3, 2, 1, -2],
	#        [6, 1, -2, 4]]
	# if sortMatrixByOccurrences(m) == ans:
	# 	print(f'PASSED! The answer is: {ans}\n')
	# else:
	# 	print(f'Your Output: {sortMatrixByOccurrences(m)}')
	# 	print(f'Correct Output: {ans}\n')
