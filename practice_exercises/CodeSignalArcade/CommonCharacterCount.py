"""
Given two strings, find the number of common characters between them.

Example:

For s1 = "aabcc" and s2 = "adcaa", the output should be:
	commonCharacterCount(s1, s2) = 3.

	Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output:

[execution time limit] 4 seconds (py3)

[input] string s1
	A string consisting of lowercase English letters.

	Guaranteed constraints:
		1 ≤ s1.length < 15.

[input] string s2
	A string consisting of lowercase English letters.

	Guaranteed constraints:
		1 ≤ s2.length < 15.

[output] integer
"""

"""
Plan:
1. Create a counter variable to keep track of the same chars.
2. Iterate through both strings to find the chars that are the same in both.
3. Return the counter
"""

def commonCharacterCount(s1, s2):
    # Create a counter variable
    count = 0

    # Iterate through the 1st string
    for i in range(len(s1)):
        # If the current character is in string 2...
        if s1[i] in s2:
            # Remove that character from string 2
            s2 = s2.replace(s1[i], '', 1)
            # Increament the counter variable
            count += 1

    # Return the count of the same characters
    return count
