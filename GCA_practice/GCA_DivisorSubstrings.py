"""
You are given two integers, n and k. Consider the string representation of n, and find the number of distinct substrings of length k, such that n is divisible by the number formed by that substring. In other words, how many different numbers formed by k consecutive digits of n are factors of n?

Note: The k-digit substrings may have leading zeros.

Example

For n = 120 and k = 2, the output should be divisorSubstrings(n, k) = 2.

The divisor substrings are 12 and 20 (120 is divisible by both of these).

For n = 555 and k = 1, the output should be divisorSubstrings(n, k) = 1.

All the substrings of length 1 are equal to 5 which is a divisor of 555. The answer is not 3 since we're only counting distinct numbers.

For n = 5341 and k = 2, the output should be divisorSubstrings(n, k) = 0.

5341 is not divisible by 53, 34 nor 41, so the answer is 0.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

An integer representing the number we're trying to find the substring factors of.

Guaranteed constraints:
1 ≤ n ≤ 109.

[input] integer k

An integer representing how many digits long the substrings should be.

Guaranteed constraints:
1 ≤ k ≤ 10,
10k - 1 ≤ n.

[output] integer

The number of distinct substrings of length k which are factors of n.
"""

"""
Assumptions:
- `n` = an integer that is the number we are trying to find the substring 
factors for.
- `n` value will be from 1-10^9
- `k` substring may have leading zeros.
- `k` = an integer that represents how many digits long the substring should be.
- `k` value will be from 1-10

Test Cases:
n = 120
k = 2
worked out --> n[0] = 12, n[1] = 20 (120 / n[0] = 10, 120 / n[1] = 6) = 2 
distinct substrings can go into `n`
output --> 2

n = 5341
k = 2
worked out --> n[0] = 53 (5341 % 53 != 0), n[1] = 34 (5341 % 34 != 0), 
n[2] = 41 (5341 % 41 != 0)
output --> 0

Plan:
1. Convert `n` to string
2. Create a counter variable
3. Create `k` long substrings from `n` with a sliding window.
4. Compare each window to see if original `n` is divisible by that interger.
5. Increase counter by 1 if `n` is divisible by window.
6. Return the counter
"""


def divisorSubstrings(n, k):
	if n == None:
		return 0

	n_str = str(n)
	counter = 0

	for i in range(len(n_str)):
		for j in range(i + k):
			print(n_str[j])
			num = n_str[i: j]
			if n % int(num) == 0:
				counter += 1

	return counter
