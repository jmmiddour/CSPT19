"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.
"""

"""
Assumptions:
- Given year will be a positive integer.
- Assume year = 1 - 2005

Test Cases:
input: 2001
output: 21

input: 1980
output: 20

input: 804
output: 9

Plan:
1. Convert given year from integer to string to manipulate.
2. Use slicing to remove the last 2 characters (digits) from the year string
3. Convert the remaining digits of the year string to integer.
4. Return the integer + 1
"""


def centuryFromYear(year):
	year = str(year)

	if len(year) == 4 or len(year) == 3:
		if 00 < int(year[-2:]) <= 99:
			century = int(year[:-2]) + 1

		else:
			century = int(year[:-2])

	elif len(year) <= 2:
		if 0 < int(year) <= 99:
			century = 1

	return century
