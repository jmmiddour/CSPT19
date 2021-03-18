# ### INSTRUCTIONS ### #
"""
Write a function that takes a string as input and returns that string in
	reverse order, with the opposite casing for each character
	within the string.
"""

# ### EXAMPLES: ### #
"""
csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
"""

# ### NOTES: ### #
"""
The input string will only contain alpha characters.
"""

# ### PSEUDOCODE ### #
"""
Test Cases:
txt = "Hello World"
output ➞ "DLROw OLLEh"

input_str = "ReVeRsE"
output ➞ "eSrEvEr"

input_str = "Radar"
output ➞ "RADAr"

Edge Cases:
- Empty string.

Plan:
1. Check if the string is empty to check for edge case
2. Turn into a list of characters to iterate through.
3. Change the case of all characters.
4. Join the list back into a string.
5. Return the reversed string.
"""

# ### SOLUTION ### #
import re


def csOppositeReverse(txt):
	if len(txt) == 0:                           # T: 1 - S: 1
		return None                             # T: 1 - S: 1

	txt_list = list(txt)                        # T: 1 - S: n

	for i in range(len(txt_list)):              # T: n - S: 1
		if re.search(r'[A-Z]', txt_list[i]):    # T: 1 - S: 1
			txt_list[i] = txt_list[i].lower()   # T: 1 - S: 1

		elif re.search(r'[a-z]', txt_list[i]):  # T: 1 - S: 1
			txt_list[i] = txt_list[i].upper()   # T: 1 - S: 1

	txt = ''.join(txt_list)                     # T: 1 - S: 1

	return txt[::-1]                            # T: 1 - S: 1

"""
Time Complexity  = O(n)
Space Complexity = O(n)
"""


# ### TEST CASES ### #
print(csOppositeReverse("Hello World"))
print(csOppositeReverse("ReVeRsE"))
print(csOppositeReverse("Radar"))
