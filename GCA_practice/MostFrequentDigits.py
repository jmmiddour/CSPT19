"""
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be mostFrequentDigits(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of positive integers.

Guaranteed constraints:
1 ≤ a.length ≤ 103,
1 ≤ a[i] < 100.

[output] array.integer

The array of most frequently occurring digits, sorted in ascending order.
"""

"""
Plan:
1. Combine all digits into one large integer, then split them to get a list 
of individual digits.
2. Create a dictionary with the digit as the key and occurance as the value.
3. Iterate over the list for single digits
4. Increase the number of occurances by one each time a digit is seen in the 
list.
5. Return only the digit(s) that appear most in a list in ascending order.
"""


def mostFrequentDigits(a):
	a_str = list(''.join(map(str, a)))
	res_list = [0] * 10
	results = []
	print(res_list)

	for i in range(len(a_str)):
		idx = int(a_str[i])
		res_list[idx] += 1

	print(res_list)

	for i in range(len(res_list)):
		if res_list[i] == max(res_list):
			results.append(i)

	return sorted(results)


# Testing:
if __name__ == '__main__':
	corr1 = [2, 3, 5]
	if mostFrequentDigits([25, 2, 3, 57, 38, 41]) == corr1:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr1}\n'
		      f'Your Output: {mostFrequentDigits([25, 2, 3, 57, 38, 41])}')

	corr2 = [2]
	if mostFrequentDigits([4, 5, 4, 2, 2, 25]) == corr2:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr2}\n'
		      f'Your Output: {mostFrequentDigits([4, 5, 4, 2, 2, 25])}')

	corr3 = [0]
	if mostFrequentDigits([1, 10, 20, 10, 30]) == corr3:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr3}\n'
		      f'Your Output: {mostFrequentDigits([1, 10, 20, 10, 30])}')

	corr4 = [3]
	if mostFrequentDigits([33, 37, 25, 16, 6]) == corr4:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr4}\n'
		      f'Your Output: {mostFrequentDigits([33, 37, 25, 16, 6])}')

	corr5 = [8, 9]
	if mostFrequentDigits([98]) == corr5:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr5}\n'
		      f'Your Output: {mostFrequentDigits([98])}')

	corr6 = [9]
	if mostFrequentDigits([99]) == corr6:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr6}\n'
		      f'Your Output: {mostFrequentDigits([99])}')

	corr7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	if mostFrequentDigits([90, 81, 22, 36, 41, 57, 58, 97, 40, 36]) == corr7:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr7}\n'
		      f'Your Output: {mostFrequentDigits([90, 81, 22, 36, 41, 57, 58, 97, 40, 36])}')

	corr8 = [3, 5]
	if mostFrequentDigits([31, 60, 53, 54, 25, 87, 33, 95]) == corr8:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr8}\n'
		      f'Your Output: {mostFrequentDigits([31, 60, 53, 54, 25, 87, 33, 95])}')

	corr9 = [2, 4, 5, 6, 8]
	if mostFrequentDigits([28, 12, 48, 23, 76, 64, 65, 50, 54, 98]) == corr9:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr9}\n'
		      f'Your Output: {mostFrequentDigits([28, 12, 48, 23, 76, 64, 65, 50, 54, 98])}')

	corr10 = [0, 3, 4, 5, 7, 8, 9]
	if mostFrequentDigits([35, 72, 38, 58, 80, 74, 94, 47, 50, 99, 41, 70, 98, 33, 50]) == corr10:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr10}\n'
		      f'Your Output: {mostFrequentDigits([35, 72, 38, 58, 80, 74, 94, 47, 50, 99, 41, 70, 98, 33, 50])}')

	corr11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	if mostFrequentDigits([47, 50, 63, 85, 64, 62, 92, 29, 18, 70, 96, 50, 87, 73, 90, 98, 55, 24, 13, 70, 30, 17, 22, 84, 13, 91, 35, 46, 21, 69, 30, 15, 77, 40, 35, 85, 91, 98, 60, 82, 64, 98, 56, 47, 84, 20, 16, 13, 74, 32]) == corr11:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr11}\n'
		      f'Your Output: {mostFrequentDigits([47, 50, 63, 85, 64, 62, 92, 29, 18, 70, 96, 50, 87, 73, 90, 98, 55, 24, 13, 70, 30, 17, 22, 84, 13, 91, 35, 46, 21, 69, 30, 15, 77, 40, 35, 85, 91, 98, 60, 82, 64, 98, 56, 47, 84, 20, 16, 13, 74, 32])}')

	corr12 = [2, 3, 5]
	if mostFrequentDigits([25, 2, 3, 57, 38, 41]) == corr12:
		print('Correct!')
	else:
		print(f'Wrong! Expected Output: {corr12}\n'
		      f'Your Output: {mostFrequentDigits([25, 2, 3, 57, 38, 41])}')
