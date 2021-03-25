"""
You are given two strings pattern and s. The first string pattern contains only
	the symbols 0 and 1, and the second string s contains only lowercase
	English letters.

Let's say that pattern matches a substring s[l..r] of s if the following 3
	conditions are met:

	- they have equal length;
	- for each 0 in pattern the corresponding letter in the substring is a
		vowel;
	- for each 1 in pattern the corresponding letter is a consonant.

Your task is to calculate the number of substrings of s that match pattern.

Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'.
All other letters are consonants.

Example

[CodeSignal Graphic](
https://codesignal.s3.amazonaws.com/tasks/binaryPatternMatching/img/binaryPatternMatching.gif?_tm=1600839368823
)

For pattern = "010" and s = "amazing", the output should be
	binaryPatternMatching(pattern, s) = 2.
	example:

	* "010" matches s[0..2] = "ama", because both 0s match a, which is a
	vowel, and 1 match m, which is a consonant;

	* "010" doesn't match s[1..3] = "maz", because the first 0 corresponds to
	an m, which is a consonant, not a vowel;

	* "010" matches s[2..4] = "azi", because the first 0 matches an a (
	vowel), 1 matches z (consonant), and the second 0 matches i (vowel);

	* "010" doesn't match s[3..5] = "zin", because the first 0 corresponds to
	a consonant (z);

	* "010" doesn't match s[4..6] = "ing", because the second 0 corresponds
	to the letter g, which is a consonant.

So, there are only 2 matches.

For pattern = "100" and s = "codesignal", the output should be
	binaryPatternMatching(pattern, s) = 0.

There are no double vowels in the string "codesignal", so it's not possible for any of its substrings to match this pattern.

Input/Output

	[execution time limit] 4 seconds (py3)

	[input] string pattern
	A string of 0s and 1s.

	Guaranteed constraints:
	1 ≤ pattern.length ≤ 103.

	[input] string s
	A string of lowercase English letters.

	Guaranteed constraints:
	1 ≤ s.length ≤ 103.

	[output] integer
	The number of substrings of s that match pattern.
"""

"""
Plan:
1. Create a list for all vowels and another variable for a counter.
2. Iterate over string `s` using the given pattern.
3. If the substring matches the pattern, increarse counter varaible.
4. Return the counter variable.
"""


def binaryPatternMatching(pattern, s):
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	counter = 0
	bool_str = []

	for x in range(len(s)):
		if s[x] in vowels:
			(bool_str.append(0))
		else:
			bool_str.append(1)

	print(bool_str)
	print(f'Pattern: {pattern}')

	for i in range(len(bool_str)):
		temp_str = ''.join([str(x) for x in bool_str[i:i + len(pattern)]])
		if temp_str == pattern:
			counter += 1
			print(f'Temp String {i}: {str(temp_str)}, Counter: {counter}')

	return counter


	#
	# for i in range(len(s) - len(pattern)):
	# 	for j in range(len(pattern)):
	# 		window = s[i:i + j]
	# 		for pat in window:
	# 			if (s[i] in vowels) and (
	# 					pattern[j] == '0') or (
	# 					s[i] not in vowels) and (
	# 					pattern[j] != '0'):
	# 				if pattern[j:-1] in window:
	# 					counter += 1
	#
	# return counter


	# print(pat)
	# print(let_str)
	# s_dict = {k:v for k, v in enumerate(s)}
	# count_dict = {}
	# # print(s_dict)
	#
	# for i in range(len(s) - len(pattern)):
	# 	for j in range(len(pattern)):
	# 		if (pattern[j] == '0') and (s[i] in vowels) or (
	# 				pattern[j] == '1') and (s[i] not in vowels):
	# 			count_dict.update(i=True)
	# 		else:
	# 			count_dict[i] = 0
	# 		print(count_dict)
	#
	# 		if count_dict.values() == 1:
	# 			for x in range(len(pattern)):
	# 				if len(count_dict.values()) == len(pattern):
	# 					counter += 1
	#
	# return counter


	# results = []
	#
	# for i in range(len(s) - len(pattern)):
	# 	for j in range(len(pattern)):
	# 		if (pattern[j] == '0' and s[i] in vowels) or (
	# 				pattern[j] == '1' and s[i] not in vowels):
	# 			results.append(True)
	#
	# 		else:
	# 			results.append(False)
	#
	# print(results)



#     begin_index = 0
#     end_index = len(pattern)
#     total = 0
#     for x in range(len(num_string)):
#         if pattern_list == num_string[begin_index:end_index]:
#             total += 1
#             begin_index += 1
#             end_index += 1
#         else:
#             begin_index += 1
#             end_index += 1
#     return num_string



if __name__ == '__main__':

	answers = {1: 2, 2: 0, 3: 2, 4: 2, 5: 2, 6: 2, 7: 0, 8: 4}

	if binaryPatternMatching(pattern="010", s="amazing") == answers[1]:
		print('Test #1 Passed!\n')

	if binaryPatternMatching(pattern="100", s="codesignal") == answers[2]:
		print('Test #2 Passed!\n')

	if binaryPatternMatching(pattern="10", s="amazing") == answers[3]:
		print('Test #3 Passed!\n')

	if binaryPatternMatching(pattern="1010", s="codesignal") == answers[4]:
		print('Test #4 Passed!\n')

	if binaryPatternMatching(pattern="1101", s="cramming") == answers[5]:
		print('Test #5 Passed!\n')

	if binaryPatternMatching(pattern="0101", s="codesignal") == answers[6]:
		print('Test #6 Passed!\n')

	if binaryPatternMatching(pattern="11", s="amazin") == answers[7]:
		print('Test #7 Passed!\n')

	if binaryPatternMatching(pattern="01", s="codesignal") == answers[8]:
		print('Test #8 Passed!')



	# print(f'Test 1: {binaryPatternMatching(pattern="010", s="amazing")} --> '
	#       f'2\n')  # -> 2
	# print(f'Test 2: {binaryPatternMatching(pattern="100", s="codesignal")} --> '
	#       f'0\n')  # -> 0
	# print(f'Test 3: {binaryPatternMatching(pattern="10", s="amazing")} --> '
	#       f'2\n')  # -> 2
	# print(f'Test 4: {binaryPatternMatching(pattern="1010", s="codesignal")} '
	#       f'--> 2\n')  # -> 2
	# print(f'Test 5: {binaryPatternMatching(pattern="1101", s="cramming")} --> '
	#       f'2\n')  # -> 2
	# print(f'Test 6: {binaryPatternMatching(pattern="0101", s="codesignal")} '
	#       f'--> 2\n')  # -> 2
	# print(f'Test 7: {binaryPatternMatching(pattern="11", s="amazin")} --> '
	#       f'0\n')  # -> 0
	# print(f'Test 8: {binaryPatternMatching(pattern="01", s="codesignal")} '
	#       f'--> 4')  # -> 4
