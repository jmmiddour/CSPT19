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

	for i in range(len(s) - len(pattern)):
		for j in range(len(pattern)):
			window = s[i:i + j]
			for pat in window:
				if (s[i] in vowels) and (
						pattern[j] == '0') or (
						s[i] not in vowels) and (
						pattern[j] != '0'):
					if pattern[j:-1] in window:
						counter += 1

	return counter // len(pattern)


if __name__ == '__main__':
	print(binaryPatternMatching(pattern='010', s="amazing"))       # -> 2
	print(binaryPatternMatching(pattern='100', s="codesignal"))    # -> 0