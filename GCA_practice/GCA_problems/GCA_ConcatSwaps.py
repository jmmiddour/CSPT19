"""
You are given a string `s`, and an array of positive integers `sizes`,
where the sum of all elements of `sizes` is equal to the length of `s`. More
formally, `sizes[0] + sizes[1] + ... + sizes[sizes.length - 1] = s.length`.

Your task is to:
	1. Split the given string `s` into substrings of lengths `sizes[0],
		sizes[1], ... , sizes[sizes.length - 1]` respectively
	2. Swap the obtained substring in pairs: swap the first substring with
		the second one, the third substring with the fourth one, etc. If the
		number of substrings is odd, leave the last substring in place.
	3. Concatenate the swapped substrings back into one string, and return
		the resulting string as the answer.

**Examples:**
- For `s = "descognail"` and `sizes = [3, 2, 3, 1, 1]`, the output should be:
	`concatSwaps(s, sizes) = "codesignal"`.

- For `s = "secondfirst"` and `sizes = [6, 5]`, the output should be:
	`concatSwaps(s, sizes) = "firstsecond"`.

**Input/Output:**
[executrion time limit] 4 seconds (py3)

[input] string s
	A string of lowercase English letters
"""

def concatSwaps(s, sizes):



# Tests:
if __name__ == '__main__':
	# Test 1
	s = "descognail"
	sizes = [3, 2, 3, 1, 1]
	ans = "codesignal"
	if ans == concatSwaps(s, sizes):
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed:\nYour Output: {concatSwaps(s, sizes)}\nCorrect Output: {ans}\n')

	# Test 2
	s = "secondfirst"
	sizes = [6, 5]
	ans = "firstsecond"
	if ans == concatSwaps(s, sizes):
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2:\nYour Output: {concatSwaps(s, sizes)}\nCorrect '
		      f'Output: {ans}\n')
