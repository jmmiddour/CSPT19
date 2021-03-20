"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
"""

"""
Assumptions:
- Given array will contain at least 2 values.
- Given array lenth will = 2 --> 10
- Given array values will = -1000 --> 1000

Test Cases:
input: [3, 6, -2, -5, 7, 3]
worked out: [3*6=18, 6*-2=-12, -2*-5=-10, -5*7=-35, 7*3=21] --> 7 * 3 = 21
output: 21

input: [3, 6, 9, 5, 4]
worked out: [3*6=18, 6*9=54, 9*5=45, 5*4=20] --> 6 * 9 = 54
output: 54

Plan:
1. Create a sliding window with 2 elements.
2. Create an empty list to hold the products of each set of numbers.
3. Iterate through the given array of numbers.
4. Multiply each set of 2 numbers to get there product and append to product 
list.
5. Return the max value from the product list.
"""


def adjacentElementsProduct(inputArray):
	window = [0, 1]
	prods = []

	while window[1] < len(inputArray):
		prods.append(inputArray[window[0]] * inputArray[window[1]])
		window[0] += 1
		window[1] += 1

	return max(prods)
