"""
You are given an array of arrays a. Your task is to group the arrays a[i] by
their mean values, so that arrays with equal mean values are in the same
group, and arrays with different mean values are in different groups.

Each group should contain a set of indices (i, j, etc), such that the
corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set
of groups as an array of arrays, where the indices within each group are
sorted in ascending order, and the groups are sorted in ascending order of
their minimum element.

Example

For

a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]
the output should be

meanGroups(a) = [[0, 4],
                 [1],
                 [2, 3]]
mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
mean(a[1]) = (4 + 4) / 2 = 4;
mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
mean(a[3]) = (2 + 3) / 2 = 2.5;
mean(a[4]) = (3 + 3 + 3) / 3 = 3.
There are three groups of means: those with mean 2.5, 3, and 4. And they form
the following groups:

Arrays with indices 0 and 4 form a group with mean 3;
Array with index 1 forms a group with mean 4;
Arrays with indices 2 and 3 form a group with mean 2.5.
Note that neither

meanGroups(a) = [[0, 4],
                 [2, 3],
                 [1]]
nor

meanGroups(a) = [[0, 4],
                 [1],
                 [3, 2]]
will be considered as a correct answer:

In the first case, the minimal element in the array at index 2 is 1, and it
is less then the minimal element in the array at index 1, which is 2.
In the second case, the array at index 2 is not sorted in ascending order.
For

a = [[-5, 2, 3],
     [0, 0],
     [0],
     [-100, 100]]
the output should be

meanGroups(a) = [[0, 1, 2, 3]]
The mean values of all of the arrays are 0, so all of them are in the same
group.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

An array of arrays of integers.

Guaranteed constraints:
1 ≤ a.length ≤ 100,
1 ≤ a[i].length ≤ 100,
-100 ≤ a[i][j] ≤ 100.

[output] array.array.integer

An array of arrays, representing the groups of indices.
"""


def meanGroups(a):
	"""
	Understanding:
	- Given a 2d array
	- Need to get each group's mean values
	- Group arrays with equal mean values and arrays with different mean
	values in different groups
	- The 2d array that I need to return is going to be of the index locations
	of the similar and different means.
	"""
	from statistics import mean

	if a is None:
		return [[]]

	groups = [[]]
	avg = []

	for i in range(len(a)):
		avg.append(mean(a[i]))

	for j in range(len(avg)):
		if avg[j] not in set(avg):
			groups.append(j)
			print(groups)

		else:
			groups[0].append(j)

	return groups


# Testing:
if __name__ == '__main__':
	# Test 1
	a = [[3, 3, 4, 2],
	     [4, 4],
	     [4, 0, 3, 3],
	     [2, 3],
	     [3, 3, 3]]
	ans = [[0, 4],
	       [1],
	       [2, 3]]
	if ans == meanGroups(a):
		print(f'PASSED!')
	else:
		print(f'Failed: Correct Output: {ans}')

	# Test 2
	a = [[-5, 2, 3],
	     [0, 0],
	     [0],
	     [-100, 100]]
	ans = [[0, 1, 2, 3]]
	if ans == meanGroups(a):
		print(f'PASSED!')
	else:
		print(f'Failed: Correct Output: {ans}')

	# Test 3
	a = [[100]]
	ans = [[0]]
	if ans == meanGroups(a):
		print(f'PASSED!')
	else:
		print(f'Failed: Correct Output: {ans}')

	# Test 4
	a = [[2, 2, -3],
	     [1],
	     [-10],
	     [7]]
	ans = [[0],
	       [1],
	       [2],
	       [3]]
	if ans == meanGroups(a):
		print(f'PASSED!')
	else:
		print(f'Failed: Correct Output: {ans}')

	# Test 5
	a = [[-2, 4, 7, -6, 2, -5, 3],
	     [-1, 0, 0, 0],
	     [2, 2, -6, 17, 9, -22, 30, -16, 0, -1, -11, 6, 0, -4],
	     [3, 3, -8, -2, 3]]
	ans = [[0, 2],
	       [1],
	       [3]]
	if ans == meanGroups(a):
		print(f'PASSED!')
	else:
		print(f'Failed: Correct Output: {ans}')

	# Test 6
	a = [[-1,0,0,0,0],
	     [-1,1],
	     [1],
	     [1,1,1,0,1],
	     [-1,-1,1,0],
	     [1,-1],
	     [0,0],
	     [0,-1,1,0],
	     [1,-1,1,1,0,-1,1]]
	ans = [[0],
	       [1, 5, 6, 7],
	       [2],
	       [3],
	       [4],
	       [8]]
	if ans == meanGroups(a):
		print(f'PASSED!')
	else:
		print(f'Failed: Correct Output: {ans}')

	# Test 7
	a = [[0],
	     [0,0],
	     [0,1],
	     [1,1,0,1,1],
	     [1,0],
	     [1],
	     [0],
	     [0,0,1,0,1,0],
	     [1,0,0,1],
	     [1,1,1],
	     [0,0,0],
	     [1,1],
	     [0,1,0,0,1]]
	ans = [[0,1,6,10],
	       [2,4,8],
	       [3],
	       [5,9,11],
	       [7],
	       [12]]
	if ans == meanGroups(a):
		print(f'PASSED!')
	else:
		print(f'Failed: Correct Output: {ans}')
