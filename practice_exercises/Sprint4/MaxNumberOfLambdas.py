"""
Given a string text, you need to use the characters of text to form as
	many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda"
	that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1

Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2

Example 3:

Input: text = "sctlamb"
Output: 0

Notes:
	text consists of lowercase English characters only

[execution time limit] 4 seconds (py3)

[input] string text

[output] integer
"""


# def csMaxNumberOfLambdas(text):
# 	# Create a dictionary that will have the letters of "lambda" as the keys
# 	letters = {'l': 0, 'a': 0, 'm': 0, 'b': 0, 'd': 0}
# 	# Create a counter to keep track of how many "Lambda"'s I can get
# 	counter = 0
#
# 	# Iterate through the string of text
# 	for i in range(len(text)):
# 		# If the current character is l, a, m, b, or d...
# 		if text[i] == 'l' or text[i] == 'a' or text[i] == 'm' or text[
# 			i] == 'b' or text[i] == 'd':
# 			# Increase the value for that key in the dictionary by 1
# 			letters[text[i]] += 1
#
# 	# While key values are > 0
# 	while all(letters.values()) > 0:
# 		# If the value at key (l, m, b, d) >= 1 and value at key(a) >=2...
# 		if letters['l'] >= 1 and letters['m'] >= 1 and letters['b'] >= 1 and \
# 				letters['d'] >= 1 and letters['a'] >= 2:
# 			# Increment the counter by 1
# 			counter += 1
# 			# Decrement the value at key (l, m, b, d) by 1
# 			letters['l'] -= 1
# 			letters['m'] -= 1
# 			letters['b'] -= 1
# 			letters['d'] -= 1
# 			# Decrement the value at key (a) by 2
# 			letters['a'] -= 2
#
# 	# Return the counter
# 	return counter


###########################################################################
# ################# Another Little Cleaner Solution ##################### #
###########################################################################

def csMaxNumberOfLambdas(text):
	# Create a dictionary that will have the letters of "lambda" as the keys
	letters = {'l': 0, 'a': 0, 'm': 0, 'b': 0, 'd': 0}
	# Create a counter to keep track of how many "Lambda"'s I can get
	counter = 0

	# Iterate through the string of text
	for i in range(len(text)):
		# If the current character is l, a, m, b, or d...
		if text[i] in letters.keys():
			# Increase the value for that key in the dictionary by 1
			letters[text[i]] += 1

	# While key values are > 0
	while all(letters.values()) > 0:
		# If the value at key (l, m, b, d) >= 1 and value at key(a) >=2...
		if (letters['l'] and letters['m'] and letters['b'] and letters[
			'd']) >= 1 and letters['a'] >= 2:
			# Increment the counter by 1
			counter += 1
			# Decrement the value at key (l, m, b, d) by 1
			letters['l'] -= 1
			letters['m'] -= 1
			letters['b'] -= 1
			letters['d'] -= 1
			# Decrement the value at key (a) by 2
			letters['a'] -= 2

	# Return the counter
	return counter


# Testing:
if __name__ == '__main__':
	# Test 1
	text = "mbxcdatlas"
	ans = 1
	if csMaxNumberOfLambdas(text) == ans:
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed!\n  Your Output: {csMaxNumberOfLambdas(text)}\n'
		      f'  Correct Output: {ans}\n')

	# Test 2
	text = "lalaaxcmbdtsumbdav"
	ans = 2
	if csMaxNumberOfLambdas(text) == ans:
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2 Failed!\n  Your Output: {csMaxNumberOfLambdas(text)}\n'
		      f'  Correct Output: {ans}\n')

	# Test 3
	text = "sctlamb"
	ans = 0
	if csMaxNumberOfLambdas(text) == ans:
		print('Test 3 PASSED!!!')
	else:
		print(f'Test 3 Failed!\n  Your Output: {csMaxNumberOfLambdas(text)}\n'
		      f'  Correct Output: {ans}')
