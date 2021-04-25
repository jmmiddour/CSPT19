"""
In a city-state of n people, there is a rumor going around that one of
	the n people is a spy for the neighboring city-state.

The spy, if it exists:

1. Does not trust anyone else.
2. Is trusted by everyone else (he's good at his job).
3. Works alone; there are no other spies in the city-state.

You are given a list of pairs, trust. Each trust[i] = [a, b]
	represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier.
	Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1,
	so Person 2 is the spy.

Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3,
	but Person 3 does not trust either Person 1 or Person 2.
	Thus, Person 3 is the spy.

Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3,
	and Person 3 trusts Person 1. Since everyone trusts at least
	one other person, there is no spy.

Example 4:

Input: n = 3, trust = [[1, 2], [2, 3]]
Output: -1
Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3.
	However, in this situation, we don't have any one person who is
	trusted by everyone else. So we can't determine who the spy is
	in this case.

Example 5:

Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
Output: 3
Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts
	Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts
	Person 3 but Person 3 does not trust anyone, so they are the spy.

[execution time limit] 4 seconds (py3)

[input] integer n
	The number of people in the city-state

[input] array.array.integer trust
	Array of pairs indicating who each person in trusts.

[output] integer
	The identifier of the spy.
"""
from collections import deque


def uncover_spy(n, trust):
	"""
	Understanding:
	- `n`: integer representing the number of people
	- `trust`: 2d list representing who trust who
	- `trust[0]`: the person who trust `trust[1]`
	- `trust[1]`: the trusted person
	- There will be at most 1 spy
	- The spy doesn't trust anyone, but everyone trust them
	- If there is a spy, return the spy's number
	- If no spy is found, return `-1`
	"""
	########################################################################
	# ####### My Solution = Only Passing 6/7 Test (Test 6 Failing) ####### #
	########################################################################
	# # Create a dictionary for the people, key is the truster, value is the
	# trusted
	# trusted = {}
	# # Create a results list with people that are not trusted
	# res = deque()

	# # Iterate over the list of trust to populate the dictionary
	# for i in range(len(trust)):
	#     # If the person at trust[0] is in the dictionary
	#     if trust[i][0] in trusted:
	#         # Append trust[1] to the value list
	#         trusted[trust[i][0]].append(trust[i][1])

	#     # Otherwise...
	#     else:
	#         # Add trust[0] as key and trust[1] as value
	#         trusted[trust[i][0]] = [trust[i][1]]

	# # Iterate through the dictionary
	# for key, _ in trusted.items():
	#     # If the value is not in the dictionary keys...
	#     if trusted[key] not in iter(trusted.keys()):
	#         # If the current val is not already in results...
	#         if trusted[key] not in res:
	#             # Add the current value to the results
	#             res.append(trusted[key].pop())

	#         else:  # Otherwise...
	#             # Remove the current value from the results
	#             res = res.remove(trusted[key()])

	#     else:  # Otherwise
	#         # Remove the current value from the results
	#         res = res.remove(trusted[key])

	#     # print(f'Results in loop: {res}')

	# # Turn the results list into a set to get only unique values
	# res = set(res)

	# # print(f'Results: {res}')

	# # If the results is not empty and there is only 1 value
	# if res != {} and len(res) < 2:
	#     # Return the value
	#     return res.pop()

	# # Otherwise, return -1, spy not found
	# return -1

	##########################################################################
	# ################### Solution found on LeetCode ####################### #
	"""
	https://leetcode.com/problems/find-the-town-judge/discuss/244859/Python-O(n)-with-Explanation
	"""
	##########################################################################
	# Create a list of the trusted
	trusted = [0] * (n + 1)

	# Iterate over the people in the trust list
	for person_a, person_b in trust:
		# Decrement person a's score by 1 for trusting another person
		trusted[person_a] -= 1
		# Increment person b's score by 1, they are the one being trusted
		trusted[person_b] += 1

	# Iterate though the number of people in the city-state
	for i in range(1, n + 1):
		# If the person's score is the number of people - 1...
		if trusted[i] == n - 1:
			# Return that person, found our spy
			return i

	# Otherwise, return -1
	return -1


