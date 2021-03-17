# ### INSTRUCTIONS ### #
"""
Write a function that searches a list of names (unsorted) for the name "Bob"
	and returns the location in the list.
If Bob is not in the array, return -1.
"""

# ### EXAMPLES: ### #
"""
csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2
csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
csWhereIsBob(["Jimmy", "Layla", "James"]) ➞ -1
"""

# ### NOTES: ### #
"""
Assume all names start with a capital letter and are lowercase thereafter
(i.e. don't worry about finding "BOB" or "bob").
"""

# ### PSEUDOCODE ### #
"""
Assumptions:
- Names will be unsorted.
- Names will start with a capital letter and lower case thereafter.
- Possible that "Bob" is not in the list -> return -1

Test Cases:
names = ["Jimmy", "Greg", "Bob", "James", "Bobby"]
output -> 2

names = ["Bobby", "James", "Greg", "Joanne", "Ben"]
output -> -1

names = ["Bob", "Bobby", "Betty", "Ben", "Bob"]
output -> 0

Edge Cases:
- More than one Bob -> Return 1st Bob index.
- Empty List.
- 
"""


# ### SOLUTION ### #
def csWhereIsBob(names):
	if len(names) == 0:
		return -1

	for i in range(len(names)):
		if names[i] == "Bob":
			return i

	return -1


# ### TEST CASES ### #
print(csWhereIsBob(["Jimmy", "Greg", "Bob", "James", "Bobby"]))
print(csWhereIsBob(["Bobby", "James", "Greg", "Joanne", "Ben"]))
print(csWhereIsBob(["Bob", "Bobby", "Betty", "Ben", "Bob"]))
