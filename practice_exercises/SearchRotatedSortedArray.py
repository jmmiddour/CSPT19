"""
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e.,
[1,2,4,5,6,7] might become [4,5,6,7,1,2]).

You should search for target in nums and if found return its index, otherwise
return -1.

Example 1:
Input: nums = [6,7,1,2,3,4,5], target = 1
Output: 2

Example 2:
Input: nums = [6,7,1,2,3,4,5], target = 3
Output: 4

Example 3:
Input: nums = [1], target = 2
Output: -1

Your solution should have better than O(n) time complexity over the number of
items in the list. There is an O(log n) solution. There is also an O(1)
solution.

Note:

1 <= nums.length < 100
1 <= nums[i] <= 100
All values of nums are unique.
Numbers from 1 up to the length of the list will be contained in the list.
[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""

"""
Plan:
1. Use recursion with binary search to iterate through the nums to find the 
target.
2. Create a helper function to use recursion.
3. Return the index location of the target in the pivotted list or -1 it not 
in the list.
"""


def csSearchRotatedSortedArray(nums, target):
	# Check if the given list only has one value
	if len(nums) < 2:
		# Check if the single value equals the target
		if nums[0] == target:
			# Return that value
			return 0

		# Else, return -1, taget not in list
		return -1

	# Find the pivot value
	pivot = nums[-1]
	# Find the lowest value index location
	low = len(nums) - pivot
	# Use my helper function to search both halves of the list
	return helper(nums, target, low, 0, len(nums) - 1, low - 1)


# Define a helper function to search the halves of the pivoted list
def helper(nums, target, r_start=0, l_start=0, r_end=0, l_end=0):
	# If the target is less than or equal to the highest value on the right
	if nums[r_end] >= target:
		# Assign the start and end index locations
		start, end = r_start, r_end

		# If the start is greater than the end, the target was not found
		if start > end:
			# The target value is not in the right list
			return -1

		# Assign the middle index location
		mid = (start + end) // 2

		# If the target is the start, middle, or end value...
		if nums[start] == target or nums[mid] == target or nums[end] == target:
			# If the target value is at the start of the list
			if nums[start] == target:
				# Found the index location for the target, return it.
				return start

			# If the target value is at the middle location
			elif nums[mid] == target:
				# Found the index location for the target, return it.
				return mid

			# If the target value is at the end of the list
			else:
				# Found the index location for the target, return it.
				return end

		# If the target value is less than the value at the middle location
		elif nums[mid] > target:
			# Reassign end to search to the left of middle using recursion
			return helper(nums, target, r_start=start, r_end=mid - 1)

		# If none of the above conditions are met...
		else:
			# Reassign start to search to the right of middle using recursion
			return helper(nums, target, r_start=mid + 1, r_end=end)

	# If target is greater than or equal to the lowest value on the left
	elif nums[l_start] <= target:
		# Assign the start and end index locations
		start, end = l_start, l_end

		# If the start location is greater than the end...
		if start > end:
			# Did not find the target value, return -1
			return -1

		# Assign the middle index location
		mid = (start + end) // 2

		# If the target is the start, middle, or end value...
		if nums[start] == target or nums[mid] == target or nums[end] == target:
			# If the start value is the target value...
			if nums[start] == target:
				# Target has been found, return that index location
				return start

			# If the middle value is the target value...
			elif nums[mid] == target:
				# Target has be found, return that index location
				return mid

			# If the end value is the target value...
			else:
				# Target has been found, return that index location
				return end

		# If the middle value is greater than the target value...
		elif nums[mid] > target:
			# Reassign the end to search to the left of the middle using
			# recursion
			return helper(nums, target, l_start=start, l_end=mid - 1)

		# If none of the conditions above were met...
		else:
			# Reassign the start to search to the right of middle using
			# recursion
			return helper(nums, target, l_start=mid + 1, l_end=end)


if __name__ == '__main__':
	nums1 = [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
	         61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
	         77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
	         93, 94, 95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
	         11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
	         27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
	         43, 44]
	print(f'Test 1 Output: {csSearchRotatedSortedArray(nums1, 48)}\nCorrect: 3')

	nums2 = [83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
	         99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
	         17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
	         33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
	         49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
	         65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
	         81, 82]
	print(f'Test 2 Output: {csSearchRotatedSortedArray(nums2, 90)}\nCorrect: 7')

	nums3 = [3]
	print(f'Test 2 Output: {csSearchRotatedSortedArray(nums3, 5)}\nCorrect: '
	      f'-1')

	nums3 = [5]
	print(f'Test 2 Output: {csSearchRotatedSortedArray(nums3, 5)}\nCorrect: '
	      f'0')
