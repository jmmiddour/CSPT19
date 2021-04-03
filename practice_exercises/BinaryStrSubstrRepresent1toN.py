"""
LeetCode: 1016: Binary String With Substrings Representing 1 To N
(Medium difficulty)

Given a binary string `S` (a string consisting only of '0' and '1's) and
	a positive integer `N`, return `True` if and only if, for every integer `X`
	from `1` to `N`, the binary representation of `X` is a substring of `S`.

Example 1:

	Input: `S = "0110", N = 3`
	Output: `True`

Example 2:

	Input: `S = "0110", N = 4`
	Output: `False`

Note:

	`1 <= S.length <= 1000`
	`1 <= N <= 10^9`
"""
"""
Test Cases:
S = '0110'
N = 3
output = True
explanation --> 3 = 11 in binary --> 11 is a substring of S
                2 = 10 in binary --> 10 is a substring of S
                1 = 1 in binary --> 1 is a substring of S

S = '0110'
N = 4
Output = False
explanation --> 4 = 100 in binary --> not a substring of S (can return False at this step)
                3 = 11 in binary --> 11 is a substring of S
                2 = 10 in binary --> 10 is a substring of S
                1 = 1 in binary --> 1 is a substring of S

S = '0110111001'
N = 13
Output = False
explanation --> 13 = 1101 in binary --> 1101 is a substrong of S
                12 = 1100 in binary --> 1100 is a substring of S
                11 = 1011 in binary --> 1011 is a substring of S
                10 = 1010 in binary --> 1010 is not a substring of S (return False here)

Plan:
1. Create a list of binary values to represent 1 - N
2. Iterate through the string S to check that all binary values are in the string.
3. Return True if all binary values are in S, False if not all match.    
"""


def query_string(S, N):
	# ### This code works but exceeded the time limit ### #
	# ### NEED TO REFACTOR FOR FASTER TIME ### #
	# bin_vals = [format(int(x), 'b') for x in range(1, N + 1)]
	# # print(bin_vals)
	# results = 0
	#
	# for i in range(len(bin_vals)):
	# 	if bin_vals[i] in S:
	# 		results += 1
	#
	# return results == len(bin_vals)

	# ### Code found at https://leetcode.com/problems/binary-string-with
# -substrings-representing-1-to-n/discuss/260847/JavaC%2B%2BPython-O(S) ### #
	if int(S) == 1:
		return True

	return all(bin(i)[2:] in S for i in range(N, N // 2 - 1, -1))


# Testing:
if __name__ == '__main__':
	S = "011010101010111101010101011111111111111111111111111111111110000000000000011111101010101001010101010101010101010101111010101010111111111111111111111111111111111100000000000000111111010101010010101010101010101010100"
	N = 1000000000

	if query_string(S, N) == False:
		print('Correct!')

	else:
		print('Wrong! Expected: False')
