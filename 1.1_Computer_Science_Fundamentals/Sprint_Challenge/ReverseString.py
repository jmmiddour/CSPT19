"""
Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

Examples:

csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]
Notes:

Your solution should be "in-place" with O(1) space complexity. Although many in-place functions do not return the modified input, in this case you should.
You should try using a "two-pointers approach".
Avoid using any built-in reverse methods in the language you are using (the goal of this challenge is for you to implement your own method).
[execution time limit] 4 seconds (py3)

[input] array.char chars

[output] array.char
"""

"""
Plan:
Return a reverse list of the given list `chars` using slicing.
"""

def csReverseString(chars):
    return chars[::-1]


if __name__ == '__main__':
	print(
		f'Test 1: {csReverseString(["r", "o", "b", "o", "t"])}\nCorrect '
		f'Output: '
		f'["t","o","b","o","r"]\n')
	print(
		f'Test 2: {csReverseString(["8", "9", "f", "9", "V"])}\nCorrect '
		f'Output: '
		f'["V","9","f","9","8"]\n')
	print(
		f'Test 3: {csReverseString(["2", "I", "9", "V", "K"])}\nCorrect '
		f'Output: '
		f'["K","V","9","I","2"]\n')
	print(
		f'Test 4: '
		f'{csReverseString(["y","x","o","S","_",")","]","-","^","2","I",\'
		f'"a", "\\","L","w","*","x","1","o","`","5",";","C","r","j","<","b",\'
		f'"A","!","*"])}\nCorrect '
		f'Output: '
		f'["*","!","A","b","<","j","r","C",";","5","`","o","1","x","*","w","L",' 
        f'"\\","a","I","2","^","-","]",")","_","S","o","x","y"]')
	print(
		f'Test 5: {csReverseString(["V",
 "n",
 "a",
 "5",
 "6",
 "V",
 "<",
 "n",
 "a",
 "^",
 "(",
 "p",
 "4",
 ":",
 "F",
 "b",
 "(",
 "+",
 "w",
 ".",
 "$",
 "u",
 ">",
 "+",
 "H",
 "8",
 "U",
 "o",
 "!",
 "n"])}\nCorrect '
		f'Output: '
		f'["n",
 "!",
 "o",
 "U",
 "8",
 "H",
 "+",
 ">",
 "u",
 "$",
 ".",
 "w",
 "+",
 "(",
 "b",
 "F",
 ":",
 "4",
 "p",
 "(",
 "^",
 "a",
 "n",
 "<",
 "V",
 "6",
 "5",
 "a",
 "n",
 "V"]')
