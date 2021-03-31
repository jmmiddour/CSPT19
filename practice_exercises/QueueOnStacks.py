"""
Implement the missing code, denoted by ellipses.
You may not modify the pre-existing code.
Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be "push <x>"
	or "pop". Return an array composed of the results of each "pop" operation
	that is performed.

Example:

For requests = ["push 1", "push 2", "pop", "push 3", "pop"],
	the output should be:
	queueOnStacks(requests) = [1, 2].

After the first request, the queue is {1};
After the second it is {1, 2}.
Then we do the third request, "pop", and add the first element of the
	queue 1 to the answer array. The queue becomes {2}.
After the fourth request, the queue is {2, 3}.
Then we perform "pop" again and add 2 to the answer array,
	and the queue becomes {3}.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.string requests
	requests[i] can be "push <x>" or "pop".
	It is guaranteed that "pop" isn't applied to an empty queue.

	Guaranteed constraints:
		1 ≤ requests.length ≤ 300,
		-1000 ≤ x ≤ 1000.

[output] array.integer
	Return an array composed of the results of each "pop"
		operation that is performed.
"""


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()


"""
Test Cases:
requests = ["push 1", "push 2", "pop", "push 3", "pop"]
output ---> [1, 2]

requests = ["push 3", "push 2", "pop", "push 6", "pop"]
output ---> [3, 2]

Plan:
1. For `insert()`, just need to use the Stack method from the above Stack 
	class to append the value to the `left` Stack.
2. For `remove()`, check if the `right` Stack is empty. While the `left` Stack
	is not empty, pop off the last value in the `left` stack and append it to 
	the `right` Stack. Then return the last value in the `right` Stack, 
	which is actually the first value added to the `left` Stack.
"""


def queueOnStacks(requests):
	left = Stack()
	right = Stack()

	def insert(x):
		# Using the method from the above Stack
		#   implementation append x to left Stack
		left.push(x)

	def remove():
		# Check if the right Stack is empty
		if right.isEmpty():

			# While the left Stack is not empty
			while not left.isEmpty():
				# Assign the last element of the left Stack
				#   to a temp variable
				temp = left.pop()
				# Append the value popped from left Stack to right Stack
				right.push(temp)

		# Return the right Stack's last value, which is the first value
		#   popped from the left Stack
		return right.pop()

	ans = []
	for request in requests:
		req = request.split(" ")
		if req[0] == 'push':
			insert(int(req[1]))
		else:
			ans.append(remove())
	return ans
