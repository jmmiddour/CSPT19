"""
Given a `pattern` and a string `a`, find if `a` follows the same `pattern`.

Here, "to follow" means a full match, such that there is a one-to-one
	correspondence between a letter in `pattern` and a non-empty word in `a`.

Example 1:

pattern = "abba"
a = "lambda school school lambda"
Output: true

Example 2:

pattern = "abba"
a = "lambda school school coding"
Output: false

Example 3:

pattern = "aaaa"
a = "lambda school school lambda"
Output: false

Example 4:

pattern = "abba"
a = "lambda lambda lambda lambda"
Output: false

Notes:

- `pattern` contains only lower-case English letters.
- `a` contains only lower-case English letters and spaces ' '.
- `a` does not contain any leading or trailing spaces.
- All the words in `a` are separated by a single space.

[execution time limit] 4 seconds (py3)

[input] string pattern

[input] string a

[output] boolean
"""


def csWordPattern(pattern, a):
	"""
	Understanding:
	- `pattern`: string of lowercase characters only
	- `a`: string with lowercase words seperated by a single space
	- Need to compare the `pattern` string to the `a` string of words.
	- Each unique character in the `pattern` string represents a word.
	- Once a character in the `pattern` string is mapped to a word, is that
	character is repeated in the `pattern` string it must be repeated in the
	`a` sting of words.
	- Need to return True or False if the `pattern` matches the string `a`
	"""
	# Create a dictionary to map the characters in the `pattern` to their
	# index location
	pat_dict = {}
	# Turn the string `a` into a list of strings
	a = a.split(' ')
	# Create a dictionary to map the words in the string `a` to there index
	# location
	a_dict = {}

	# Populate the dictionary for `pattern`
	for i, char in enumerate(pattern):
		# Add the index loaction(s) for each character in `pattern`
		pat_dict[char] = pat_dict.get(char, []) + [i]

	# Populate the dictionary for `a`
	for idx, word in enumerate(a):
		# Add the index location(s) for each word in `a`
		a_dict[word] = a_dict.get(word, []) + [idx]

	# Return True or False if the `pattern` matches `a`
	return sorted(pat_dict.values()) == sorted(a_dict.values())


# Testing:
if __name__ == '__main__':
	# Test 1
	pattern = "abba"
	a = "lambda school school lambda"
	ans = True
	if csWordPattern(pattern, a) == ans:
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed!\n  Your Output: '
		      f'{csWordPattern(pattern, a)}\n  Correct Output: {ans}\n')

	# Test 2
	pattern = "abba"
	a = "lambda school school coding"
	ans = False
	if csWordPattern(pattern, a) == ans:
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2 Failed!\n  Your Output: '
		      f'{csWordPattern(pattern, a)}\n  Correct Output: {ans}\n')

	# Test 3
	pattern = "aaaa"
	a = "lambda school school lambda"
	ans = False
	if csWordPattern(pattern, a) == ans:
		print('Test 3 PASSED!!!\n')
	else:
		print(f'Test 3 Failed!\n  Your Output: '
		      f'{csWordPattern(pattern, a)}\n  Correct Output: {ans}\n')

	# Test 4
	pattern = "abba"
	a = "lambda lambda lambda lambda"
	ans = False
	if csWordPattern(pattern, a) == ans:
		print('Test 4 PASSED!!!\n')
	else:
		print(f'Test 4 Failed!\n  Your Output: '
		      f'{csWordPattern(pattern, a)}\n  Correct Output: {ans}\n')

	# Test 5
	pattern = "abc"
	a = "abc"
	ans = False
	if csWordPattern(pattern, a) == ans:
		print('Test 5 PASSED!!!\n')
	else:
		print(f'Test 5 Failed!\n  Your Output: '
		      f'{csWordPattern(pattern, a)}\n  Correct Output: {ans}\n')

	# Test 6
	pattern = "t"
	a = "l"
	ans = True
	if csWordPattern(pattern, a) == ans:
		print('Test 6 PASSED!!!')
	else:
		print(f'Test 6 Failed!\n  Your Output: '
		      f'{csWordPattern(pattern, a)}\n  Correct Output: {ans}')
