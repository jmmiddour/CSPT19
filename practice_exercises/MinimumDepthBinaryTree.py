"""
You are given a binary tree and you are asked to write a function that
	finds its minimum depth. The minimum depth can be defined as the number
	of nodes along the shortest path from the root down to the nearest leaf
	node. As a reminder, a leaf node is a node with no children.

Example:
	Given the binary tree

	```
	[5,7,22,None,None,17,9],
	    5
	   / \
	  7  22
	    /  \
	   17   9
	```

	your function should return its minimum depth = 2.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] integer
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

from collections import deque


def minimumDepthBinaryTree(root):
	"""
	- Check edge case of only one node.
	- Tranvers the tree using bFS (Breadth-First Search)
	- As I traverse the tree add to a counter (create a dictionary for this,
	key = side of tree, value = how many deep) for each node
	- Once I hit the first leaf (node with no children), save that number and
	traverse the other side, repeating the steps above.
	- Return the min value from the counter dictionary.
	"""
	if root is None:
		return 0

	if root.left is None and root.right is None:
		return 1

	if root.left is None:
		return minimumDepthBinaryTree(root.right) + 1

	if root.right is None:
		return minimumDepthBinaryTree(root.left) + 1

	return min(minimumDepthBinaryTree(root.left),
	           minimumDepthBinaryTree(root.right)) + 1

# que = deque()

# que.append([root])

# level_count = 1
# # counts = {'left': 1, 'right': 1}

# while len(que) > 0:
#     nodes_in_level = que.popleft()
#     # res_level = []
#     next_level = []

#     for node in nodes_in_level:
#         # res_level.append(node.value)

#         if node.left != None:
#             next_level.append(node.left)
#             # counts['left'] += 1
#             # print(f'In left: {counts["left"]}')

#         if node.right != None:
#             next_level.append(node.right)
#             # counts['right'] += 1
#             # print(f'In right: {counts["right"]}')

#     if 0 < len(next_level):
#         que.append(next_level)
#         level_count += 1
#         print(level_count)

#     # if len(next_level) == 0:
#         # if counts['left'] <= counts['right']:
#         #     print(counts.values())
#         #     return counts['left']

#         # return counts['right']
#         # print(level_count)

# return level_count


#     counts = {'Left': 0, 'Right': 0}

#     # return dft(root)

#     return min(dft(counts.values())

# def dft(curr, counts):
#     if curr is None:
#         return

#     if curr.left:
#         counts['Left'] += 1

#     if curr.right:
#         counts['right'] += 1


# left_node = minimumDepthBinaryTree(root.left)
# print(f'Left node: {left_node}')
# right_node = minimumDepthBinaryTree(root.right)
# print(f'Right Node: {right_node}')

# if left_node:
#     counts['Left'] += 1
#     print(f'Counts in left: {counts}')

# if right_node:
#     counts['Right'] += 1
#     print(f'Counts in Right: {counts}')


# l_depth = dft(curr.left)
# r_depth = dft(curr.right)

# return min(l_depth, r_depth) + 1
