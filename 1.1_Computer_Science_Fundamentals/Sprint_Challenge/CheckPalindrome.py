"""
A palindrome is a word, phrase, number, or another sequence of characters
that reads the same backward or forward. This includes capital letters,
punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:

csCheckPalindrome("racecar") -> true
csCheckPalindrome("anna") -> true
csCheckPalindrome("12345") -> false
csCheckPalindrome("12321") -> true
Notes:

Try to solve this challenge without using the reverse of the input string;
use a for loop to iterate through the string and make the necessary comparisons.
Something like the code below might be your first intuition, but can you
figure out a way to use a for loop instead?
def csCheckPalindrome(input_str):
    return input_str == "".join(reversed(input_str))
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] boolean
"""

"""
Assumptions:
- The given string could have capital letters, punctuation, numbers, 
and other special characters.

* Need to solve without using the reverse of the given string.

Plan:
1. Convert input string to a list of characters.
2. Create a results list to add the oppisite character
3. Iterate over the input string
4. Check for edge case of string being an odd length.
5. Return True if palindrome, False if not.
"""


# Final code that passed all test, both visible and hidden.
def csCheckPalindrome(input_str):
	rev_list = [input_str[x] for x in range(len(input_str))]

	if ''.join(rev_list[::-1]) == input_str:
		return True

	return False

	# ### Much simpler code if I did not need to use the `for` loop ### #
	# return input_str[::-1] == input_str  # Still O(n) time and space


	# ### The above simplified code WORKS too! ### #

	# ### One Found on StackOverflow using a `for` loop ### #
	# for i in range(len(input_str)//2):
	# 	if input_str[i] != input_str[-(i+1)]:
	# 		return False
	# return True
	# ### The above code from StackOverflow WORKS! ### #


	"""
	Tried to use for loop as instructions stated but could not
		get it to work properly. However, I did use a list
		comprehension which is a for loop, but do not think
		that is what was being suggested. If you want to see
		my other code attempting to use a for loop, you can
		view it below this comment.
	"""
	# ### First Attempt: Passed only 2/5 visible test ### #
	# # left = [] * len(input_str) // 2
	# # right = [] * len(input_str) - left
	# str_list = [x for x in range(len(input_str))]
	# results = []
	#
	# for i in range(len(str_list)):
	# 	for j in range(len(str_list)):
	# 		if i == j:
	# 			results.append(str_list[i])
	#
	# 		elif i <= len(str_list) // 2:
	# 			results.append(str_list[-i])
	#
	# 		else:
	# 			results.append(str_list[i])
	#
	# if results == str_list:
	# 	return True
	#
	# return False

	# ### Returned Error: unsupported operand type(s) for //: 'list' and 'int'
	# when I did not have left and right commented out. Once I commented those
	# out, it returned a list of numerical values for the results list ### #


	# ### Second Attempt: Passed only 2/5 visible test ### #
	# # left = [] * len(input_str) // 2
	# # right = [] * len(input_str) - left
	# str_list = [input_str[x] for x in range(len(input_str))]
	# results = []
	# print(f'Given String: {input_str}')
	#
	# for i in range(0, len(input_str)//2):
	# 	for j in range(len(input_str), len(input_str) - i):
	# 		if i:
	# 			results.append(input_str[-(i+1)])
	#
	# 		elif i == j:
	# 			results.append(input_str[i])
	#
	# 		else:
	# 			results.append(input_str[j])
	#
	# print(f'Results String: {"".join(results)}')
	#
	# return ''.join(results) == input_str

	# ### Returned list of characters but a large list with the characters
	# repeating where they should not have been and not putting the characters in
	# the proper locations ### #

	# ### Fixed the Above code from my second attempt ### #
	results = []

	for i in range(0, len(input_str)):
		if i <= len(input_str) // 2 + 1:
			results.append(input_str[-(i + 1)])

		elif i == -i:
			results.append(input_str[i])

		else:
			results.append(input_str[i])

	return ''.join(results) == input_str


	# ### Third Attempt: Passed only 2/5 visible test ### #
	# # left = [] * len(input_str) // 2
	# # right = [] * len(input_str) - left
	# str_list = [input_str[x] for x in range(len(input_str))]
	# results = []
	# print(str_list)
	#
	# for i in range(len(str_list)):
	# 	# for j in range(len(str_list)):
	# 	if i == -i+1:
	# 		results.append(str_list[i])
	#
	# 	else:
	# 		if i <= len(str_list) // 2:
	# 			results.append(str_list[- i])
	#
	# 		else:
	# 			results.append(str_list[i])
	#
	# print(results)
	# if results == str_list:
	# 	return True
	#
	# return False

	# ### Returned characters in list but some were duplicated and some of the index
	# locations were off from where they should be ### #


	# ### Forth Attempt: Passed only 2/5 visible test ### #
	# # left = [] * len(input_str) // 2
	# # right = [] * len(input_str) - left
	# str_list = [input_str[x] for x in range(len(input_str))]
	# results = []
	# print(str_list)
	#
	# for i in range(len(str_list) // 2):
	# 	# for j in range(len(str_list)):
	# 	if i == -i+1:
	# 		results.append(str_list[i])
	#
	# 	else:
	# 		if i <= len(str_list) // 2:
	# 			results.append(str_list[-i+1])
	#
	# 		else:
	# 			results.append(str_list[i])
	#
	# print(results)
	# if results == str_list:
	# 	return True
	#
	# return False

	# ### Returned characters in list but only a few of them and not in the
	# proper index location ### #


	# ### Fifth Attempt: Passed only 2/5 visible tests ### #
	# str_list = [input_str[x] for x in range(len(input_str))]
	# results = []
	# print(str_list)
	#
	# for i in range(len(str_list) // 2):
	# 	if str_list[i] == str_list[-i]:
	# 		results.append(True)
	#
	# 	else:
	# 		results.append(False)
	#
	# print(results)
	#
	# for x in range(len(results)):
	# 	if results[x:-1] is True:
	# 		return True
	#
	# 	else:
	# 		return False

	# ### Returned True and False in a list but only a few of them and not
	# correct ### #


	# ### Sixth Attempt: Passed only 2/5 visible tests ### #
	# str_list = [input_str[x] for x in range(len(input_str))]
	# results = []
	# print(str_list)
	#
	# for i in range(len(str_list)):
	# 	if str_list[i] == str_list[-i]:
	# 		results.append(True)
	#
	# 	else:
	# 		results.append(False)
	#
	# print(results)
	#
	# for x in range(len(results)):
	# 	if results[x:-1] is True:
	# 		return True
	#
	# 	else:
	# 		return False

	# ### Returned False in a list of the proper size but all values are False
	# when some should have been True ### #


	# ### Seventh Attempt: Passed only 2/5 visible tests ### #
	# str_list = [input_str[x] for x in range(len(input_str))]
	# results = []
	# print(str_list)
	#
	# for i in range(1, len(str_list)):
	# 	if i == -i:
	# 		results.append(str_list[i])
	#
	# 	else:
	# 		if i <= (len(str_list) // 2):
	#           results.append(str_list[-i])
	#
	#       else:
	#           results.append(str_list[i])
	#
	# print(results)
	#
	# if results == str_list:
	# 	return True
	#
	# return False

	# ### Returned a list of characters in almost the proper order but missing
	# the 1 index value in the center. Plus did not return the values on the
	# right, just the same from the left ### #


	# ### Eighth Attempt: Passed only 2/5 visible tests ### #
	# str_list = [input_str[x] for x in range(len(input_str))]
	# results = []
	# print(str_list)
	#
	# for i in range(1, len(str_list)):
	#         if i <= (len(str_list) / 2):
	#             results.append(str_list[-i])
	#
	#         else:
	#             if i == -(i + 1):
	#                 results.append(str_list[i])
	#
	#             else:
	#                 results.append(str_list[i])
	#
	# print(results)
	#
	# if results == str_list:
	# 	return True
	#
	# return False

	# ### Returned a list of characters in almost the proper order but missing
	# the 1 index value in the center. Plus did not return the values on the
	# right, just the same from the left ### #


if __name__ == '__main__':
	print(f'Test 1: {csCheckPalindrome("racecar")}\nCorrect Answer: True\n')
	print(f'Test 2: {csCheckPalindrome("anna")}\nCorrect Answer: True\n')
	print(f'Test 3: {csCheckPalindrome("12345")}\nCorrect Answer: False\n')
	print(f'Test 4: {csCheckPalindrome("12321")}\nCorrect Answer: True\n')
	print(f'Test 5: '
	      f'{csCheckPalindrome("~=JM!`i!KHW/FGhr|w@d&E_A)%Vl+sK]4:)Q*@r.zCIC!W:DvHN|`aPuXtZ8.|DfT=pyR,uls7afZ&X81ip!/RWh13g!nBUyZFxp")}\nCorrect Answer: False')
