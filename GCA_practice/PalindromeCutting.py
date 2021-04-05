"""
You are given a string s. Consider the following algorithm applied to this string:

Take all the prefixes:
A prefix is a non-empty string constructed from the first few characters of the string.

For example, string s = "abaca" has five prefixes:

"a"
"ab"
"aba"
"abac"
"abaca"

of the string, and choose the longest palindrome:
A string that doesn't changed when reversed (it reads the same backward and forward).

Examples:

"eye" is a palindrome
"noon" is a palindrome
"decaf faced" is a palindrome
"taco cat" is not a palindrome (backwards it spells "tac ocat")
"racecars" is not a palindrome (backwards it spells "sracecar")

between them.
If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
Your task is to implement the above algorithm and return its result when applied to string s.

Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

Example

For s = "aaacodedoc", the output should be palindromeCutting(s) = "".

The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
Finally the algorithm ends on the empty string, so the answer is "".
For s = "codesignal", the output should be palindromeCutting(s) = "codesignal".
The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

For s = "", the output should be palindromeCutting(s) = "".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string consisting of English lowercase letters.

Guaranteed constraints:
0 ≤ s.length ≤ 1000.

[output] string

The result of the described algorithm.
"""

"""
- Check for edge case of any enpty string, return the empty string
- Iterate through the string if > 2 chars, checking for the longest prefix 
that is a palindrome that is at least 2 chars long.
- Remove the longest prefix if it is a palindrome of at least 2 chars.
- Return the finally string after removing valid palindromes.
"""


def palindromeCutting(s):
	max_pal = 0

	if s == '':
		return s

	print(f'S before loop: {s}')

	if s[:-1] == reversed(s[:-1]):
		s = s.replace(s, '')
		return s

	print(f's after 1st if: {s}')

	for i in range(len(s)):
		for j in range(len(s) - 1):

			if len(s[:j]) > 1 and s[:j] == reversed(s[:j]):
				max_pal += 1

			print(f'max_pal after 1st if: {max_pal}')

			if max_pal >= 2 and s[:j] != reversed(s[:j]):
				s = s.replace(s[:j - 1], '', 1)
				print(f'S in loop: {s}')

	return s


"""
CodeSignal Tests:

Test 1
Input:
s: "aaacodedoc"
Output:
"aaacodedoc"
Expected Output:
""

Test 2
Input:
s: "codesignal"
Output:
"codesignal"
Expected Output:
"codesignal"

Test 3
Input:
s: ""
Output:
""
Expected Output:
""

Test 4
Input:
s: "a"
Output:
"a"
Expected Output:
"a"
Console Output:
S before loop: a
s after 1st if: a

Test 5
Input:
s: "abbab"
Output:
"abbab"
Expected Output:
"b"

Test 6
Input:
s: "aaabba"
Output:
"aaabba"
Expected Output:
"a"

Test 7
Input:
s: "aaaaaaab"
Output:
"aaaaaaab"
Expected Output:
"b"

Test 8
Input:
s: "abbaabbaabba"
Output:
"abbaabbaabba"
Expected Output:
""

Test 9
Input:
s: "abababaaab"
Output:
"abababaaab"
Expected Output:
"b"

Test 10
Input:
s: "bbabbaabaabbbbb"
Output:
"bbabbaabaabbbbb"
Expected Output:
""
"""