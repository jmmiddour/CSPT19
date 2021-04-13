"""
48. Rotate Image (Medium Problem)

You are given an `n x n` 2D matrix representing an image,
	rotate the image by 90 degrees (clockwise).

You have to rotate the image **in-place**, which means you have to
	modify the input 2D matrix directly.
**DO NOT allocate another 2D matrix and do the rotation.**

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output:         [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output:         [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:

Input: matrix = [[1]]
Output:         [[1]]

Example 4:

Input: matrix = [[1,2],[3,4]]
Output:         [[3,1],[4,2]]

Constraints:

- `matrix.length == n`
- `matrix[i].length == n`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`
"""


class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# Get the len of the matrix row
		mat_len = len(matrix)

		# Iterate through half of the rows in the matrix to avoid the 2 meeting
		for i in range((mat_len // 2) + (mat_len % 2)):  # rows
			# Iterate through half of the cols to avoid overwriting already
			# placed values
			for j in range(mat_len // 2):  # cols
				# Create a temp variable to hold the first value looked at
				# Iter 1: matrix[2][0] = 7
				# Iter 2: matrix[1][0] = 4
				temp = matrix[mat_len - 1 - j][i]
				# Rotate 1
				# Iter 1: matrix[2][0] = matrix[2][2] = 9
				# Iter 2: matrix[1][0] = matrix[2][1] = 8
				matrix[mat_len - 1 - j][i] = matrix[mat_len - 1 - i][
					mat_len - j - 1]
				# Rotate 2
				# Iter 1: matrix[2][2] = matrix[0][2] = 3
				# Iter 2: matrix[2][1] = matrix[1][2] = 6
				matrix[mat_len - 1 - i][mat_len - j - 1] = matrix[j][
					mat_len - 1 - i]
				# Rotate 3
				# Iter 1: matrix[0][2] = matrix[0][0] = 1
				# Iter 2: matrix[1][2] = matrix[0][1] = 2
				matrix[j][mat_len - 1 - i] = matrix[i][j]
				# Rotate 4
				# Iter 1: matrix[0][0] = temp = 7
				# Iter 2: matrix[0][1] = temp = 4
				matrix[i][j] = temp
# Iteration is complete, all is rotated!

	"""
	Work through on a 3 x 3 matrix:

	[1  2  3]
	[4  5  6]
	[7  8  9]

	mat_len = 3
		i = 0 --> 2
		j = 0 --> 1

	Iteration 1:
		i = 0
		j = 0
		temp = [3 - 1 - 0][0] = matrix[2][0] = 7
		Rotate 1 = matrix[2][0] = matrix[2][2] = 9
		Rotate 2 = matrix[2][2] = matrix[0][2] = 3
		Rotate 3 = matrix[0][2] = matrix[0][0] = 1
		Rotate 4 = matrix[0][0] = temp = 7
		New Matrix:
			[7  2  1]
			[4  5  6]
			[9  8  3]

	Iteration 2:
		i = 0
		j = 1
		temp = [3 - 1 - 1][0] = matrix[1][0] = 4
		Rotate 1 = matrix[1][0] = matrix[2][1] = 8
		Rotate 2 = matrix[2][1] = matrix[1][2] = 6
		Rotate 3 = matrix[1][2] = matrix[0][1] = 2
		Rotate 4 = matrix[0][1] = temp = 4
		New Matrix:
			[7  4  1]
			[8  5  2]
			[9  6  3]
	Done rotating!
	"""

