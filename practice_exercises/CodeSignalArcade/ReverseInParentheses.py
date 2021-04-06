"""
Write a function that reverses characters in (possibly nested) parentheses
	in the input string.

Input strings will always be well-formed with matching ()s.

Example:

- For inputString = "(bar)", the output should be:
	reverseInParentheses(inputString) = "rab";

- For inputString = "foo(bar)baz", the output should be:
	reverseInParentheses(inputString) = "foorabbaz";

- For inputString = "foo(bar)baz(blim)", the output should be:
	reverseInParentheses(inputString) = "foorabbazmilb";

- For inputString = "foo(bar(baz))blim", the output should be:
	reverseInParentheses(inputString) = "foobazrabblim".
	- Because "foo(bar(baz))blim" becomes "foo(barzab)blim"
		and then "foobazrabblim".

Input/Output:

[execution time limit] 4 seconds (py3)

[input] string inputString
	A string consisting of lowercase English letters and the characters ( and ).
	It is guaranteed that all parentheses in inputString form a
		regular bracket sequence:
			A bracket sequence is called regular if it is possible to insert
				some numbers and signs into the sequence in such a way that
				the new sequence will represent a correct arithmetic expression.

	Guaranteed constraints:
		0 ≤ inputString.length ≤ 50.

[output] string
	Return inputString, with all the characters that were
		in parentheses reversed.
"""
"""
Understanding:
- If the chars are inside nested (), need to reverse the chars in the inner 
most () and remove those ().
- Then work my way out to outer most () reversing and deleting () along the way.
- Final string should not have any () left in it.

Plan:
- Iterate through the string to find the (chars)
- Once I have reversed the chars in the () remove the ()
- After all () found, return the new string.
"""


def reverseInParentheses(inputString):
	# Assign the inputString to a new variable to make a copy
	s = inputString

	# Check if the inputString is empty or has only ()
	if s == '' or s == '()':
		return ''

	# Iterate through the string while there are still ()
	while '(' in s:
		# Get the index for the opening parentheses
		open_idx = s.rfind('(')
		# Get the index for the closing parentheses
		close_idx = s.find(')', open_idx + 1)
		# Create a window to search for nested ()
		in_pars = s[open_idx + 1: close_idx]

		# Check if there is a nested () in window
		if '(' in in_pars:
			# Get the index for the opening parentheses
			nest_open = s[open_idx + 1: close_idx].rfind('(')
			# Get the index for the closing parentheses
			nest_close = s[open_idx + 1: close_idx].find(')', nest_open + 1)
			# Add the reversed string from inside the nested (), while
			# deleting the ( and ) at the same time
			s = s[:nest_open] + s[nest_open + 1:nest_close][::-1] + s[
			                                                        nest_close
			                                                        + 1:]

		# If there are no nested ()
		else:
			# Add the reversed string from inside the () while deleting the (
			# and ) at the same time.
			s = s[:open_idx] + s[open_idx + 1:close_idx][::-1] + s[
			                                                     close_idx + 1:]

	# Return the final string
	return s


"""
CodeSignal Tests:

Test 1
Input:
inputString: "(bar)"
Expected Output:
"rab"

Test 2
Input:
inputString: "foo(bar)baz"
Expected Output:
"foorabbaz"

Test 3
Input:
inputString: "foo(bar)baz(blim)"
Expected Output:
"foorabbazmilb"

Test 4
Input:
inputString: "foo(bar(baz))blim"
Expected Output:
"foobazrabblim"

Test 5
Input:
inputString: ""
Expected Output:
""

Test 6
Input:
inputString: "()"
Expected Output:
""

Test 7
Input:
inputString: "(abc)d(efg)"
Expected Output:
"cbadgfe"
"""