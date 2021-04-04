"""
Given an array of integers `arr` and a positive integer `m`, your task is
	to find the frequency of the most common element within each contiguous
	subarray of length `m` in `arr`.

Contiguous Subarray:
	An array made up of adjacent elements from another array.

	For example, consider arr = [2, 3, 7]:

	[3, 7] is a contiguous subarray of arr
	[2, 3, 7] is a contiguous subarray of arr
	[7] is a contiguous subarray of arr
	[1, 2, 3] is not a contiguous subarray because it contains elements not in arr
	[2, 7] is not a contiguous subarray because the elements aren't adjacent in arr

Return an array of these highest frequencies among subarray elements,
	ordered by their corresponding subarray's starting index.
	You can look at the examples section for a better understanding.

Example:

For `arr = [1, 2]` and `m = 2`, the output should be:
	occurrencesInSubarrays(arr, m) = [1].

https://codesignal.s3.amazonaws.com/tasks/occurrencesInSubarrays/img/example1.gif?_tm=1582075286649

`arr` contains only one contiguous subarray of length
	`m = 2 - arr[0..1] = [1, 2]`.
This subarray contains 2 most frequent elements - `1` and `2`,
	both having a frequency of `1`. So, the answer is `[1]`.

For `arr = [1, 3, 2, 2, 3]` and `m = 4`, the output should be:
	occurrencesInSubarrays(arr, m) = [2, 2].

https://codesignal.s3.amazonaws.com/tasks/occurrencesInSubarrays/img/example2.gif?_tm=1582075286985

`arr` contains two contiguous subarrays of length `m = 4`:

- `arr[0..3] = [1, 3, 2, 2]` contains only one most frequent element - `2`,
	and its frequency is `2`.
- `arr[1..4] = [3, 2, 2, 3]` contains two most frequent elements - `2` and `3`,
	both of them have a frequency of `2`.
- Putting the answers for both subarrays together, we obtain the array `[2, 2]`

For `arr = [2, 1, 2, 3, 3, 2, 2, 2, 2, 1]` and `m = 3`, the output should be:
	occurrencesInSubarrays(arr, m) = [2, 1, 2, 2, 2, 3, 3, 2].

https://codesignal.s3.amazonaws.com/tasks/occurrencesInSubarrays/img/example3.gif?_tm=1582075287360

`arr` contains `8` contiguous subarrays of length `m = 3`:

- arr[0..2] = [2, 1, 2] contains only one most frequent element - 2, and its
frequency is 2.
- arr[1..3] = [1, 2, 3] contains three most frequent elements - 1, 2, and 3.
All of them have frequency 1.
- arr[2..4] = [2, 3, 3] contains only one most frequent element - 3, and its
frequency is 2.
- arr[3..5] = [3, 3, 2] contains only one most frequent element - 3, and its
frequency is 2.
- arr[4..6] = [3, 2, 2] contains only one most frequent element - 2, and its
frequency is 2.
- arr[5..7] = [2, 2, 2] contains only one most frequent element - 2, and its
frequency is 3.
- arr[6..8] = [2, 2, 2] contains only one most frequent element - 2, and its
frequency is 3.
- arr[7..9] = [2, 2, 1] contains only one most frequent element - 1, and its
frequency is 2.
- Putting the answers for both subarrays together,
	we obtain the array `[2, 1, 2, 2, 2, 3, 3, 2]`.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.integer arr
	An array of integers.

	Guaranteed constraints:
		2 ≤ arr.length ≤ 105,
		-109 ≤ arr[i] ≤ 109.

[input] integer m
	An integer representing the length of each subarray.

	Guaranteed constraints:
		2 ≤ m ≤ arr.length.

[output] array.integer
	An array of the highest frequencies in each contiguous subarray
		of length m in arr.
"""