# Testing
if __name__ == '__main__':
	# Test 1
	n = 2
	trust = [[1, 2]]
	ans = 2
	if uncover_spy(n, trust) == ans:
		print('Test 1 PASSED!!!\n')
	else:
		print(
			f'Test 1 Failed!\n  Your Output: {uncover_spy(n, trust)}\n  '
			f'Correct Output: {ans}\n'
		)

	# Test 2
	n = 4
	trust = [[1, 2], [3, 4]]
	ans = -1
	if uncover_spy(n, trust) == ans:
		print('Test 2 PASSED!!!\n')
	else:
		print(
			f'Test 2 Failed!\n  Your Output: {uncover_spy(n, trust)}\n  '
			f'Correct Output: {ans}\n'
		)

	# Test 3
	n = 3
	trust = [[1, 3], [2, 3]]
	ans = 3
	if uncover_spy(n, trust) == ans:
		print('Test 3 PASSED!!!\n')
	else:
		print(
			f'Test 3 Failed!\n  Your Output: {uncover_spy(n, trust)}\n  '
			f'Correct Output: {ans}\n'
		)

	# Test 4
	n = 3
	trust = [[1, 3], [2, 3], [3, 1]]
	ans = -1
	if uncover_spy(n, trust) == ans:
		print('Test 4 PASSED!!!\n')
	else:
		print(
			f'Test 4 Failed!\n  Your Output: {uncover_spy(n, trust)}\n  '
			f'Correct Output: {ans}\n'
		)

	# Test 5
	n = 3
	trust = [[1, 2], [2, 3]]
	ans = -1
	if uncover_spy(n, trust) == ans:
		print('Test 5 PASSED!!!\n')
	else:
		print(
			f'Test 5 Failed!\n  Your Output: {uncover_spy(n, trust)}\n  '
			f'Correct Output: {ans}\n'
		)

	# Test 6
	n = 4
	trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
	ans = 3
	if uncover_spy(n, trust) == ans:
		print('Test 6 PASSED!!!\n')
	else:
		print(
			f'Test 6 Failed!\n  Your Output: {uncover_spy(n, trust)}\n  '
			f'Correct Output: {ans}\n'
		)

	# Test 7
	n = 99
	trust = [
		[14, 99], [38, 99], [17, 99], [3, 99], [34, 99], [37, 99], [82, 99],
		[76, 99], [71, 99], [2, 99], [91, 99], [95, 99], [5, 99], [56, 99],
		[7, 99], [25, 99], [20, 99], [54, 99], [72, 99], [67, 99], [43, 99],
		[93, 99], [94, 99], [26, 99], [81, 99], [87, 99], [36, 99], [79, 99],
		[22, 99], [11, 99], [23, 99], [52, 99], [86, 99], [19, 99], [88, 99],
		[55, 99], [4, 99], [21, 99], [51, 99], [83, 99], [92, 99], [73, 99],
		[57, 99], [89, 99], [48, 99], [29, 99], [59, 99], [53, 99], [6, 99],
		[24, 99], [65, 99], [47, 99], [90, 99], [45, 99], [18, 99], [31, 99],
		[13, 99], [49, 99], [64, 99], [97, 99], [70, 99], [40, 99], [60, 99],
		[28, 99], [50, 99], [68, 99], [77, 99], [35, 99], [78, 99], [12, 99],
		[1, 99], [30, 99], [8, 99], [61, 99], [85, 99], [15, 99], [96, 99],
		[98, 99], [69, 99], [62, 99], [84, 99], [58, 99], [27, 99], [42, 99],
		[44, 99], [66, 99], [16, 99], [9, 99], [41, 99], [39, 99], [32, 99],
		[80, 99], [10, 99], [63, 99], [74, 99], [46, 99], [33, 99], [75, 99]
	]
	ans = 99
	if uncover_spy(n, trust) == ans:
		print('Test 1 PASSED!!!')
	else:
		print(
			f'Test 1 Failed!\n  Your Output: {uncover_spy(n, trust)}\n  '
			f'Correct Output: {ans}'
		)
