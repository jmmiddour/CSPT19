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
