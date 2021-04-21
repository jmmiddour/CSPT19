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

def csMaxNumberOfLambdas(text):



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
		print('Test 3 PASSED!!!\n')
	else:
		print(f'Test 3 Failed!\n  Your Output: {csMaxNumberOfLambdas(text)}\n'
		      f'  Correct Output: {ans}')
