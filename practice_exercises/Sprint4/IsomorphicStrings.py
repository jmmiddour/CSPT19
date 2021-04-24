"""
Given two strings `a` and `b`, determine if they are isomorphic.

Two strings are isomorphic if the characters in `a` can be replaced to get `b`.

*All occurrences of a character must be replaced with another character
	while preserving the order of characters. No two characters may map
	to the same character but a character may map to itself.*

Example 1:

a = "odd"
b = "egg"
Output: true

Example 2:

a = "foo"
b = "bar"
Output: false

Example 3:

a = "abca"
b = "zbxz"
Output: true

Example 4:

a = "abc"
b = ""
Output: false

[execution time limit] 4 seconds (py3)

[input] string a

[input] string b

[output] boolean
"""


def csIsomorphicStrings(a, b):
	"""
	Understanding:
	- Given two strings `a` and `b` which could also be an empty string
	- Each unique character in `a` can only be mapped to one character in `b`.
	- A character can be mapped to itself but no two characters can be mapped
	to the same character
	- Example:
		a = 'oddom'
		b = 'eggem'
		Explaination:
			'o' --> 'e'
			'd' --> 'g'
			'm' --> 'm'
			For each 'o' the `b` string must have an 'e' for every place there
			is a 'o' in `a`
	- If the above example was:
		a = 'oddom'
		b = 'eggbm'
		This would be false because for a[3] there is an 'o' but b[3] is not
		an 'e', since the first 'o' was mapped to 'e' the second 'o' must map
		to 'e' in string `b` also.
	- Need to return True or False
	"""
	# Create a dictionary for `a` string
	dict_a = {}
	# Create a dictionary for `b` string
	dict_b = {}
	# Populate dict_a from values in string `a`
	for i, char in enumerate(a):
		# Map the character to its index location(s)
		dict_a[char] = dict_a.get(char, []) + [i]

	# Populate dict_b from valus in string `b`
	for i, char in enumerate(b):
		# Map the character to its index location(s)
		dict_b[char] = dict_b.get(char, []) + [i]

	# print(f'A Dict: {dict_a}\nB Dict: {dict_b}')

	# Return the bool for comparing dict_a sorted to dict_b soorted
	#   This will ensure that the values are in the correct order and that
	#       they are the correct values
	return sorted(dict_a.values()) == sorted(dict_b.values())


# Testing
if __name__ == '__main__':
	# Test 1
	a = "egg"
	b = "add"
	ans = True
	if csIsomorphicStrings(a, b) == ans:
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')

	# Test 2
	a = ""
	b = ""
	ans = True
	if csIsomorphicStrings(a, b) == ans:
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')

	# Test 3
	a = "abc"
	b = ""
	ans = False
	if csIsomorphicStrings(a, b) == ans:
		print('Test 3 PASSED!!!\n')
	else:
		print(f'Test 3 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')

	# Test 4
	a = "oddom"
	b = "eggem"
	ans = True
	if csIsomorphicStrings(a, b) == ans:
		print('Test 4 PASSED!!!\n')
	else:
		print(f'Test 4 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')

	# Test 5
	a = "oddom"
	b = "eggbm"
	ans = False
	if csIsomorphicStrings(a, b) == ans:
		print('Test 5 PASSED!!!\n')
	else:
		print(f'Test 5 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')

	# Test 6
	a = "foo"
	b = "bar"
	ans = False
	if csIsomorphicStrings(a, b) == ans:
		print('Test 6 PASSED!!!\n')
	else:
		print(f'Test 6 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')

	# Test 7
	a = "abca"
	b = "zbxz"
	ans = True
	if csIsomorphicStrings(a, b) == ans:
		print('Test 7 PASSED!!!\n')
	else:
		print(f'Test 7 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')

	# Test 8
	a = "paper"
	b = "title"
	ans = True
	if csIsomorphicStrings(a, b) == ans:
		print('Test 8 PASSED!!!\n')
	else:
		print(f'Test 8 Failed!\n  Your Output: '
		      f'{csIsomorphicStrings(a, b)}\n  Correct Output: {ans}\n')
