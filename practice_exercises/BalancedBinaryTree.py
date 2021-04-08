"""
You are given a binary tree and you need to write a function that
	can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the
	left and right subtrees of every node differ in height by a
	maximum of 1.

Example 1:

Given the following tree `[5,10,25,None,None,12,3]`:

```
    5
   / \
 10  25
    /  \
   12   3
```Add

return `True`.

Example 2:

Given the following tree `[5,6,6,7,7,None,None,8,8]`:

```
       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
```

return False.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] boolean
"""


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):
	"""
	- Implement a BFS to get the max depth of each subtree using recursive
	helper function
	- Compare the final subtrees to find out if there is <= 1 level difference
	- Return True if it is height-balanced and False if not
	"""

#     print(subtree)

# def helper(root):
#     if root is None:

#     subtree = (root.left.value, root.value, root.right.value)

#####################################################
#     if root.left is None and root.right is None:
#         return True

#     max_left_cnt = 0
#     max_right_cnt = 0

#     if max_left(root) is None:
#         max_left_cnt = 0

#     else: max_left_cnt = max_left(root)

#     if max_right(root) is None:
#         max_right_cnt = 0

#     else: max_right_cnt = max_right(root)

#     print(f'Left fn: {max_left(root)}, Left cnt: {max_left_cnt}')
#     print(f'Right fn: {max_right(root)}, Right cnt: {max_right_cnt}')

#     return (0 <= (max_left_cnt - max_right_cnt) <= 1) or (
#         0 <= (max_right_cnt - max_left_cnt) <= 1)


# def max_left(root):
#     if root is None or (root.left is None and root.right is None):
#         return 0

#     if root.right is not None:
#         return max_left(root.left) + 1

# def max_right(root):
#     if root is None or (root.left is None and root.right is None):
#         return 0

#     if root.left is not None:
#         return max_right(root.right) + 1

# One helper to calculate height.
# One edge case to empty
#

###########################################
# def balancedBinaryTree(root):
#     if root is None:
#         return True

#     height_left = height(root.left)
#     height_right = height(root.right)

#     if abs(height_left - height_right) <= 1 and balancedBinaryTree(
#     root.left) and balancedBinaryTree(root.right):
#         return True

#     return False

# def height(root):
#     if root is None:
#         return 0

#     return max(height(root.left), height(root.right)) + 1

#####################################################
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def balancedBinaryTree(root):
	"""
	- Implement a BFS to get the max depth of each subtree using recursive
	helper function
	- Compare the final subtrees to find out if there is <= 1 level difference
	- Return True if it is height-balanced and False if not
	"""
	# Check for edge case of an empty node
	if root is None:
		return True

	# Get the max height for the left of the tree
	max_left = max_height(root.left)
	# Get the max height for the right of the tree
	max_right = max_height(root.right)

	# If the max height of left - right is 1 or less and there is a both a
	# left and right child for the node, return True, else, False.
	return (max_left - max_right) <= 1 and balancedBinaryTree(
		root.left) and balancedBinaryTree(root.right)


# Define a function to get the max height of the subtree using recursion
def max_height(root):
	# If there is an empty node, just return 0
	if root is None:
		return 0

	# Return the max of the left root and right root plus 1
	return max(max_height(root.left), max_height(root.right)) + 1
