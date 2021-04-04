"""
There are some lamps placed on a coordinate line. Each of these lamps
	illuminates some space around it within a given radius. You are given
	the coordinates of the lamps on the line, and the effective radius
	of each of the lamps' light.

In other words, you are given a two-dimensional array lamps, where lamps[i]
	contains information about the ith lamp. lamps[i][0] is an integer
	representing the lamp's coordinate, and lamps[i][1] is a positive integer
	representing the effective radius of the ith lamp. That means that the
	ith lamp illuminates everything in a range from lamps[i][0] - lamps[i][1]
	to lamps[i][0] + lamps[i][1] inclusive.

Your task is to find the coordinate of the point that is illuminated by the
	highest number of lamps. In case of a tie, return the point among them
	with the minimal possible coordinate.

Example:

For lamps = [[-2, 3], [2, 3], [2, 1]], the output should be:
	theMostLightenedPoint(lamps) = 1.

https://codesignal.s3.amazonaws.com/tasks/theMostLightenedPoint/img/example1.gif?_tm=1617298405423

- The first lamp illuminates everything in range [-2 - 3, -2 + 3] = [-5, 1].
- The second lamp illuminates everything in range [2 - 3, 2 + 3] = [-1, 5].
- The third lamp illuminates everything in range [2 - 1, 2 + 1] = [1, 3].
- The only point that is illuminated by all of the lamps is 1,
	hence the answer is 1.

For lamps = [[-2, 1], [2, 1]], the output should be:
	theMostLightenedPoint(lamps) = -3.

https://codesignal.s3.amazonaws.com/tasks/theMostLightenedPoint/img/example2.gif?_tm=1617298405856

- The given lamps illuminate ranges [-3, -1] and [1, 3] respectively.
- Every point in these ranges are illuminated by only 1 lamp, but the one
	with the minimal coordinate among them is -3, so it is the answer.

Input/Output:

[execution time limit] 4 seconds (py3)

[input] array.array.integer lamps
	A two-dimensional array containing information about the lamps.
	Each lamp is described by a two-element array containing the coordinate
		and the effective radius of the lamp.

	Guaranteed constraints:
		1 ≤ lamps.length ≤ 105,
		lamps[i].length = 2,
		-109 ≤ lamps[i][0] ≤ 109,
		1 ≤ lamps[i][1] ≤ 105.

[output] integer
	The coordinate of the point with the smallest coordinate that is
		illuminated by the most number of lamps.
"""

def theMostLightenedPoint(lamps):
