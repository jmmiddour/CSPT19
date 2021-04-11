"""
Note:
	Try to solve this task without using recursion, since this is what
		you'll be asked to do during an interview.

Given a binary tree of integers `t`,
	return its node values in the following format:

- The first element should be the value of the tree root;
- The next elements should be the values of the nodes at height 1 (i.e. the
	root children), ordered from the leftmost to the rightmost one;
- The elements after that should be the values of the nodes at height 2 (i.e.
	the children of the nodes at height 1) ordered in the same way;
- Etc.

Example:

For t = {
	"value": 1,
	"left": {
		"value": 2,
		"left": null,
		"right": {
			"value": 3,
			"left": null,
			"right": null
		}
	},
	"right": {
		"value": 4,
		"left": {
			"value": 5,
			"left": null,
			"right": null
		},
		"right": null
	}
}

the output should be:
	traverseTree(t) = [1, 2, 4, 3, 5].

This `t` looks like this:

     1
   /   \
  2     4
   \   /
    3 5

Input/Output:

[execution time limit] 4 seconds (py3)

[input] tree.integer t
	Guaranteed constraints:
		0 ≤ tree size ≤ 104.

[output] array.integer
	An array that contains the values at t's nodes, ordered as described above.
"""
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# Import deque (double-ended queue)
from collections import deque


def traverseTree(t):
	"""
	Understand:
	- results[0] = the root of the given tree
	- results[1] = left child of the root
	- results[2] = right child of the root
	- results[3] = left child of the left child of the root
	- results[4] = right child of the left child of the root
	- etc...
	"""
	# Create a results list to hold the values as I traverse the tree in a
	# breadth-first level order manner.
	results = []

	# Check for the edge case of an empty tree
	if t is None:
		return []

	# Instantiate a queue and append `t` to it
	que = deque()
	que.append([t])

	# While traverse the tree level by level, remove each level after it has
	# been seen from the queue.
	while len(que) > 0:
		# Pop off the left most value, the root node
		level_nodes = que.popleft()
		# Create a list to hold the results for each level
		level_res = []
		# Create a list to hold the values for the next level
		next_level = []

		# Iterate through the nodes in the current level
		for node in level_nodes:
			# Add the value of the current node
			level_res.append(node.value)

			# Add the left child of the current node to the next level list,
			# if there is one
			if node.left:
				next_level.append(node.left)

			# Add the right child of the current node to the next level list,
			# if there is one
			if node.right:
				next_level.append(node.right)

		# Check if there are still more levels in the tree
		if len(next_level) > 0:
			que.append(next_level)

		# Add all the results from the last level to the final results list
		results.append(level_res)

	# Return the results list as a 1D list
	return sum(results, [])


# Testing:
if __name__ == '__main__':
	# Test 1:
	t = Tree(1)
	t.left = Tree(2)
	t.left.right = Tree(3)
	t.right = Tree(4)
	t.right.left = Tree(5)
	ans = [1, 2, 4, 3, 5]
	if ans == traverseTree(t):
		print('PASSED!')
	else:
		print(f'Failed:\nYour Output --> {traverseTree(t)}\nCorrect Output '
		      f'--> {ans}')

	# Test 2:
	t = None
	ans = []
	if ans == traverseTree(t):
		print('PASSED!')
	else:
		print(f'Failed:\nYour Output --> {traverseTree(t)}\nCorrect Output '
		      f'--> {ans}')

	# Test 3:
	t = Tree(2)
	t.left = Tree(1)
	t.left.right = Tree(0)
	ans = [2, 1, 0]
	if ans == traverseTree(t):
		print('PASSED!')
	else:
		print(f'Failed:\nYour Output --> {traverseTree(t)}\nCorrect Output '
		      f'--> {ans}')

	# Test 4:
	t = Tree(15)
	t.left = Tree(15)
	ans = [15, 15]
	if ans == traverseTree(t):
		print('PASSED!')
	else:
		print(f'Failed:\nYour Output --> {traverseTree(t)}\nCorrect Output '
		      f'--> {ans}')
