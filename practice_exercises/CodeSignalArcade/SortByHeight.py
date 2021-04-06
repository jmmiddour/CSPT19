"""
Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in
	a non-descending order without moving the trees.
People can be very tall!

Example:

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be:
	sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.integer a
	If a[i] = -1, then the ith position is occupied by a tree.
	Otherwise a[i] is the height of a person standing in the ith position.

	Guaranteed constraints:
		1 ≤ a.length ≤ 1000,
		-1 ≤ a[i] ≤ 1000.

[output] array.integer
	Sorted array a with all the trees untouched.
"""
"""
Understanding:
- All -1 in the a list are trees and can not be moved.
- Any value not -1 is a person's height, need to order those around the trees.

Plan:
- Create a list to hold all of the heights of people.
- Iterate through a to get the heights of all the people and append those 
heights to the height only list.
- Sort the height only list from smallest to greatest.
- Replace the values in a with the sorted values for the heights only where 
the value is not -1
- Return the sorted list.
"""


def sortByHeight(a):
	heights = sorted([a[x] for x in range(len(a)) if a[x] != -1])

	for i in range(len(a)):
		if a[i] != -1:
			a[i] = heights.pop(0)

	return a


"""
CodeSignal Tests:

Test 1
Input:
a: [-1, 150, 190, 170, -1, -1, 160, 180]
Output:
[-1, 150, 160, 170, -1, -1, 180, 190]
Expected Output:
[-1, 150, 160, 170, -1, -1, 180, 190]

Test 2
Input:
a: [-1, -1, -1, -1, -1]
Output:
[-1, -1, -1, -1, -1]
Expected Output:
[-1, -1, -1, -1, -1]

Test 3
Input:
a: [-1]
Output:
[-1]
Expected Output:
[-1]

Test 4
Input:
a: [4, 2, 9, 11, 2, 16]
Output:
[2, 2, 4, 9, 11, 16]
Expected Output:
[2, 2, 4, 9, 11, 16]

Test 5
Input:
a: [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
Output:
[1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
Expected Output:
[1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]

Test 6
Input:
a: [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
Output:
[1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
Expected Output:
[1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
"""
