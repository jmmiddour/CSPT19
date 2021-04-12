"""
You are given an array of integers `a` and two integers `l` and `r`.
You task is to calculate a boolean array `b`, where `b[i] = True` if there
	exists an integer `x`, such that `a[i] = (i + 1) * x` and `l ≤ x ≤ r`.
	Otherwise, `b[i]` should be set to `False`.

Example:

For `a = [8, 5, 6, 16, 5]`, `l = 1`, and `r = 3`,
	the output should be
	boundedRatio(a, l, r) = `[False, False, True, False, True]`.

	For `a[0] = 8`, we need to find a value of `x` such that `1 * x = 8`,
		but the only value that would work is `x = 8` which doesn't satisfy
		the boundaries `1 ≤ x ≤ 3`, so `b[0] = False`.
	For `a[1] = 5`, we need to find a value of `x` such that `2 * x = 5`,
		but there is no integer value that would satisfy this equation,
		so `b[1] = False`.
	For `a[2] = 6`, we can choose `x = 2` because `3 * 2 = 6` and `1 ≤ 2 ≤ 3`,
		so `b[2] = True`.
	For `a[3] = 16`, there is no an integer `1 ≤ x ≤ 3`, such that `4 * x = 16`,
		so `b[3] = False`.
	For `a[4] = 5`, we can choose `x = 1` because `5 * 1 = 5` and `1 ≤ 1 ≤ 3`,
		so `b[4] = True`.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.integer a
An array of integers.

Guaranteed constraints:
1 ≤ a.length ≤ 100,
1 ≤ a[i] ≤ 106.

[input] integer l
An integer representing the lower bound for x.

Guaranteed constraints:
1 ≤ l ≤ 104.

[input] integer r
An integer representing the upper bound for x.

Guaranteed constraints:
1 ≤ r ≤ 104,
l ≤ r.

[output] array.boolean
A boolean array.
"""

"""
Assumptions:
- `a` length will be from 1 - 100.
- `a` values will be from 1 - 10^6.
- `l` value will be from 1 - 10^4.
- `r` value will be from 1 - 10^4.

Inputs:
`a` = An array of intergers
`l` = An integer that represents the lower bound for `x`
`r` = An integer that represents the upper bound for `x`

Output:
`b` = An array of booleans stating True if `a[i] = (i +1) * x` and `l <= x <= 
r`. 
`x` = the value that you multiple by the index number of the next element in 
the array to get the value at `a[i]`.

Test Cases:
a = [8, 5, 6, 16, 5]
l = 1
r = 3
output --> [False, False, True, False, True]

a = [9, 6, 5, 8]
l = 1
r = 5
worked out --> a[0] = 9 = False, a[1] = 3 = True, a[2] = (can not do 5/3) = 
False, a[3] = 2 = True
output --> [False, True, False, True]

Plan:
1. Create a list to hold boolean values.
2. Iterate through the `a` array to check the values against the formula.
3. Add the boolean value for each index to the boolean list.
4. Return the boolean list.
"""

def boundedRatio(a, l, r):

# 	b = []  # empty list to hold the boolean values
#
# 	for i in range(len(a)):  # iterate through array `a`
# 		x = a[i] / (i + 1)  # find the value for `x`
#
# 		if a[i] % (i + 1) == 0 and l <= x <= r:  # if the condition is `True`
# 			b.append(True)
#
# 		else:  # if the condition above is `False`
# 			b.append(False)
#
# 	return b  # return the list of boolean values


############################################
# ######### 04-12-2021 Solution ########## #
	"""
	Understanding:
	- `a` = array of ints
	- `l` = int: <= x
	- `r` = int: >= x
	- `x` = a[i] = (i + 1) * x
	- `b` = Bool array created by me that will hold the results
	- If `l`<=`x`<=`r` return True in the `b` array for that `a[i]` position.
	"""
	# Create `b` array for holding the bool results
	b = []

	# Iterate through `a` array
	for i in range(len(a)):
		# Get value for x: a[i] = (i + 1) * x
		x = a[i] / (i + 1)

		# Check if `x` is an integer, not a float and if l <= x <= r
		if a[i] % (i + 1) == 0 and l <= x <= r:
			b.append(True)

		# If not True...
		else:
			# Append False to `b` array
			b.append(False)

	# Return the `b` array
	return b

# Testing
if __name__ == '__main__':
	# Test 1
	a = [8, 5, 6, 16, 5]
	l = 1
	r = 3
	ans = [False, False, True, False, True]
	if ans == boundedRatio(a, l, r):
		print('Test 1 PASSED!')
	else:
		print(f'Test 1 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')

	# Test 2
	a = [100]
	l = 1
	r = 1000
	ans = [True]
	if ans == boundedRatio(a, l, r):
		print('Test 2 PASSED!')
	else:
		print(f'Test 2 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')

	# Test 3
	a = [1, 2, 3, 4, 5]
	l = 1
	r = 1
	ans = [True, True, True, True, True]
	if ans == boundedRatio(a, l, r):
		print('Test 3 PASSED!')
	else:
		print(f'Test 3 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')

	# Test 4
	a = [1, 2, 3, 4, 5]
	l = 2
	r = 10000
	ans = [False, False, False, False, False]
	if ans == boundedRatio(a, l, r):
		print('Test 4 PASSED!')
	else:
		print(f'Test 4 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')

	# Test 5
	a = [1000000, 20000]
	l = 10000
	r = 10000
	ans = [False, True]
	if ans == boundedRatio(a, l, r):
		print('Test 5 PASSED!')
	else:
		print(f'Test 5 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')

	# Test 6
	a = [65, 46, 60, 164, 243, 228, 231, 298, 231, 211]
	l = 20
	r = 50
	ans = [False, True, True, True, False, True, True, False, False, False]
	if ans == boundedRatio(a, l, r):
		print('Test 6 PASSED!')
	else:
		print(f'Test 6 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')

	# Test 7
	a = [643, 531, 504, 224, 415, 360, 364, 84, 212, 587]
	l = 70
	r = 80
	ans = [False, False, False, False, False, False, False, False, False, False]
	if ans == boundedRatio(a, l, r):
		print('Test 7 PASSED!')
	else:
		print(f'Test 7 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')

	# Test 8
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
	     20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
	     37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
	l = 1
	r = 10000
	ans = [True, True, True, True, True, True, True, True, True, True, True,
	      True, True, True, True, True, True, True, True, True, True, True,
	       True, True, True, True, True, True, True, True, True, True, True,
	       True, True, True, True, True, True, True, True, True, True, True,
	       True, True, True, True, True]
	if ans == boundedRatio(a, l, r):
		print('Test 8 PASSED!')
	else:
		print(f'Test 8 Failed:\nYour Output: {boundedRatio(a, l, r)}'
		      f'\nCorrect Output: {ans}')
