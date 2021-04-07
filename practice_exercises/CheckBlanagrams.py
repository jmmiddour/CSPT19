"""
Two words are
	blanagrams: (blank + anagram; a word which is an anagram of another but
		for the substitution of a single letter; In Scrabble, a blank tile
		on the player's rack that may be used to form any of several
		possible words in conjunction with the player's other tiles)
	if they are anagrams (А string `x` is an anagram of a string `y` if one
		can get `y` by rearranging the letters of `x`.
		For example, the strings `"MITE"` and `"TIME"` are anagrams,
		so are `"BABA"` and `"AABB"`, but `"ABBAC"` and `"CAABA"` are not.)
	but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example:

For `word1 = "tangram"` and `word2 = "anagram"`, the output should be:
	checkBlanagrams(word1, word2) = True;

- After changing the first letter 't' to 'a' in the word1,
	the words become anagrams.

For `word1 = "tangram"` and `word2 = "pangram"`, the output should be:
	checkBlanagrams(word1, word2) = True.

- Since a word is an anagram of itself (a so-called trivial anagram), we are
	not obliged to rearrange letters. Only the substitution of a single letter
	is required for a word to be a blanagram, and here 't' is changed to 'p'.

For `word1 = "aba"` and `word2 = "bab"`, the output should be:
	checkBlanagrams(word1, word2) = True.

- You can take the first letter 'a' of word1 and change it to 'b', obtaining
	the word "bba", which is an anagram of word2 = "bab". It is also possible
	to change the first letter 'b' of word2 to 'a' and obtain "aab", which is
	an anagram of word1 = "aba".

For `word1 = "silent"` and `word2 = "listen"`, the output should be:
	checkBlanagrams(word1, word2) = False.

- These two words are anagrams of each other, but no letter substitution was
	made (the trivial substitution of a letter with itself shouldn't be
	considered), so they are not blanagrams.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] string word1
	A string consisting of lowercase letters.

	Guaranteed constraints:
		1 ≤ word1.length ≤ 100.

[input] string word2
	A string consisting of lowercase letters.

	Guaranteed constraints:
		word2.length = word1.length.

[output] boolean
	Return True if word1 and word2 are blanagrams of each other,
		otherwise return False.
"""

"""
1. Sort each of the strings to verify they have the same characters less only 
one.
2. Check if one letter can be replaced to create word 2.
3. Return True or False if only one letter can be replaced.
"""


def checkBlanagrams(word1, word2):
	# Iterate through word one to check if the same chars as word2 less 1
	for i in range(len(word1)):
		# If the char is in word2
		if word1[i] in word2:
			# remove from word2
			word2 = word2.replace(word1[i], '', 1)

	return len(word2) == 1


# Testing:
if __name__ == '__main__':
	# Test 1
	word1 = "tangram"
	word2 = "anagram"
	ans = True
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 2
	word1 = "tangram"
	word2 = "pangram"
	ans = True
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 3
	word1 = "aba"
	word2 = "bab"
	ans = True
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 4
	word1 = "silent"
	word2 = "listen"
	ans = False
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 5
	word1 = "x"
	word2 = "y"
	ans = True
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 6
	word1 = "z"
	word2 = "z"
	ans = False
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 7
	word1 = "bab"
	word2 = "aba"
	ans = True
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 8
	word1 = "abacaba"
	word2 = "abadaba"
	ans = True
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 9
	word1 = "abacabaabcabcabc"
	word2 = "abadabaabcabcabc"
	ans = True
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 10
	word1 = "abacabaabcabcabd"
	word2 = "abadabaabcabcabc"
	ans = False
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')

	# Test 11
	word1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu"
	word2 = "cabdefghijklmnopqrstuvwzyxabcdefghijklonmpqrstu"
	ans = False
	if checkBlanagrams(word1, word2) == ans:
		print(f'Correct! The answer is: {ans}')
	else: print(f'Wrong! The correct answer is: {ans}')
