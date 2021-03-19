"""
Given a square matrix of positive integers a, your task is to sort the numbers in each of its diagonals parallel to the secondary diagonal. Each diagonal should contain the same set of numbers as before, but sorted in ascending order from the bottom-left to top-right.

Example

For

a = [[1, 3, 9, 4],
     [9, 5, 7, 7],
     [3, 6, 9, 7],
     [1, 2, 2, 2]]
the output should be

diagonalsSort(a) = [[1, 9, 9, 7],
                    [3, 5, 6, 9],
                    [3, 4, 7, 7],
                    [1, 2, 2, 2]]
example

The diagonals parallel to the secondary diagonal in the initial matrix (left-to-right, bottom-to-top) are:

1
9, 3
3, 5, 9
1, 6, 7, 4
2, 9, 7
2, 7
2
For

a = [[10, 1],
     [7, 5]]
the output should be

diagonalsSort(a) = [[10, 7],
                    [1, 5]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

A square matrix of integers.

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 100.

[output] array.array.integer

The same array with sorted diagonals.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print "This prints to the console when you Run Tests"
    return "Hello, " + name
"""

"""

"""


def diagonalsSort(a):
