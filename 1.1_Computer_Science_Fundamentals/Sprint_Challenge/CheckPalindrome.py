"""
A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:

csCheckPalindrome("racecar") -> true
csCheckPalindrome("anna") -> true
csCheckPalindrome("12345") -> false
csCheckPalindrome("12321") -> true
Notes:

Try to solve this challenge without using the reverse of the input string; use a for loop to iterate through the string and make the necessary comparisons.
Something like the code below might be your first intuition, but can you figure out a way to use a for loop instead?
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


def csCheckPalindrome(input_str):
	rev_list = [input_str[x] for x in range(len(input_str))]
	# results = []

	print(rev_list)

	if ''.join(rev_list[::-1]) == input_str:
		return True

	return False

"""
Tried to use for loop as intructions stated but could not 
	get it to work properly. However, I did use a list 
	cmprehension which is a for loop, but do not think 
	that is what was being suggested. If you want to see 
	my other code attemping to use a for loop, you can 
	view it below this comment.
"""
# for i in range(1, len(input_str)):
#     if input_str == input_str[::-1]:
#         results.append(True)

#     else:
#         results.append(False)

# print(results)

# for x in range(len(results)):
#     if results[x:-1] is True:
#         return True

#     else:
#         return False

# for i in range(1, len(str_list)):
#     if i <= (len(str_list) / 2):
#         results.append(str_list[-i])

#     else:
#         if i == -(i + 1):
#             results.append(str_list[i])

#         else:
#             results.append(str_list[i])

# print(results)
# if results == str_list:
#     return True

# return False
