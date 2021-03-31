"""
Given a string sequence consisting of the characters
	'(', ')', '[', ']', '{', and '}'.
Your task is to determine whether or not the sequence
	is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

- An empty bracket sequence is a valid bracket sequence.
- If S is a valid bracket sequence then (S), [S] and {S} are also valid.
- If A and B are valid bracket sequences then AB is also valid.

Example:

- For sequence = "()", the output should be:
	validBracketSequence(sequence) = true;

- For sequence = "()[]{}", the output should be:
	validBracketSequence(sequence) = true;

For sequence = "(]", the output should be:
	validBracketSequence(sequence) = false;

For sequence = "([)]", the output should be:
	validBracketSequence(sequence) = false;

For sequence = "{[]}", the output should be:
	validBracketSequence(sequence) = true.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] string sequence
	A bracket sequence, consisting of the characters (, ), [, ], {, and }.

	Guaranteed constraints:
		0 ≤ sequence.length ≤ 106.

[output] boolean
	true if sequence is a valid bracket sequence and false otherwise.
"""

"""
Test Cases:
sequence = "(]"
output ---> False

sequence = "([{}])"
output ---> True

sequence = "(]})"
output ---> False

Plan:
1. Return True if sequence is empty
2. Check if i is the opposite of i + 1, remove if it is.
3. Return if the final sequence is empty.
"""


# My Code:
def validBracketSequence(sequence):
	# Check if the sequence is an empty string
	if sequence == '':
		return True

	# Create a result list
	result = []
	# Assign a variable to the left brackets
	left = ['(', '[', '{']
	# Assign a variable to the right brackets
	right = [')', ']', '}']
	# Create a dict with matching brackets as key and value
	match = {'(': ')', '[': ']', '{': '}'}

	# Check if the first char is in right or odd length
	if sequence[0] in right or len(sequence) % 2 != 0:
		return False

	# Iterate through the sequence to find matches
	for i in range(len(sequence)):
		# If the char is in the left bracket list
		if sequence[i] in left:
			# Append the char to the result list
			result.append(sequence[i])

		# If the char is in the right bracket list
		elif sequence[i] in right:
			# If not already in result or match at result.pop
			#   does not = char
			if not result or match[result.pop()] != sequence[i]:
				return False

	# Return if there are any left in result or not
	return len(result) == 0


# # Steve's Code:
# def validBracketSequence(sequence):
# 	while len(sequence) > 0:
# 		temp = sequence
# 		sequence = sequence.replace('()', '')
# 		sequence = sequence.replace('[]', '')
# 		sequence = sequence.replace('{}', '')
# 		if temp == sequence:
# 			return False
# 	return True
