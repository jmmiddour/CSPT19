"""
There are N students in a baking class together. Some of them are friends,
	while some are not friends. The students' friendship can be considered
	*transitive*. This means that if Ami is a direct friend of Bill, and Bill
	is a direct friend of Casey, Ami is an indirect friend of Casey.
	A friend circle is a group of students who are either direct or indirect
	friends of some level. That is, the friend circle consists of a person,
	their friends, their friends-of-friends,
	their friends-of-friends-of-friends, and so on.

Given a N*N matrix M representing the friend relationships between students
	in the class. If M[i][j] = 1, then the ith and jth students are direct
	friends with each other, otherwise not.

You need to write a function that can output the total number of friend
	circles among all the students.

**Example 1:**

friendships =  [[1,1,0],
				[1,1,0],
				[0,0,1]]
Output = 2
Explanation:
	The 0th and 1st students are direct friends, so they are in a friend circle.
	The 2nd student himself is in a friend circle. So return 2.

**Example 2:**

friendships =  [[1,1,0],
				[1,1,1],
				[0,1,1]]
Output = 1
Explanation:
	The 0th and 1st students are direct friends, the 1st and 2nd students
		are direct friends, so the 0th and 2nd students are indirect friends.
		All of them are in the same friend circle, so return 1.

[execution time limit] 4 seconds (py3)

[input] array.array.integer friendships

[output] integer
"""

def csFriendCircles(M):
	"""
	Understanding:
	- Given a n*n Matrix with the relationships between the students in the
	class.
	- This is just a matrix representation of the graph
	- As a matrix:
	    [[1, 1, 0],
	     [1, 1, 1],
	     [0, 1, 1]]
	- As an adjacency list:
	    {
	        0: {1},
	        1: {0, 2},
	        2: {1}
	     }
	- What defines a friend circle is all of the 1's that are connected in the
	graph, either direct or indirect.
	- Another way to represent a friend circle is if the vertex is not
	connected to any other vertices.
	- Need to return the number of friend cirles
	"""

	from collections import deque

	def csFriendCircles(M):
		# Need a variable to hold the number of circles
		num_circles = 0
		# Create a visited set
		visited = set()

		# Iterate over the rows (vertex edges)
		for row in range(len(M)):
			# Check if the row is already in the seen set
			if row not in visited:
				# Increase the num_circles by 1
				num_circles += 1
				# Use a recursive helper function to traverse the row
				friend_helper(row, M, visited)

		# Return the number of circles
		return num_circles

	# Create a helper function to traverse each vertex (row)
	def friend_helper(person, M, visited):
		# Iterate through enumerated row (vertex)
		for vert, edge in enumerate(M[person]):
			# Check if there is an edge and person is not in visited already
			if edge and vert not in visited:
				# Add the vertex to the visited set
				visited.add(vert)
				# Recursively call helper to continue traversing until no more
				# edges exist
				friend_helper(vert, M, visited)


	# ################ Origin - Not Working ################# #
	# # Need a variable to hold the number of circles
	# num_circles = 0
	# # Create a visited set
	# visited = set()
	# # Implement a queue
	# que = deque()
	# # Append to the queue a tuple with the start row and start col
	# que.append((0, 0))
	# # Get the number of rows and cols
	# rows, cols = len(M), len(M[0])
	# # Need a results list
	# num_circles = 0

	# # Traverse the length of the queue
	# while len(que) > 0:
	#     # Create a current pointer to look at the current vertex
	#     pointer = que.popleft()
	#     print(f'Pointer: {pointer}')
	#     # Get the current row and col
	#     cur_row, cur_col = pointer[0], pointer[1]
	#     print(f'Current Row: {cur_row}\nCurrent Column: {cur_col}')

	#     # If the pointer is in visited already
	#     if pointer in visited:
	#         # Keep traversing
	#         continue

	#     # Check to make sure still within the index
	#     if cur_row < 0 or cur_row >= rows or cur_col < 0 or cur_col >= cols:
	#         # Keep traversing
	#             continue

	#     # Add the pointer to the visited
	#     visited.add(pointer)
	#     print(f'Visited in Loop: {visited}')
	#     # Change the value of the current node to zero
	#     M[cur_row][cur_col] = 0
	#     # print(f'Matrix in Loop: {M}')

	#     # if cur_col == len(cols):

	#     # Add all the neighbors to the queue
	#     que.append((cur_row - 1, cur_col))
	#     que.append((cur_row + 1, cur_col))
	#     que.append((cur_row, cur_col - 1))
	#     que.append((cur_row, cur_col + 1))
	#     print(f'Queue in Loop: {que}')

	# print(f'Visited out of Loop:\n{visited}')
	# print(f'Queue out of loop: {que}')


# Testing
if __name__ == '__main__':
	# Test 1
	M = [[1,1,0], [1,1,0], [0,0,1]]
	ans = 2
	if ans == csFriendCircles(M):
		print('Test 1 PASSED!!!')
	else:
		print(f'Test 1 Failed:\nYour Output: {csFriendCircles(M)}\nCorrect '
		      f'Output: {ans}')

	# Test 2
	M = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
	ans = 1
	if ans == csFriendCircles(M):
		print('Test 2 PASSED!!!')
	else:
		print(f'Test 2 Failed:\nYour Output: {csFriendCircles(M)}\nCorrect '
		      f'Output: {ans}')
