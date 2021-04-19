"""
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the
	nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

Example 1:

Input:
root = [10, 5, 15, 3, 7, null, 18]
lower = 7
upper = 15

         10
         / \
        5  15
       / \    \
      3   7    18

Output:
32
Example 2:

Input:
root = [10,5,15,3,7,13,18,1,null,6]
lower = 6
upper = 10

           10
          /  \
       5      15
     / \     /   \
    3   7  13   18
   /   /
  1   6

Output:
23
[execution time limit] 4 seconds (py3)

[input] tree.integer root

[input] integer lower

[input] integer upper

[output] integer
"""


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
	"""
	Understanding:
		- Given the root node of a BST
		- Need to return the sum of all nodes that are `lower` <= nodes <=
		`upper`
		- All nodes are gauranteed to be unique values
	"""
	# Create a result variable to hold the running total of nodes seen
	results = 0

	# Create a list to hold the nodes while traversing the BST
	res = []

	# Add the value of the current node to the results
	get_vals(root, res)

	# Iterate through the nodes list
	for i in range(len(res)):
		# If lower <= current node <= upper
		if lower <= res[i] <= upper:
			# Add the value to the results total
			results += res[i]

	# Return the resulting sum
	return results


# Create a function to traverse the BST
def get_vals(root, res):
	# Check for edge case of empty node, this my base case
	if root == None:
		return

	# Traverse the tree in a depth-first in-order manner using recursion
	if root.left:
		get_vals(root.left, res)

	res.append(root.value)

	if root.right:
		get_vals(root.right, res)


"""
Test 1
Input:
root:
{
    "value": 10,
    "left": {
        "value": 5,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 7,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 15,
        "left": null,
        "right": {
            "value": 18,
            "left": null,
            "right": null
        }
    }
}
lower: 7
upper: 15
Expected Output:
32

Test 2
Input:
root:
{
    "value": 10,
    "left": {
        "value": 5,
        "left": {
            "value": 3,
            "left": {
                "value": 1,
                "left": null,
                "right": null
            },
            "right": null
        },
        "right": {
            "value": 7,
            "left": {
                "value": 6,
                "left": null,
                "right": null
            },
            "right": null
        }
    },
    "right": {
        "value": 15,
        "left": {
            "value": 13,
            "left": null,
            "right": null
        },
        "right": {
            "value": 18,
            "left": null,
            "right": null
        }
    }
}
lower: 6
upper: 10
Expected Output:
23

Test 3
Input:
root:
{
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 5,
            "left": null,
            "right": {
                "value": 3,
                "left": {
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
                },
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": {
                "value": 5,
                "left": null,
                "right": null
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
    }
}
lower: 10
upper: 15
Expected Output:
0
"""