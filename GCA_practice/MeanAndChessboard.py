"""
You are given a matrix of integers matrix of size n × m and a list of queries.
The given matrix is colored in black and white in a checkerboard style -
	the top left corner is colored white and any two side-neighboring
	cells have opposite colors.

![matrix colouring](https://codesignal.s3.amazonaws.com/tasks/meanAndChessboard/img/meanAndChessboard.png?_tm=1581452749370)

Each query is represented as a pair of indices (i, j).
For each query, perform the following operations:

- Select the ith-smallest value among the black cells. In case of a tie,
	select the one with the lower row number.
	If there is still a tie, select the one with the lower column number;
- Select the jth-smallest white cell using the same process;
- Find the average value of these two cells;
- If the average value is a whole integer, replace both of the selected cells
	with the found average value;
- Otherwise, replace the cell of the greater value with the average rounded
	up to the nearest integer, and replace the cell of the smaller value
	with the average rounded down to the nearest integer.

Your task is to return the resulting matrix after processing all the queries.

Example:

matrix = [[2, 0, 4],
          [2, 8, 5],
          [6, 0, 9],
          [2, 7, 10],
          [4, 3, 4]]
queries = [[0, 0], [1, 3]], the output should be:
	meanAndChessboard(matrix, queries) = [[1, 2, 4],
                                          [2, 8, 5],
                                          [6, 0, 9],
                                          [2, 7, 10],
                                          [4, 3, 3]]
![example 1](https://codesignal.s3.amazonaws.com/tasks/meanAndChessboard/img/meanAndChessboard1.gif?_tm=1581452749886)

- The average of the 0th black cell and the 0th white cell is
	(0 + 2) / 2 = 1, so both cells are replaced with 1.
- The average of the 1st black cell and the 3rd white cell is
	(1 + 4) / 2 = 2.5, so the 1 is replaced with floor(2.5) = 2
	and the 4 is replaced with ceil(2.5) = 3.

matrix = [[1, 9, 10, 8],
          [3, 4, 4, 4]]
queries = [[2, 3], [3, 2]], the output should be:
	meanAndChessboard(matrix, queries) = [[1, 9, 9, 7],
                                          [3, 4, 4, 6]]

![example 2](https://codesignal.s3.amazonaws.com/tasks/meanAndChessboard/img/meanAndChessboard2.gif?_tm=1581452750493)

- The average of the 2nd black cell and the 3rd white cell is
	(8 + 10) / 2 = 9, so both cells are replaced with 9.
- The average of the 3rd black cell and the 2nd white cell is
	(9 + 4) / 2 = 6.5, so the 9 is replaced with ceil(6.5) = 7 and
	the 4 is replaced with floor(6.5) = 6.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix
	A matrix of integers.

	Guaranteed constraints:
		2 ≤ matrix.length ≤ 30,
		2 ≤ matrix[i].length ≤ 30,
		0 ≤ matrix[i][j] ≤ 1000.

[input] array.array.integer queries
	A matrix of integers representing queries. Each row has length 2
		and represents a single query. It's guaranteed that all the
		indices in all the queries are valid.

	Guaranteed constraints:
		1 ≤ queries.length ≤ 500,
		queries[i].length = 2.

[output] array.array.integer
	The resulting matrix after processing all the queries in
		the order they appear in queries.
"""

def meanAndChessboard(matrix, queries):



# Tests from CodeSignal:
if __name__ == '__main__':
	# Test 1
	matrix = [[2,0,4], [2,8,5], [6,0,9], [2,7,10], [4,3,4]]
	queries = [[0,0], [1,3]]
	ans = [[1,2,4], [2,8,5], [6,0,9], [2,7,10], [4,3,3]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')

	# Test 2
	matrix = [[1,9,10,8], [3,4,4,4]]
	queries = [[2,3], [3,2]]
	ans = [[1,9,9,7], [3,4,4,6]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')

	# Test 3
	matrix = [[3,19], [20,16], [7,8], [8,9]]
	queries = [[0,1], [1,2], [1,3], [0,0]]
	ans = [[5,19], [20,12], [7,6], [12,9]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 3 PASSED!!!\n')
	else:
		print(f'Test 3 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')

	# Test 4
	matrix = [[27,20,14,20,14], [19,23,18,28,11], [26,18,30,21,28],
	          [13,21,10,26,10], [13,25,21,10,20]]
	queries = [[6,12]]
	ans = [[27,20,14,20,14], [19,23,18,28,11], [26,24,24,21,28],
	       [13,21,10,26,10], [13,25,21,10,20]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 4 PASSED!!!\n')
	else:
		print(f'Test 4 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')

	# Test 5
	matrix = [[280,161,67,285,364,273], [154,258,98,365,390,223],
	          [84,79,336,55,252,332], [112,111,390,261,284,260],
	          [79,241,111,14,37,216], [32,67,255,344,83,65]]
	queries = [[6,5], [15,15], [0,12], [3,0], [8,11], [17,15]]
	ans = [[280,209,67,285,364,273], [154,210,98,365,390,223],
	       [98,79,336,55,252,338], [98,111,364,138,284,260],
	       [79,241,111,137,60,216], [32,67,255,364,60,65]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 5 PASSED!!!\n')
	else:
		print(f'Test 5 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')

	# Test 6
	matrix = [[19,146,356,390,73,491,236,189,343,357],
	          [405,49,232,306,255,311,9,263,221,295],
	          [190,319,436,484,280,453,386,486,222,201]]
	queries = [[13,2], [5,13], [1,11], [9,12], [4,0], [9,14],
	           [10,13], [2,0], [13,13]]
	ans = [[123,124,429,390,279,491,236,119,350,375],
	       [405,119,309,306,255,229,9,263,221,295],
	       [190,319,393,429,280,453,309,280,222,201]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 6 PASSED!!!\n')
	else:
		print(f'Test 6 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')

	# Test 7
	matrix = [[79,948], [218,148], [310,715], [921,243], [508,24], [737,39],
	          [102,332], [521,338], [863,58], [535,707]]
	queries = [[3,1], [6,9], [9,7], [3,0], [9,4], [6,1], [4,9], [1,3], [0,1],
	           [4,8], [9,9], [9,8], [5,6]]
	ans = [[205,728], [129,86], [184,687], [572,582], [758,86], [737,355],
	       [102,206], [614,338], [572,184], [535,686]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 7 PASSED!!!\n')
	else:
		print(f'Test 7 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')

	# Test 8
	matrix = [[192,300,253,857,409,961], [181,865,288,409,190,460],
	          [839,987,778,583,653,494], [497,615,515,425,836,539],
	          [647,891,746,141,747,363], [142,336,625,822,114,684],
	          [575,958,329,153,487,337]]
	queries = [[0,17], [6,4], [17,11], [5,14], [0,15], [17,10], [2,13], [2,15]]
	ans = [[192,354,253,672,355,961], [414,865,486,409,430,460],
	       [839,987,446,583,653,494], [497,615,515,425,836,539],
	       [414,733,746,437,747,363], [142,336,625,822,446,431],
	       [437,958,329,153,487,337]]
	if ans == meanAndChessboard(matrix, queries):
		print('Test 8 PASSED!!!\n')
	else:
		print(f'Test 8 Failed:\nYour Output: '
		      f'{meanAndChessboard(matrix, queries)}\nCorrect Output: {ans}')
