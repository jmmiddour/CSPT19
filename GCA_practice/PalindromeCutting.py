"""
You are given a string s.
Consider the following algorithm applied to this string:

1. Take all the prefixes:
	A prefix is a non-empty string constructed from the
		first few characters of the string.

	For example, string s = "abaca" has five prefixes:

	"a"
	"ab"
	"aba"
	"abac"
	"abaca"
of the string, and choose the longest palindrome:
	A string that doesn't changed when reversed
		(it reads the same backward and forward).

	Examples:

	"eye" is a palindrome
	"noon" is a palindrome
	"decaf faced" is a palindrome
	"taco cat" is not a palindrome (backwards it spells "tac ocat")
	"racecars" is not a palindrome (backwards it spells "sracecar")
between them.

2. If this chosen prefix contains at least two characters, cut this prefix
	from `s` and go back to the first step with the updated string.
	Otherwise, end the algorithm with the current string `s` as a result.

Your task is to implement the above algorithm and return
	its result when applied to string `s`.

Note:
	you can click on the prefixes and palindrome words to see the
		definition of the terms if you're not familiar with them.

Example:

For s = "aaacodedoc", the output should be:
	palindromeCutting(s) = "".

- The initial string s = "aaacodedoc" contains only three prefixes which
	are also palindromes - "a", "aa", "aaa".
- The longest one between them is "aaa", so we cut if from s.
- Now we have string "codedoc". It contains two prefixes which are also
	palindromes - "c" and "codedoc".
- The longest one between them is "codedoc", so we cut if from the current
	string and obtain the empty string.
- Finally the algorithm ends on the empty string, so the answer is "".

For s = "codesignal", the output should be:
    palindromeCutting(s) = "codesignal".
- The initial string s = "codesignal" contains the only prefix, which is also
	palindrome - "c".
- This prefix is the longest, but doesn't contain two characters, so the
	algorithm ends with string "codesignal" as a result.

For s = "", the output should be:
	palindromeCutting(s) = "".

Input/Output:

[execution time limit] 4 seconds (py3)

[input] string s
	A string consisting of English lowercase letters.

	Guaranteed constraints:
		0 ≤ s.length ≤ 1000.

[output] string
	The result of the described algorithm.
"""

"""
- Check for edge case of any empty string, return the empty string
- Iterate through the string if > 2 chars, checking for the longest prefix 
that is a palindrome that is at least 2 chars long.
- Remove the longest prefix if it is a palindrome of at least 2 chars.
- Return the finally string after removing valid palindromes.
"""


# # This is my first solution and it does not pass all test... Needs work!
# def palindromeCutting(s):
# 	max_pal = 0
#
# 	if s == '':
# 		return s
#
# 	# print(f'S before loop: {s}')
#
# 	if s[:-1] == reversed(s[:-1]):
# 		s = s.replace(s, '')
# 		return s
#
# 	# print(f's after 1st if: {s}')
#
# 	for i in range(len(s)):
# 		for j in range(len(s) - 1):
#
# 			if len(s[:j]) > 1 and s[:j] == reversed(s[:j]):
# 				max_pal += 1
#
# 			# print(f'max_pal after 1st if: {max_pal}')
#
# 			if max_pal >= 2 and s[:j] != reversed(s[:j]):
# 				s = s.replace(s[:j - 1], '', 1)
# 				# print(f'S in loop: {s}')
#
# 	return s

##################################################################
# #################### Solution 04-12-2021 ##################### #
##################################################################

# # Can not get this one to pass more than 6 test... Needs work...
# def palindromeCutting(s):
# 	"""
# 	Understanding:
# 	- `s` = str of lowercase English letters
# 	- Need to check each of the "prefixes" to see if they are a palindrome of
# 	at least 2 characters or not.
# 	- Get the largest prefix that is a palindrome of at least 2 characters and
# 	remove it from string `s`
# 	- Continue Checking until no more prefixes left that are valid.
# 	- Return the new string `s`
# 	"""
# 	# Create a max_pal counter to find the max palindrome
# 	max_pal = 0
#
# 	# Check for edge case of an empty string, return '' if True
# 	# Check if the whole string is already a palindrome...
# 	if len(s) < 2:
# 		return s
#
# 	# Iterate through the entire string
# 	for i in range(len(s)):
# 		print(i)
# 		if s == None or s == s[::-1]:
# 			return ''
# 		# print(s[:i + 1], s[:i + 1][::-1])
# 		# Check if the length of prefix is > 1 and a palindrome
# 		if len(s[:i]) > 1 and s[:i] == s[:i][::-1]:
# 			# Increment max_pal
# 			max_pal = i
# 			# print(f'max_pal after if: {max_pal}')
#
# 		# Check if max_pal > 1 and current prefix is not a palindrome
# 		if max_pal >= 2 and s[:i] != s[:i][::-1]:
# 			# If True, remove prefix from `s`
# 			# print(s[:i-1])
# 			s = s[i+1:]
#
# 		# print(f's in loop: {s}')
#
# 	# Return the new string `s`
# 	return s

