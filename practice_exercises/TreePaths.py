"""
Given a binary tree of integers, return all the paths from the tree's
	root to its leaves as an array of strings.
The strings should have the following format:
	"root->node1->node2->...->noden", representing the path from
		root to noden, where root is the value stored in the root
		and node1,node2,...,noden are the values stored in the 1st,
		2nd,..., and nth nodes in the path respectively (noden
		representing the leaf).

Example:

For t = {
	"value": 5,
	"left": {
		"value": 2,
		"left": {
			"value": 10,
			"left": null,
			"right": null
		},
		"right": {
			"value": 4,
			"left": null,
			"right": null
		}
	},
	"right": {
		"value": -3,
		"left": null,
		"right": null
	}
}

the output should be:
	treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4

Input/Output:

[execution time limit] 4 seconds (py3)

[input] tree.integer t
	A tree of integers.

	Guaranteed constraints:
		0 ≤ tree size ≤ 710,
		-1000 ≤ node value ≤ 1000.

[output] array.string
	The root-to-leaf paths, sorted by the leaves in the order that they
		appear in the pre-order traversal (i.e. from the leftmost leaf
		to the rightmost).
"""


#
# Binary trees are already defined with this interface:
class Tree(object):
	def __init__(self, x):
		self.value = x
		self.left = None
		self.right = None


def treePaths(t):
	"""
	Understanding:
	- Traverse the tree in a pre-order depth-first manner.
	- Need to return the values in a list of strings
	- Strings need to be in the format:
		"root->child1->child2->...->leaf"
	"""
	# Check for edge case of no tree node
	if t is None:
		# Return an empty list
		return []

	# If there is no children, it is a leaf
	if t.left == None and t.right == None:
		# and need to return just the leaf node
		return [str(t.value)]

	# Using recursion, get root node value, root's left, then right and add it
	# all as one string per path.
	return [str(t.value) + '->' + x for x in
	        treePaths(t.left) + treePaths(t.right)]

# Testing
if __name__ == '__main__':
	# Test 1
	t = Tree(5)
	t.left = Tree(2)
	t.left.left = Tree(10)
	t.left.right = Tree(4)
	t.right = Tree(-3)
	ans = ["5->2->10", "5->2->4", "5->-3"]
	if ans == treePaths(t):
		print(f'PASSED!\n')
	else:
		print(f'Failed:\nYour Output --> {treePaths(t)}\nCorrect Output -->'
		      f' {ans}\n')

	# Test 2
	t = None
	ans = []
	if ans == treePaths(t):
		print(f'PASSED!\n')
	else:
		print(f'Failed:\nYour Output --> {treePaths(t)}\nCorrect Output -->'
		      f' {ans}\n')

	# Test 3
	t = Tree(42)
	ans = ['42']
	if ans == treePaths(t):
		print(f'PASSED!\n')
	else:
		print(f'Failed:\nYour Output --> {treePaths(t)}\nCorrect Output -->'
		      f' {ans}\n')

	# Test 4
	t = Tree(1000)
	t.left = Tree(2)
	t.left.left = Tree(10)
	t.left.left.right = Tree(-1000)
	t.left.left.right.right = Tree(0)
	t.left.right = Tree(4)
	t.right = Tree(3)
	t.right.right = Tree(99)
	t.right.right.left = Tree(6)
	t.right.right.left.left = Tree(1)
	ans = ["1000->2->10->-1000->0", "1000->2->4", "1000->3->99->6->1"]
	if ans == treePaths(t):
		print(f'PASSED!\n')
	else:
		print(f'Failed:\nYour Output --> {treePaths(t)}\nCorrect Output -->'
		      f' {ans}\n')
