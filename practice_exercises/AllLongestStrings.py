"""
Given an array of strings, return another array containing all of
	its longest strings.

Example:

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be:
	allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.string inputArray
	A non-empty array.

	Guaranteed constraints:
		1 ≤ inputArray.length ≤ 10,
		1 ≤ inputArray[i].length ≤ 10.

[output] array.string
	Array of the longest strings, stored in the same order as in the inputArray.
"""

"""
Plan:
1. Create a list to hold the results.
2. Iterate through the list of strings to get the max length
3. Append only the strings that are the max length to the results list.
4. Return the results list.
"""


def allLongestStrings(inputArray):
	# Create a list to hold the valid strings
	results = []
	# Get all the lengths of the strings in the given array
	arr_lens = [len(inputArray[x]) for x in range(len(inputArray))]
	# Get the max length of the strings
	max_len = max(arr_lens)

	# Iterate through the given array
	for i in range(len(inputArray)):
		# If the length of the current string is the max_len
		if len(inputArray[i]) == max_len:
			# Add string to the results list
			results.append(inputArray[i])

	# Return the results list
	return results
