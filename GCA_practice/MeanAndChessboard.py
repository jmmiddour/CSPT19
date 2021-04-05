"""
You are given a matrix of integers matrix of size n × m and a list of queries queries. The given matrix is colored in black and white in a checkerboard style - the top left corner is colored white and any two side-neighboring cells have opposite colors.

[matrix colouring](https://codesignal.s3.amazonaws.com/tasks
/meanAndChessboard/img/meanAndChessboard.png?_tm=1581452749370)

Each query is represented as a pair of indices (i, j). For each query, perform the following operations:

Select the ith-smallest value among the black cells. In case of a tie, select the one with the lower row number. If there is still a tie, select the one with the lower column number;
Select the jth-smallest white cell using the same process;
Find the average value of these two cells;
If the average value is a whole integer, replace both of the selected cells with the found average value;
Otherwise, replace the cell of the greater value with the average rounded up to the nearest integer, and replace the cell of the smaller value with the average rounded down to the nearest integer.
Your task is to return the resulting matrix after processing all the queries.

Example

For

matrix = [[2, 0, 4],
          [2, 8, 5],
          [6, 0, 9],
          [2, 7, 10],
          [4, 3, 4]]
and queries = [[0, 0], [1, 3]], the output should be

meanAndChessboard(matrix, queries) = [[1, 2, 4],
                                      [2, 8, 5],
                                      [6, 0, 9],
                                      [2, 7, 10],
                                      [4, 3, 3]]
[example 1](https://codesignal.s3.amazonaws.com/tasks/meanAndChessboard/img/meanAndChessboard1.gif?_tm=1581452749886)

The average of the 0th black cell and the 0th white cell is (0 + 2) / 2 = 1, so both cells are replaced with 1.
The average of the 1st black cell and the 3rd white cell is (1 + 4) / 2 = 2.5, so the 1 is replaced with floor(2.5) = 2 and the 4 is replaced with ceil(2.5) = 3.
For

matrix = [[1, 9, 10, 8],
          [3, 4, 4, 4]]
and queries = [[2, 3], [3, 2]], the output should be

meanAndChessboard(matrix, queries) = [[1, 9, 9, 7],
                                      [3, 4, 4, 6]]
[example 2](https://codesignal.s3.amazonaws.com/tasks/meanAndChessboard/img/meanAndChessboard2.gif?_tm=1581452750493)

The average of the 2nd black cell and the 3rd white cell is (8 + 10) / 2 = 9, so both cells are replaced with 9.
The average of the 3rd black cell and the 2nd white cell is (9 + 4) / 2 = 6.5, so the 9 is replaced with ceil(6.5) = 7 and the 4 is replaced with floor(6.5) = 6.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

A matrix of integers.

Guaranteed constraints:
2 ≤ matrix.length ≤ 30,
2 ≤ matrix[i].length ≤ 30,
0 ≤ matrix[i][j] ≤ 1000.

[input] array.array.integer queries

A matrix of integers representing queries. Each row has length 2 and represents a single query. It's guaranteed that all the indices in all the queries are valid.

Guaranteed constraints:
1 ≤ queries.length ≤ 500,
queries[i].length = 2.

[output] array.array.integer

The resulting matrix after processing all the queries in the order they appear in queries.
"""

def meanAndChessboard(matrix, queries):



"""
Tests from CodeSignal:

Test 1
Input:
matrix:
[[2,0,4],
 [2,8,5],
 [6,0,9],
 [2,7,10],
 [4,3,4]]
queries:
[[0,0],
 [1,3]]
Expected Output:
[[1,2,4],
 [2,8,5],
 [6,0,9],
 [2,7,10],
 [4,3,3]]

 Test 2
Input:
matrix:
[[1,9,10,8],
 [3,4,4,4]]
queries:
[[2,3],
 [3,2]]
Expected Output:
[[1,9,9,7],
 [3,4,4,6]]

Test 3
Input:
matrix:
[[3,19],
 [20,16],
 [7,8],
 [8,9]]
queries:
[[0,1],
 [1,2],
 [1,3],
 [0,0]]
Expected Output:
[[5,19],
 [20,12],
 [7,6],
 [12,9]]
"""