"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

All elements in nums are unique.
The length of nums will be <= 100
The value of each element in nums will be in the range [1, 10000]
[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""

"""
Plan:
1. Use recursion to iterate over the given list using a helper function
2. Set up the start, end, and middle locations
3. If the target is less tan the middle, reassign the end to the middle - 1 
to search on the left of the middle.
4. If the target is larger than the middle, reassign start to the middle + 1 
to search on the right of middle.
5. If the middle is the target, return that index location.
"""


def csBinarySearch(nums, target):
	# Use helper function to iterate through the list
	return helper(nums, 0, len(nums) - 1, target)


# Create a helper function that I can recursively run
def helper(nums, start, end, target):
	# If the start is greater than the end, no match
	if start > end:
		return -1

	# Set the middle point of the list
	middle = (start + end) // 2

	# If the middle value is equal to the target
	if nums[middle] == target:
		# Return the index location of the middle value
		return middle

	# If the middle value is greater than the target, search the right side of
	# the middle
	elif nums[middle] > target:
		return helper(nums, start, middle - 1, target)

	# If the middle value is less than the target, search to the left of the
	# middle
	else:
		return helper(nums, middle + 1, end, target)