# # Trying another attempt, using recursion this time
# def palindromeCutting(s):
# 	# Check for edge case of an empty string, return '' if True
# 	# Check if the whole string is already a palindrome...
# 	if s == None or s == s[::-1]:
# 		return ''
#
#
# def max_pal(s, start, end):

# Christopher's solution
def palindromeCutting(s):
	switch = True
	if len(s) <= 1:
		return s
	if s == None or s == s[::-1]:
		return ""

	while switch:
		max_pal = 0
		switch = False
		for i in range(len(s)+1):
			if len(s[:i]) > 1 and s[:i] == s[:i][::-1]:
				max_pal = i
		if max_pal >= 2:
			s = s[max_pal:]
			switch = True

	return s


# Testing
if __name__ == '__main__':
	# Test 1
	s = "aaacodedoc"
	ans = ""
	if ans == palindromeCutting(s):
		print('\nTest 1 PASSED!!!\n')
	else:
		print(f'\nTest 1 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
		      f'Output: {ans}\n')

	# Test 2
	s = "codesignal"
	ans = "codesignal"
	if ans == palindromeCutting(s):
		print('\nTest 2 PASSED!!!\n')
	else:
		print(f'\nTest 2 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
		      f'Output: {ans}\n')

	# Test 3
	s = ""
	ans = ""
	if ans == palindromeCutting(s):
		print('\nTest 3 PASSED!!!\n')
	else:
		print(f'\nTest 3 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
		      f'Output: {ans}\n')

	# Test 4
	s = "a"
	ans = "a"
	if ans == palindromeCutting(s):
		print('\nTest 4 PASSED!!!\n')
	else:
		print(f'\nTest 4 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
		      f'Output: {ans}\n')

	# Test 5
	s = "abbab"
	ans = "b"
	if ans == palindromeCutting(s):
		print('\nTest 5 PASSED!!!\n')
	else:
		print(f'\nTest 5 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
		      f'Output: {ans}\n')

	# # Test 6
	# s = "aaabba"
	# ans = "a"
	# if ans == palindromeCutting(s):
	# 	print('\nTest 6 PASSED!!!\n')
	# else:
	# 	print(f'\nTest 6 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
	# 	      f'Output: {ans}\n')
	#
	# # Test 7
	# s = "aaaaaaab"
	# ans = "b"
	# if ans == palindromeCutting(s):
	# 	print('\nTest 7 PASSED!!!\n')
	# else:
	# 	print(f'\nTest 7 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
	# 	      f'Output: {ans}\n')
	#
	# # Test 8
	# s = "abbaabbaabba"
	# ans = ""
	# if ans == palindromeCutting(s):
	# 	print('\nTest 8 PASSED!!!\n')
	# else:
	# 	print(f'\nTest 8 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
	# 	      f'Output: {ans}\n')
	#
	# # Test 9
	# s = "abababaaab"
	# ans = "b"
	# if ans == palindromeCutting(s):
	# 	print('\nTest 9 PASSED!!!\n')
	# else:
	# 	print(f'\nTest 9 Failed:\nYour Output: {palindromeCutting(s)}\nCorrect '
	# 	      f'Output: {ans}\n')
	#
	# # Test 10
	# s = "bbabbaabaabbbbb"
	# ans = ""
	# if ans == palindromeCutting(s):
	# 	print('\nTest 10 PASSED!!!\n')
	# else:
	# 	print(f'\nTest 10 Failed:\nYour Output:'
	# 	      f' {palindromeCutting(s)}\nCorrect '
	# 	      f'Output: {ans}\n')
