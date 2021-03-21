"""
You are given an array of integers `a` and two integers `l` and `r`.
You task is to calculate a boolean array `b`, where `b[i] = true` if there
	exists an integer `x`, such that `a[i] = (i + 1) * x` and `l ≤ x ≤ r`.
	Otherwise, `b[i]` should be set to `false`.

Example:

For `a = [8, 5, 6, 16, 5]`, `l = 1`, and `r = 3`,
	the output should be
	boundedRatio(a, l, r) = `[false, false, true, false, true]`.

	For `a[0] = 8`, we need to find a value of `x` such that `1 * x = 8`,
		but the only value that would work is `x = 8` which doesn't satisfy
		the boundaries `1 ≤ x ≤ 3`, so `b[0] = false`.
	For `a[1] = 5`, we need to find a value of `x` such that `2 * x = 5`,
		but there is no integer value that would satisfy this equation,
		so `b[1] = false`.
	For `a[2] = 6`, we can choose `x = 2` because `3 * 2 = 6` and `1 ≤ 2 ≤ 3`,
		so `b[2] = true`.
	For `a[3] = 16`, there is no an integer `1 ≤ x ≤ 3`, such that `4 * x = 16`,
		so `b[3] = false`.
	For `a[4] = 5`, we can choose `x = 1` because `5 * 1 = 5` and `1 ≤ 1 ≤ 3`,
		so `b[4] = true`.

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
output --> [false, false, true, false, true]

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
	b = []  # empty list to hold the boolean values

	for i in range(len(a)):  # iterate through array `a`
		x = a[i] / (i + 1)  # find the value for `x`

		if a[i] % (i + 1) == 0 and l <= x <= r:  # if the condition is `True`
			b.append(True)

		else:  # if the condition above is `False`
			b.append(False)

	return b  # return the list of boolean values
