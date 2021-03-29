"""
Note:
	Your solution should have O(n) time complexity,
	where n is the number of elements in l, since this is
	what you will be asked to accomplish in an interview.

You have a singly linked list l,
	which is sorted in strictly increasing order,
	and an integer value. Add value to the list l,
	preserving its original sorting.

Note:
	in examples below and tests preview linked lists are presented
	as arrays just for simplicity of visualization: in real data
	you will be given a head node l of the linked list

Example:

For l = [1, 3, 4, 6] and value = 5, the output should be:
	insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];

For l = [1, 3, 4, 6] and value = 10, the output should be:
	insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];

For l = [1, 3, 4, 6] and value = 0, the output should be:
	insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].

Input/Output:

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l
	A singly linked list of integers sorted in strictly increasing order.
	Thus, all integers in the list are pairwise distinct.

	Guaranteed constraints:
		0 ≤ list size ≤ 104,
		-109 ≤ element value ≤ 109.

[input] integer value
	A single integer value to be inserted into l.
		It is guaranteed that there is not an element equal to value in l
		before the insertion is performed.

	Guaranteed constraints:
		-109 ≤ value ≤ 109.

[output] linkedlist.integer
	Return l after inserting value into it,
		with the original sorting preserved.
"""


# Singly-linked lists are already defined with this interface:
class ListNode(object):
	def __init__(self, x):
		self.value = x
		self.next = None

	def __repr__(self):
		return f'{self.value} '


# Test Case 1
a1 = ListNode(1)
a1.next = ListNode(3)
a1.next.next = ListNode(4)
a1.next.next.next = ListNode(6)

# a1.next = b1
# b1.next = c1
# c1.next = d1

# Test Case 2
a2 = ListNode(1)
a2.next = ListNode(3)
a2.next.next = ListNode(4)
a2.next.next.next = ListNode(6)

# a2.next = b2
# b2.next = c2
# c2.next = d2

# Test Case 3
a3 = ListNode(1)
a3.next = ListNode(3)
a3.next.next = ListNode(4)
a3.next.next.next = ListNode(6)

# a3.next = b3
# b3.next = c3
# c3.next = d3

"""
Test Cases:
l = [1, 3, 4, 6]
value = 5
output --> [1, 3, 4, 5, 6]

l = [3, 6, 8, 9, 12, 15]
value = 7
output --> [3, 6, 7, 8, 9, 12, 15]

l = []
value = 2
output --> [2]

Plan:
1. Create a pointer to point at the current node, (the head node to start)
2. Create a linked list node to hold the given value.
3. Create a last pointer to point to the previous node for the current node, 
which will be None to start.
4. Traverse the linked list while comparing each node's value with the given 
value.
5. If the given value is greater than the current node but less than the 
current node's next node, need to insert given value after current node but 
before current node's next node. Will do this by 1st pointing the given value 
node's next to the current node's next, then point the current node to the 
given value node.
6. Return new linked list.
"""


def insertValueIntoSortedLinkedList(l, value):
	# # My attempt to solve, not working, too much time on it. # #
	# if l is None:
	# 	l = ListNode(value)
	# 	return l
	#
	# curr = l
	# print(f'Current Node - Start: {curr.value}')
	# new_node = ListNode(value)
	# print(f'Value as new node: {new_node.value}\n')
	# prev = ListNode('*')
	#
	# while curr.next:
	# 	if curr is not None and curr.value < new_node.value:
	# 		prev = curr
	# 		print(f'Previous Node - in if statement: {prev.value}')
	# 		curr = curr.next
	# 		if curr:
	# 			print(f'Current Node - in if statement: {curr.value}\n')
	#
	# 	elif curr.value > new_node.value and prev is None:
	# 		new_node.next = curr
	# 		print(f'New Node Next - in elif 1: {new_node.value}\n')
	# 		return l
	#
	# 	elif prev.value < new_node.value < curr.value:
	# 		new_node.next = curr
	# 		print(f'New Node Next - in elif 2: {new_node.value}')
	# 		prev.next = new_node
	# 		print(f'Previous Node Next - in elif 2: {prev.next.value}\n')
	# 		return l
	#
	# 	else:
	# 		prev.next = curr
	# 		print(f'Previous Node Next: {prev.next.value}')
	#
	# print(f'Current Node - After loop: {curr.value}')
	# print(f'Current Previous Node - After loop: {prev.value}')
	# # print(f'New Node Next - After loop: {new_node.next.value}')
	#
	# # new_node.next = temp_next
	# # print(f'Value next node: {new_node.next.value}')
	# # curr.next = temp
	# # print(f'Current Next Node: {curr.next.value}')
	#
	# # return l

	# ### Code I got from Jeremiah ### #
	# Create a pointer to point at the prev node of the current node.
	# Create a pointer tp point at the current node.
	# Starting prev at None, and curr at head.
	prev = None
	curr = l

	# Create a "helper" function to insert the new node value
	def insert_node():
		# Create a new node with the given value
		new_node = ListNode(value)

		# If current node is not None
		if curr:
			# Then the new node will equal the current node.
			# So it doesn't loose track of the current node.
			new_node = curr

		# If the previous node to the current node is not None
		if prev:
			# Then previous next pointer needs to point to the new node
			prev.next = new_node
			# Return the new linked list
			return l

		# If it does not meet any of the above conditions...
		else:
			# Just return the new node
			return new_node

	# Transverse the linked list as long as the current node is not None
	while curr:
		# If the given value is less than the current node's value...
		if value < curr.value:
			# Then need to insert the value before the current node
			#   using my helper function
			return insert_node()

		# If the above condition is not met...
		# Need to assign the previous node pointer to the current node
		prev = curr
		# Need to assign the current node to the current node's next node.
		curr = curr.next

	# Return the new linked list using my helper function
	return insert_node()


if __name__ == '__main__':
	if insertValueIntoSortedLinkedList(a1, 5):
		assert [1, 3, 4, 5, 6]
		print('True')
	else:
		print('False')

	if insertValueIntoSortedLinkedList(a2, 10):
		assert [1, 3, 4, 6, 10]
		print('True')
	else:
		print('False')

	if insertValueIntoSortedLinkedList(a3, 0):
		assert [0, 1, 3, 4, 6]
		print('True')
	else:
		print('False')

# print('Test 2 Result:', insertValueIntoSortedLinkedList(a2, 10),
#       '\nCorrect:', [1, 3, 4, 6, 10], '\n')
#
# print('Test 3 Result:', insertValueIntoSortedLinkedList(a3, 0),
#       '\nCorrect:', [0, 1, 3, 4, 6], '\n')
