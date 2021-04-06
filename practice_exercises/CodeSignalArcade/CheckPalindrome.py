"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
"""

"""
Assumptions:
- No given string will be empty.
- The given string will = 1 - 10^5
- The given string will be all lower case letters.

Test Cases:
input: "racecar"
output: True

input: "racecars"
output: False

input: "taco cat"
output: False

Plan:
1. Create a variable to hold the reverse string
2. Compare the given string to the reversed string.
3. If both strings are the same, return True, if not, return False.
"""

def checkPalindrome(inputString):
    rev_str = inputString[::-1]
    return rev_str == inputString
