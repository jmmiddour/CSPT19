"""
Note:
	Your solution should have O(l.length) time complexity and
	O(1) space complexity, since this is what you will be asked
	to accomplish in an interview.

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be:
	reverseLinkedList(l) = [5, 4, 3, 2, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l
	A singly linked list of integers.

	Guaranteed constraints:
		0 ≤ l.length ≤ 105,
		-109 ≤ l.value ≤ 109.

[output] linkedlist.integer
	Reversed l.
"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
	"""
	1. Need previous, current, and temp pointers
	2. The previous pointer points to the previous node of the current node.
	3. The current pointer will point to the current node.
	4. The temp pointer will point to the next node of the the current node to
	reverse it.
	5. Return the previous pointer.
	"""
	# Current pointer initialized to the head node
	curr = l
	# Previous pointer initialized to None
	prev = None

	# Iterate through the linked list while the current node is not None.
	while curr != None:
		# Temp pointer keeps track of the current node's next node.
		temp = curr.next
		# Assign the current pointer's next to point to the current node's
		#   previous node.
		curr.next = prev
		# Point the prev pointer to the current node.
		prev = curr
		# Reassign the current pointer to point at the temp pointer.
		curr = temp

	# Return the previous pointer.
	return prev


# Testing:
if __name__ == '__main__':
	# Test 1:
	l = [1, 2, 3, 4, 5]
	ans = [5, 4, 3, 2, 1]

	# Test 2:
	l = [5, 4, 3, 2, 1, 2, 3, 4, 5]
	ans = [5, 4, 3, 2, 1, 2, 3, 4, 5]

	# Test 3:
	l = [5, 4, 3, 2, 1, 2, 3, 4, 5, 1000000000, -1000000000]
	ans = [-1000000000, 1000000000, 5, 4, 3, 2, 1, 2, 3, 4, 5]

	# Test 4:
	l = []
	ans = []

	# Test 5:
	l = [42]
	ans = [42]
