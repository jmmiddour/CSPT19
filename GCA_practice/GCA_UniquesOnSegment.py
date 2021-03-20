"""
You are given an array of integers numbers and an integer k. Your task is to count the number of contiguous subarrays containing at least k numbers which appear exactly once in this subarray.

Example

For numbers = [1, 2, 1, 1] and k = 2, the output should be uniquesOnSegment(numbers, k) = 2.

There are 2 subarrays satistfying the criteria of containing at least k = 2 numbers exactly once:

numbers[0..1] = [1, 2]
numbers[1..2] = [2, 1]
Note that the subarray numbers[0..2] = [1, 2, 1] is not counted because the number 1 appears twice, so only one number appears exactly once in this subarray.

For numbers = [1, 2, 3, 4, 1] and k = 3, the output should be uniquesOnSegment(numbers, k) = 6.

There are 6 subarrays that satisfy the criteria of containing at least k = 3 numbers occuring exactly once:

numbers[0..2] = [1, 2, 3]
numbers[0..3] = [1, 2, 3, 4]
numbers[0..4] = [1, 2, 3, 4, 1]
numbers[1..3] = [2, 3, 4]
numbers[1..4] = [2, 3, 4, 1]
numbers[2..4] = [3, 4, 1]
For numbers = [5, 5, 5, 5] and k = 2, the output should be uniquesOnSegment(numbers, k) = 0.

There are no subarrays with at least k = 2 different numbers.

For numbers = [5, 5, 5, 5] and k = 1, the output should be uniquesOnSegment(numbers, k) = 4.

There are 4 subarrays that satisfy the criteria of containing at least k = 1 occuring exactly once:

numbers[0..0] = [5]
numbers[1..1] = [5]
numbers[2..2] = [5]
numbers[3..3] = [5]
Input/Output

[execution time limit] 6 seconds (py3)

[input] array.integer numbers

An array of integers.

Guaranteed constraints:
3 ≤ numbers.length ≤ 2000,
0 ≤ numbers[i] ≤ 104.

[input] integer k

The minimal amount of unique numbers in the subarray.

Guaranteed constraints:
1 ≤ k ≤ 2000.

[output] integer

Return the number of contiguous subarrays each of which contains at least k elements occuring exactly once.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print "This prints to the console when you Run Tests"
    return "Hello, " + name
"""

