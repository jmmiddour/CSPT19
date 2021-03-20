"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer statues

An array of distinct non-negative integers.

Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.

[output] integer

The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.
"""

"""
Assumptions:
- No negative numbers given.
- List given will be unordered
- List given wil not be empty
- List given length = 1-10
- List give values = 0-20
- All values will be unique

Test Case:
statues = [3, 5, 2, 8]
missing = [4, 6, 7]
output = 3

Plan:
1. Create a new list with a length in the range of min - max of values in the 
given list.
2. Compare the given list to the new list and return the difference.
"""


def makeArrayConsecutive2(statues):
	con_statues = range(min(statues), max(statues) + 1)
	if len(con_statues) != len(statues):
		return len(con_statues) - len(statues)

	else:
		return 0
