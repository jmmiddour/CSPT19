"""
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing
	at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
Example 2:

Input: [1,2,1,2,1,2,80]
Output: 80
Note: You should be able to develop a solution that has O(n) time complexity.

[execution time limit] 4 seconds (py3)

[input] array.integer nums

[output] integer
"""


def csFindTheSingleNumber(nums):
	"""
	Understanding:
		- Given a NON-EMPTY list of ints
		- Need to return the only number that appears only 1 time
	"""
	# Create a dictionary to keep track of how many times a value is seen
	vals = {nums[0]: 0}

	# Iterate through the list of ints
	for i in nums:
		# Each time a value is seen, add a 1 to the value at that key
		if i in vals.keys():
			vals[i] = vals[i] + 1

		# If value has not been seen yet, create key with value of 1
		else:
			vals[i] = 1

	# Return the only key that has a 1 for it's value
	# Iterate through the key value pairs in vals
	for key, _ in vals.items():
		# If the current key has a value of 1...
		if vals[key] == 1:
			# Return that key
			return key


# Testing
if __name__ == '__main__':
	# Test 1
	nums = [2, 2, -3, 2]
	ans = -3
	if ans == csFindTheSingleNumber(nums):
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed!\n  Your Output: '
		      f'{csFindTheSingleNumber(nums)}\n Correct Output: {ans}\n')

	# Test 2
	nums = [0, 1, 0, 1, 0, 1, 99]
	ans = 99
	if ans == csFindTheSingleNumber(nums):
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2 Failed!\n  Your Output: '
		      f'{csFindTheSingleNumber(nums)}\n Correct Output: {ans}\n')
