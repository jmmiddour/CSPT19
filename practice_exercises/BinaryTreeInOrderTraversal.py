"""
You are given a binary tree.
Write a function that returns the binary tree's
	node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] array.integer
"""

# Binary trees are already defined with this interface:
class Tree(object):
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None


def binaryTreeInOrderTraversal(root):
	# Check if the given tree is empty
	if root is None:
		return

	# Create a list to hold the results of the traversal
	results = []
	# Call on the helper function to traverse the tree
	helper(root, results)
	# Return the results list
	return results


def helper(node, results):
	"""
	Helper function to traverse a binary tree in a Depth-First in-order manner
	"""
	# Check for base case
	if node == None:
		return

	# If there is a left child for the current node
	if node.left != None:
		# Use recursion to append the value to the results list
		helper(node.left, results)

	# Append the current node's value to the results list
	results.append(node.value)

	# There is a right child for the current node
	if node.right != None:
		# Use recursion to append the value to the results list
		helper(node.right, results)


if __name__ == '__main__':
	root = Tree(2)
	root.right = Tree(3)
	root.right.left = Tree(4)
	ans = [2, 4, 3]
	if ans == binaryTreeInOrderTraversal(root):
		print('PASSED!')
	else:
		print(f'Failed:\nYour Output --> '
		      f'{binaryTreeInOrderTraversal(root)}\nCorrect Output --> {ans}')
