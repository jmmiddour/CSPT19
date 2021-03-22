"""
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

Examples:

`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string
"""

"""
Plan:
Return the input string with only unique values (words).

Tried to use set but that did not return the first instance of a word. It 
returned all the unique values but not in the correct order.
"""


def csRemoveDuplicateWords(input_str):
	input_list = input_str.split(' ')
	result = []

	for i in range(len(input_list)):
		if input_list[i] not in result:
			result.append(input_list[i])

	return ' '.join(result)