"""
You are given a sorted array in ascending order that is rotated at some
	unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2])
	and a target value.

Write a function that returns the target value's index.
If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

	Input: nums = [4,5,6,7,0,1,2], target = 0
	Output: 4

Example 2:

	Input: nums = [4,5,6,7,0,1,2], target = 3
	Output: -1

[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""

"""
Create a helper function to recurse through the nums with a binary search 
algoritm. Return the index location of the target if in the nums list or -1 
if not found.
"""


def findValueSortedShiftedArray(nums, target):
	# Check edge case of only one value in list
	if len(nums) < 2:
		# If the only value is equal to the target
		if nums[0] == target:
			# Return 0 index location
			return 0

		# Else, target not found, return -1
		return -1

	# Need to find the pivot point
	pivot = nums[-1]

	# Find the lowest value's index location
	low = (len(nums) - 1) - pivot

	# Use my helper function to search both halves of the list using recursion
	return helper(nums, target, low, 0, len(nums) - 1, low - 1)


# Define my helper function
def helper(nums, target, r_start=0, l_start=0, r_end=0, l_end=0):
	# If target is less than or equal to the highest value on the right
	if nums[r_end] >= target:
		# Assign the start and end index locations
		start, end = r_start, r_end

		# If start is greater than end, target not found
		if start > end:
			return -1

		# Get the middle index location
		mid = (start + end) // 2

		# Check if the target is at the start, middle, or end
		if nums[start] == target or nums[mid] == target or nums[end] == target:
			# If the target is at the start index
			if nums[start] == target:
				# Return the start index
				return start

			# If the target is at the middle index
			elif nums[mid] == target:
				# Return the middle index
				return mid

			# If the target is at the end index
			else:
				# Return the end index
				return end

		# Create a binary search algorithm
		elif nums[mid] > target:
			return helper(nums, target, r_start=start, r_end=mid - 1)

		else:
			return helper(nums, target, r_start=mid + 1, r_end=end)

	# If target is less than or equal to the lowest value on the left
	if nums[l_start] <= target:
		# Assign the start and end index locations
		start, end = l_start, l_end

		# If start is greater than end, target not found
		if start > end:
			return -1

		# Get the middle index location
		mid = (start + end) // 2

		# Check if the target is at the start, middle, or end
		if nums[start] == target or nums[mid] == target or nums[end] == target:
			# If target at the start index
			if nums[start] == target:
				# Return the start index
				return start

			# If the target is at the middle index
			elif nums[mid] == target:
				# Return the middle index
				return mid

			# If the target is at the end index
			else:
				# Return the end index
				return end

		# Create a binary search algorithm
		elif nums[mid] > target:
			return helper(nums, target, l_start=start, l_end=mid - 1)

		else:
			return helper(nums, target, l_start=mid + 1, l_end=end)


# Testing:
if __name__ == '__main__':
	nums = [4, 5, 6, 7, 0, 1, 2]
	target = 0
	ans = 4
	if findValueSortedShiftedArray(nums, target):
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')
