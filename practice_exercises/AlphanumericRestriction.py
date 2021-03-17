# ### INSTRUCTIONS ### #
"""
Create a function that returns True if the given string has
	any of the following:
	- Only letters and no numbers.
	- Only numbers and no letters.

If a string has both numbers and letters or contains characters that
	don't fit into any category, return False.
"""

# ### EXAMPLES: ### #
"""
csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
"""

# ### NOTES: ### #
"""
Any string that contains spaces or is empty should return `False`.
"""

# ### PSEUDOCODE ### #
"""
Assumptions:
- Possible that string is empty or contains spaces -> return `False`
- String can contain upper and lower case letters and/or numbers.

Test Cases:
input_str = "Bold"
output ➞ True

input_str = "123454321"
output ➞ True

input_str = "H3LL0"
output ➞ False

Edge Cases:
- Empty List or spaces.

Plan:
1. Check if the string is empty to check for edge case
2. Use regular expression to find out what if the string matches the patterns.
3. Return True or False.
"""

# ### SOLUTION ### #
import re


def csAlphanumericRestriction(input_str):
	if len(input_str) == 0:
		return False

	if re.search(r'^[a-zA-Z]+$',
	             input_str) or re.search(r'^[0-9]+$', input_str):
		return True

	else:
		return False


# ### TEST CASES ### #
print(csAlphanumericRestriction("Bold"))
print(csAlphanumericRestriction("123454321"))
print(csAlphanumericRestriction("H3LL0"))
