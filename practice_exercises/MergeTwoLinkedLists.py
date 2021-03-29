"""
Note: Your solution should have O(l1.length + l2.length) time complexity,
	since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order,
	your task is to merge them. In other words, return a singly linked list,
	also sorted in non-decreasing order, that contains the elements from
	both original lists.

Example:

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be:
	mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];

For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be:
	mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].

Input/Output:

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1
	A singly linked list of integers.

	Guaranteed constraints:
		0 ≤ list size ≤ 104,
		-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2
	A singly linked list of integers.

	Guaranteed constraints:
		0 ≤ list size ≤ 104,
		-109 ≤ element value ≤ 109.

[output] linkedlist.integer
	A list that contains elements from both l1 and l2, sorted in
		non-decreasing order.
"""


def mergeTwoLinkedLists(l1, l2):
	"""
	Edge Cases:
	- Posible to get an empty list
	- Both list are sorted in ascending order,
		but does not guarantee that it will be sorted
		once merged. Have to sort merged list too.

	Test Cases:
	l1 = [1, 2, 3]
	l2 = [4, 5, 6]
	output ---> [1, 2, 3, 4, 5, 6]

	l1 = []
	l2 = [3, 5, 7]
	output ---> [3, 5, 7]

	l1 = [1, 3, 3]
	l2 = [2, 6, 6]
	output ---> [1, 2, 3, 3, 6, 6]

	Plan:
	1. Check for edge cases of an empty list.
	2. Traverse the first list to find the tail node.
	3. Point the tail node of list 1 to the head of list 2.
	4. Sort the merged linked list.
	5. Return the sorted merged list.
	"""

	# My Solution
	if l1 is None:
		return l2

	if l2 is None:
		return l1

	result = res_curr = ListNode(0)

	while l1 or l2:
		if l1 and (not l2 or l1.value <= l2.value):
			res_curr.next = ListNode(l1.value)
			l1 = l1.next

		else:
			res_curr.next = ListNode(l2.value)
			l2 = l2.next

		res_curr = res_curr.next

	return result.next

# # Lambda's Solution
# def mergeTwoLinkedLists(l1: ListNode, l2: ListNode) -> ListNode:
#     p1, p2 = l1, l2
#     new_list = None
#     current = None

#     if not p1:
#         return p2
#     if not p2:
#         return p1

#     if p1.value < p2.value:
#         new_list = ListNode(p1.value)
#         p1 = p1.next
#     else:
#         new_list = ListNode(p2.value)
#         p2 = p2.next

#     current = new_list

#     while p1 and p2:
#         if p1.value < p2.value:
#             current.next = ListNode(p1.value)
#             p1 = p1.next
#         else:
#             current.next = ListNode(p2.value)
#             p2 = p2.next

#     current = current.next

#     if p1:
#         current.next = p1
#     if p2:
#         current.next = p2

#     return new_list

	# # Paul's Code
	# # Create a head and temp dummy pointer
	# head_ptr = temp_ptr = ListNode('*')
	# while l1 or l2:
	#     if l1 and (not l2 or l1.value <= l2.value):
	#         temp_ptr.next = ListNode(l1.value)
	#         l1 = l1.next
	#     else:
	#         temp_ptr.next = ListNode(l2.value)
	#         l2 = l2.next
	#     # move temp_pointer to next position
	#     temp_ptr = temp_ptr.next
	# # return output list
	# return head_ptr.next
