"""
Given two strings `s` and `t`, both consisting of lowercase English letters
	and digits, your task is to calculate how many ways exactly one digit
	could be removed from one of the strings so that s is
	lexicographically smaller than `t` after the removal.
Note that we are removing only a single instance of a single digit,
	rather than all instances (eg: removing 1 from the string a11b1c
	could result in a1b1c or a11bc, but not abc).

LEXICOGRAPHICAL ORDER (FOR STRINGS):
	A way of sorting strings, similar to alphabetical order but generalized
		to all kinds of characters.

	When comparing two strings, `s` and `t`, we compare each pair of
		characters with equal indices (s[i] and t[i]), starting with i = 0:

	if s[i] < t[i] or if s[i] is undefined, then we conclude that s < t,
	if s[i] > t[i] or if t[i] is undefined, then we conclude that s > t,
	if s[i] = t[i] then we repeat the process by comparing s[i + 1] to t[i + 1].
	If the two strings have equal length and s[i] = t[i] for every character,
		then we conclude that s = t

Examples:

"snow" > "snoring" because the first string contains a greater character at index i = 2
"cat" < "caterpillar" because the first string is undefined at index i = 3

Also note that digits are considered lexicographically smaller than letters.

Example

For s = "ab12c" and t = "1zz456", the output should be removeOneDigit(s, t) = 1.

Here are all the possible removals:

We can remove the first digit from s, obtaining "ab2c". "ab2c" > "1zz456", so we don't count this removal
We can remove the second digit from s, obtaining "ab1c". "ab1c" > "1zz456", so we don't count this removal
We can remove the first digit from t, obtaining "zz456". "ab12c" < "zz456", so we count this removal
We can remove the second digit from t, obtaining "1zz56". "ab12c" > "1zz56", so we don't count this removal
We can remove the third digit from t, obtaining "1zz46". "ab12c" > "1zz46", so we don't count this removal
We can remove the fourth digit from t, obtaining "1zz45". "ab12c" > "1zz45", so we don't count this removal
The only valid case where s < t after removing a digit is "ab12c" < "zz456". Therefore, the answer is 1.

For s = "ab12c" and t = "ab24z", the output should be removeOneDigit(s, t) = 3.

There are 4 possible ways of removing the digit:

"ab1c" < "ab24z"
"ab2c" > "ab24z"
"ab12c" < "ab4z"
"ab12c" < "ab2z"
Three of these cases match the requirement that s < t, so the answer is 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string consisting of lowercase English letters and digits 0..9.

Guaranteed constraints:
1 ≤ s.length ≤ 103.

[input] string t

A string consisting of lowercase English letters and digits 0..9.

Guaranteed constraints:
1 ≤ t.length ≤ 103.

[output] integer

The number of ways to remove exactly one digit from one of the strings so that s is lexicographically smaller than t after the removal.
"""


def removeOneDigit(s, t):
	"""
	- Split the given strings `s` and `t` by character
	- Create a counter to keep track of the valid amount
	- Iterate over each character, removing one a time from `s` then `t` and
	compare if the new `s` string < the `t` string or if the `s` string is <
	the new `t` string.
	- Return the counter
	"""
	count = 0

	if len(s) <= 1 and len(t) > 1:
		count += 1
		return count

	for i in s:
		if i.isdigit():
			new_s = s.replace(i, '', 1)
			print(new_s)
			if new_s < t:
				count += 1

	for j in t:
		if j.isdigit():
			new_t = t.replace(j, '', 1)
			if s < new_t:
				count += 1

	return count

# Testing:
if __name__ == '__main__':
	# Test 1
	s = "ab12c"
	t = "1zz456"
	ans = 1
	if ans == removeOneDigit(s, t):
		print(f'PASSED!')
	else:
		print(f'')

	# Test 2
	s = "ab12c"
	t = "ab24z"
	ans = 3

	# Test 3
	s = "96726"
	t = "9z34c"
	Output:
	ans = 8

	# Test 4
	s = "4u05q"
	t = "ed0r7"
	ans = 4

	# Test 5
	s = "6"
	t = "h"
	ans = 1

	# Test 6
	s = "d"
	t = "6"
	ans = 0

	# Test 7
	s = "5"
	t = "4"
	ans = 1

	# Test 8
	s = "d"
	t = "q"
	ans = 0
