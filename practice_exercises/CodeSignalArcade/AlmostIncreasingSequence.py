"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
"""

"""
Assumptions:
- If `sequence` is only 1 element it is True
- `sequence` length will be from 2 - 10^5 (will not be empty)
- `sequence` values will be integers from -10^5 - 10^5

Test Cases:
sequence = [1, 3, 2]
worked out --> If 3 is removed [1, 2] is True
output --> True

sequence = [5, 9, 10, 7, 13]
worked out --> If 7 is removed [5, 9, 10, 13] is True
output --> True

Plan:
1. Create an empty list to hold the resulting sequence.
2. Iterate through the `sequence` comparing each element to the next.
3. If the element is not > the prior element and < the next element, remove 
that element.
4. Check that the length of the resulting array is only 1 less than the 
original array.
5. Return True or False based on step 4 and if the array is sorted.
"""

# My Final solution:
def almostIncreasingSequence(sequence):
	def check(sequence):
		for i in range(len(sequence) - 1):
			if sequence[i] >= sequence[i + 1]:
				return i

		return -1

	chk = check(sequence)

	if check == -1:
		return True

	if check(
			sequence[chk - 1: chk] + sequence[chk + 1:]
	) == -1 or check(sequence[chk: chk + 1] + sequence[chk + 2:]) == -1:
		return True

	return False

# # Another solution from pharfenmeister on Code Signal
# def almostIncreasingSequence(sequence):
#     droppped = False
#     last = prev = min(sequence) - 1
#     for elm in sequence:
#         if elm <= last:
#             if droppped:
#                 return False
#             else:
#                 droppped = True
#             if elm <= prev:
#                 prev = last
#             elif elm >= prev:
#                 prev = last = elm
#         else:
#             prev, last = last, elm
#     return True

# # Another solution from coells on Code Signal
# def almostIncreasingSequence(s):
#     return 3> sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10**6]))

# # Another solution from djurado on Code Signal
# def almostIncreasingSequence(sequence):
#     f1 = sum([1 for a, b in zip(sequence[:-1], sequence[1:]) if a>=b ]) <= 1
#     f2 = sum([1 for a, c in zip(sequence[:-2], sequence[2:]) if a>=c ]) <= 1
#     return f1 and f2

# # Another solution from bandorthild on Code Signal
# def almostIncreasingSequence(sequence):
#     c = 0
#     for i in range(len(sequence)-1):
#         if sequence[i] >= sequence[i+1]: c += 1
#         if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: c += 1
#     return c < 3

# # Another solution from ashwin_m8 on Code Signal
# def first_bad_pair(sequence):
#     """Return the first index of a pair of elements where the earlier
#     element is not less than the later elements. If no such pair
#     exists, return -1."""
#     for i in range(len(sequence)-1):
#         if sequence[i] >= sequence[i+1]:
#             return i
#     return -1
#
# def almostIncreasingSequence(sequence):
#     """Return whether it is possible to obtain a strictly increasing
#     sequence by removing no more than one element from the array."""
#     j = first_bad_pair(sequence)
#     if j == -1:
#         return True  # List is increasing
#     if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
#         return True  # Deleting earlier element makes increasing
#     if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
#         return True  # Deleting later element makes increasing
#     return False  # Deleting either does not make increasing

# # Another solution from abbey_m on Code Signal
# def almostIncreasingSequence(sequence):
# 	fails1 = 0
# 	fails2 = 0
#
# 	for i in range(len(sequence) - 1):
# 		if sequence[i] >= sequence[i + 1]:
# 			fails1 = fails1 + 1
#
# 	for i in range(len(sequence) - 2):
# 		if sequence[i] >= sequence[i + 2]:
# 			fails2 = fails2 + 1
#
# 	if (fails1 < 2) and (fails2 < 2):
#
# 		return True
# 	else:
# 		return False

# # Another solution from alanchou on Code Signal
# def almostIncreasingSequence(sequence):
# 	counter = 0
# 	for i in range(1, len(sequence)):
# 		if sequence[i] > sequence[i - 1]:
# 			continue
# 		elif i == 1 or i == len(sequence) - 1:
# 			counter += 1
# 		elif sequence[i] > sequence[i - 2]:
# 			counter += 1
# 		elif sequence[i + 1] > sequence[i - 1]:
# 			i += 1
# 			counter += 1
# 		else:
# 			return False
#
# 		if counter > 1:
# 			return False
# 	return True

# # Another solution from vanitaw on Code Signal
# def almostIncreasingSequence(sequence):
# 	lst = []
# 	remove_count = 0
# 	index = -1
# 	for n in range(len(sequence) - 1):
# 		if sequence[n] >= sequence[n + 1]:
# 			if remove_count > 0:
# 				return False
# 			remove_count += 1
# 			if n + 1 == len(sequence) - 1 or sequence.count(
# 					sequence[n + 1]) > 1:
# 				index = n + 1
# 			else:
# 				index = n
# 	del sequence[index]
# 	if sequence != sorted(sequence):
# 		return False
# 	if len(list(set(sequence))) != len(sequence):
# 		return False
#
# 	return True

# # Another solution from jsamuelson on Code Signal
# def almostIncreasingSequence(sequence):
#     return 2 >= sum((i >= j) + (i >= k) for i, j, k in zip(sequence, sequence[1:], sequence[2:] + [1e6]))

# # Another solution from gaspa79 on Code Signal
# def almostIncreasingSequence(sequence):
#     problemHere = problemAhead = 0
#     for i in range(len(sequence) - 1):
#         if sequence[i] >= sequence[i+1]:
#             problemHere += 1
#         if i+2 < len(sequence) and sequence[i] >= sequence[i+2]:
#             problemAhead += 1
#     return problemHere < 2 and problemAhead < 2;

# # Another solution from the_logic on Code Signal
# def almostIncreasingSequence(sequence):
#     i = 0
#     while i < len(sequence) - 1:
#         if not sequence[i] < sequence[i + 1]:
#             if increasingSequence(sequence[:i] + sequence[i+1:]) or \
#                     increasingSequence(sequence[:i+1] + sequence[i+2:]):
#                 return True
#             else:
#                 return False
#         i += 1
#     return True
#
#
# def increasingSequence(sequence):
#     for i in range(len(sequence) - 1):
#         if not sequence[i] < sequence[i + 1]:
#             return False
#     return True
