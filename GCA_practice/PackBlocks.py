"""
You are given array of integers called blocks. Each of the values in this
	array represents the width of a block - the ith block has a height of 1
	and a width of blocks[i] (i.e. it's a 1 x blocks[i] block).

You want to pack all the given blocks into a rectangular container of
	dimensions height x width, according to the following rules:

Place blocks into the container row by row, starting with block 0.
For each row, place the blocks into the container one by one, in the order
	they are given in the blocks array.
If there is not enough space to put the current block in the current row,
	start filling the next row.
You are given the value height of the rectangular container. Your task is
	to find the minimal possible width of a rectangular container in which
	all blocks can fit. Find and return this minimal possible width value.

NOTE:
	The blocks cannot be rotated.

Example:

For blocks = [1, 3, 1, 3, 3] and height = 2, the output should be:
	packBlocks(blocks, height) = 6.

Here's how the blocks should be packed in a container of size 2 x 6:

Note:
 	It wouldn't be possible to fit these blocks in a container that's
		any less wide than 6.

For blocks = [2, 3, 1, 1, 1] and height = 2, the output should be:
	packBlocks(blocks, height) = 5.

Here's how the blocks should be packed in container of size 2 x 5:

It might seem like these blocks could be packed into a container of
	size 2 x 4, but since we must place them in the order they appear
	in the blocks array, the width must be at least 5.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.integer blocks
	An array of integers representing block widths.

	Guaranteed constraints:
		1 ≤ blocks.length ≤ 105,
		1 ≤ blocks[i] ≤ 104.

[input] integer height
	An integer representing the height of the rectangular container.

	Guaranteed constraints:
		1 ≤ height ≤ 109.

[output] integer
	The minimal possible width for the rectangular container to fit
		all the blocks, according to the specifications above.
"""

def packBlocks(blocks, height):
	"""
	Understanding:
	- The "blocks" are an array of integers of the width of each block
	- The "height" is an integer that represents the height of the rectangle
	- Need to return the min width that the rectangle can be to fit all
	blocks in the order they are currently in (such as, if blocks[0] = 3 and
	blocks[1] = 2, then you have 3 more values that are all 1, even though
	the sum of all blocks is 8, which could be done in a width of 4, the min
	width has to be at least 5 because 3 + 2 = 5 and they can not be split
	- If only 1 for height, add all blocks, return the sum as the width
	- If the sum is < the height, return 1
	"""
	# Check for edge case of 1 for the height
	if height == 1:
		# Return the sum of blocks
		return sum(blocks)

	# Check if the height is larger than the sum of blacks
	if sum(blocks) <= height:
		# The width of the rectangle min is 1
		return 1

	# print(f'Blocks: {blocks}')
	# print(f'Sum of blocks: {sum(blocks)}')

	# Get the sum of blocks
	block_div = (sum(blocks) // height) + (sum(blocks) % height)
	# print(f'Block Divided: {block_div}')

	# Check if there is a max value that is larger than the blocks divided
	if max(blocks) > block_div:
		return max(blocks)

	# Check if the first value is greater than the blocks divided
	if blocks[0] >= block_div:
		# print(f'Blocks at 0: {blocks[0]}')
		return blocks[0]

	# Create a variable to keep track of the sum as it iterates
	sum_now = 0

	# Iterate through the blocks to verify the sum/height is not less than
	#   the sum of the values starting at the 0 index
	for i in range(len(blocks)):
		# Check if current sum + current block value is <= the blocks divided
		if (sum_now + blocks[i]) <= block_div:
			# Add the current block value to the sum tracker
			sum_now += blocks[i]

		# Check if the current sum <= the blocks divided and blocks divided
		#   is less than the current sum + the next block value
		elif sum_now <= block_div < (sum_now + blocks[i+1]):
			# Done, can return the block divided value
			return block_div

		# Check if the current sum + current block value is greater than the
		#   block divide
		elif (sum_now + blocks[i]) > block_div:
			# Add the current block value to the sum tracker
			sum_now += blocks[i]
			# Return the new sum
			return sum_now


# Testing
if __name__ == '__main__':
	# Test 1
	blocks = [1, 3, 1, 3, 3]
	height = 2
	ans = 6
	if ans == packBlocks(blocks, height):
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 2
	blocks = [2, 3, 1, 1, 1]
	height = 2
	ans = 5
	if ans == packBlocks(blocks, height):
		print('Test 2 PASSED!!!\n')
	else:
		print(f'Test 2 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 3
	blocks = [4, 1, 1]
	height = 2
	ans = 4
	if ans == packBlocks(blocks, height):
		print('Test 3 PASSED!!!\n')
	else:
		print(f'Test 3 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 4
	blocks = [3]
	height = 2
	ans = 3
	if ans == packBlocks(blocks, height):
		print('Test 4 PASSED!!!\n')
	else:
		print(f'Test 4 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 5
	blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	height = 1
	ans = 10
	if ans == packBlocks(blocks, height):
		print('Test 5 PASSED!!!\n')
	else:
		print(f'Test 5 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 6
	blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	height = 1000000000
	ans = 1
	if ans == packBlocks(blocks, height):
		print('Test 6 PASSED!!!\n')
	else:
		print(f'Test 6 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 7
	# sum of blocks = 89979 // 86 = 1,046
	blocks = [9999, 9997, 9995, 9997, 9998, 9995, 9995, 10000, 9999, 9999]
	height = 86
	ans = 10000
	if ans == packBlocks(blocks, height):
		print('Test 7 PASSED!!!\n')
	else:
		print(f'Test 7 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 8
	blocks = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,
	          10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,
	          10000, 10000]
	height = 1
	ans = 200000
	if ans == packBlocks(blocks, height):
		print('Test 8 PASSED!!!\n')
	else:
		print(f'Test 8 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 9
	# sum of blocks = 52 // 26 --> blocks[4:-1] = 29
	blocks = [6, 10, 1, 6, 8, 2, 7, 3, 2, 7]
	height = 2
	ans = 29
	if ans == packBlocks(blocks, height):
		print('Test 9 PASSED!!!\n')
	else:
		print(f'Test 9 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 10
	# sum of blocks = 56 // 4 = 14 --> blocks[2:5] = 16
	blocks = [10, 3, 5, 4, 7, 8, 3, 2, 6, 8]
	height = 4
	ans = 16
	if ans == packBlocks(blocks, height):
		print('Test 10 PASSED!!!\n')
	else:
		print(f'Test 10 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 11
	# sum of blocks = 55 // 7 = 7 + 6 = 13
	blocks = [9, 6, 5, 7, 1, 6, 2, 6, 10, 3]
	height = 7
	ans = 11
	if ans == packBlocks(blocks, height):
		print('Test 11 PASSED!!!\n')
	else:
		print(f'Test 11 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 12
	blocks = [5, 4, 2, 5, 8, 3, 1, 5, 10, 9]
	height = 10
	ans = 10
	if ans == packBlocks(blocks, height):
		print('Test 12 PASSED!!!\n')
	else:
		print(f'Test 12 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')

	# Test 13
	blocks = [5, 4, 2, 5, 9, 6, 9, 8, 10, 4]
	height = 7
	ans = 14
	if ans == packBlocks(blocks, height):
		print('Test 13 PASSED!!!\n')
	else:
		print(f'Test 13 Failed:\nYour Output: '
		      f'{packBlocks(blocks, height)}\nCorrect Output: {ans}\n')
