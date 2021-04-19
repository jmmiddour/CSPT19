"""
Given a binary tree, write a function that inverts the tree.

Example:

Input:
     6
   /   \
  4     8
 / \   / \
2   5 7   9

Output:
     6
   /   \
  8     4
 / \   / \
9   7 5   2
[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] tree.integer
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def csBinaryTreeInvert(root):
	"""
	Understanding:
		- Given a binary tree, starting at the root node
		- Need to swicth each left and right child through the tree
		- Return the inverted tree
	"""
	# Check for edge case of an empty tree
	if root == None:
		return None

	# Reverse the order of the child nodes for the current node
	root.left, root.right = root.right, root.left

	# Use recursion to go to the next subtree until my base case is reached
	csBinaryTreeInvert(root.left)
	csBinaryTreeInvert(root.right)

	# Return the reversed tree
	return root


"""
root:
{
    "value": 4,
    "left": {
        "value": 2,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 7,
        "left": {
            "value": 6,
            "left": null,
            "right": null
        },
        "right": {
            "value": 9,
            "left": null,
            "right": null
        }
    }
}
Expected Output:
{
    "value": 4,
    "left": {
        "value": 7,
        "left": {
            "value": 9,
            "left": null,
            "right": null
        },
        "right": {
            "value": 6,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    }
}
"""
