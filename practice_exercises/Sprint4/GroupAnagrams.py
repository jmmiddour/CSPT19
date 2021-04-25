"""
Given an array of strings `strs`, write a function that can group
	the anagrams. The groups should be ordered such that the larger
	groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a
	different word or phrase, typically using all the original
	letters exactly once.

Example 1:

strs = ["apt","pat","ear","tap","are","arm"]
Output: [["apt","pat","tap"],["ear","are"],["arm"]]

Example 2:

strs = [""]
Output: [[""]]

Example 3:

strs = ["a"]
Output: [["a"]]

Notes:

- `strs[i]` consists of lower-case English letters.
- [execution time limit] 4 seconds (py3)
- [input] array.string `strs`
- [output] array.array.string
"""

from itertools import groupby


def csGroupAnagrams(strs):
	"""
	Understanding:
	- `strs`: list of strings
	- Need to sort `strs` list into groups of anagrams
	- The groups need to be sort with the longest group first to the shortest
	group last
	- Need to return the 2d array of groups
	"""
	# Create a results list to hold the groups
	res = []
	# Create a dictionary to hold the anagrams and their index position(s)
	str_dict = {}
	# Create a list of all the words sorted
	sort_strs = [''.join(sorted(x)) for x in strs]

	# Iterate through `strs` to populate the dictionary
	for i, word in enumerate(sort_strs):
		# For each word in the sorted strings, add the index position in a
		# list in the dictionary
		str_dict[word] = str_dict.get(word, []) + [i]

	# Iterate through the strs to compare them to the dictionary
	for key, val in str_dict.items():
		# Iterate through each value set at the keys
		for i in str_dict[key]:
			# Add all the strings from strs in order based on the grouping
			res.append(strs[i])

	# Group the strings by the values being anagrams
	res = [list(group) for key, group in groupby(res, key=sorted)]

	# Return the results list
	return res


# Testing
if __name__ == '__main__':
	# Test 1
	strs = ["apt", "pat", "ear", "tap", "are", "arm"]
	ans = [["apt", "pat", "tap"], ["ear", "are"], ["arm"]]
	if csGroupAnagrams(strs) == ans:
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed!\n  Your Output: {csGroupAnagrams(strs)}\n  '
		      f'Correct Output: {ans}\n')

	# Test 2
	strs = [""]
	ans = [[""]]
	if csGroupAnagrams(strs) == ans:
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2 Failed!\n  Your Output: {csGroupAnagrams(strs)}\n  '
		      f'Correct Output: {ans}\n')

	# Test 3
	strs = ["a"]
	ans = [["a"]]
	if csGroupAnagrams(strs) == ans:
		print('Test 3 PASSED!!!\n')
	else:
		print(f'Test 3 Failed!\n  Your Output: {csGroupAnagrams(strs)}\n  '
		      f'Correct Output: {ans}\n')
