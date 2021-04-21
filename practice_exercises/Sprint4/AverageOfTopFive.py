"""
Given a list of different students' scores, write a function that returns
	the average of each student's top five scores. You should return the
	averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and
	the student's score (scores[i][1]). The averages should be calculated
	using integer division.

Example 1:

Input: [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65],
		[1, 87], [1, 100], [2, 100], [2, 76]]
Output: [[1, 87], [2, 88]]
Explanation:
	The average student `1` is `87`.
	The average of student `2` is `88.6`, but with integer division is `88`.

Notes:
	The score of the students is between 1 and 100.

[execution time limit] 4 seconds (py3)

[input] array.array.integer scores

[output] array.array.integer
"""
from collections import defaultdict


def csAverageOfTopFive(scores):
	"""
	Understanding:
		- Given a 2d list of [student, score]
		- Need to return the average score for each students' top 5 scores
		- The return 2d list needs to have [student, avg score] and
			needs to be in ascending order based on student id
	"""
	# Create a dictionary to hold the student scores for each student
	students = defaultdict(list)
	# Create a list to hold tuples with student and score
	score_tups = []
	# Create a final list to return the average for each student
	final = []

	# Iterate through the given list of students and scores
	for i in range(len(scores)):
		# Add a new tuple for each nested list in the given list
		score_tups.append((scores[i][0], scores[i][1]))

	# Iterate over the tuples list to add the key and values to my dictionary
	for stud, score in score_tups:
		# Update the dictionary at that key to include the new score
		students[stud].append(score)

	# Sort the current scores in descending order
	results = {key: sorted(students[key], reverse=True) for key in
	           sorted(students)}

	# Need to iterate over the key value pairs
	for key, val in results.items():
		# If the key has more than 5 values...
		if len(val) > 5:
			# Keep only the top 5 values
			results[key] = val[:5]

		# Get the average for each key
		results[key] = round(sum(results[key]) // len(results[key]))

		# Turn results into a 2d list
		final.append([key, results[key]])

	# Return my final 2d list
	return final


# Testing
if __name__ == '__main__':
	# Test 1
	scores = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77],
	          [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
	ans = [[1, 87], [2, 88]]
	if csAverageOfTopFive(scores) == ans:
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed!\n  Your Output: {csAverageOfTopFive(scores)}\n  '
		      f'Correct Output: {ans}'\n)

	# Test 2
	scores = [[1,2]]
	ans = [[1,2]]
	if csAverageOfTopFive(scores) == ans:
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed!\n  Your Output: {csAverageOfTopFive(scores)}\n  '
		      f'Correct Output: {ans}'\n)