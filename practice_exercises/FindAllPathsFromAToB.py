"""
You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1.

graph[a] is a list of all nodes b for which the edge a -> b exists.

Example:

![](https://codesignal.s3.amazonaws.com/uploads/1601416906699/Screen_Shot_2020-09-29_at_3.01.34_PM.png)

Input: graph = [[1, 2],[3],[3],[4],[]]
Output: [[0,1,3,4], [0,2,3,4]]

Note:
	The results must be returned in sorted order.
	You can use any built-in sort method on the results array at the
		end of your function before returning.

[execution time limit] 4 seconds (py3)

[input] array.array.integer graph

[output] array.array.integer
"""


def csFindAllPathsFromAToB(graph):
	"""
	Understanding:
	- Given a DIRECTED ACYCLIC Graph containing `n` nodes
	- Need to find all possible paths from node `0` to `n - 1`
	- Need to return the results in sorted order
	"""
	# Create a results list to hold the nested lists of paths
	result = []
	# Create a path list to get each path before adding to the results list
	path = [0]
	# Use a helper function
	helper(graph, path, result)
	# Return the results
	return result


def helper(graph, path, result):
	# Update the index position as the function recurses to get the current
	# index location
	idx = path[-1]

	# If there is still values in graph at the current index...
	if graph[idx]:
		# Traverse the sorted graph at the current index
		for i in sorted(graph[idx]):
			# Assign the new path to its own nested list
			new_path = path + [i]
			print(f'New Path: {new_path}')
			# Recurse back through the helper function until all of the
			# vertices have been seen
			result = helper(graph, new_path, result)

	# Once all vertices have been seen and edges recorded
	else:
		# Add the path to the results list
		result += [path]

	# Return results list
	return result

# # Check edge case of empty graph list
# if graph is None:
#     return []

# # Create an adjacency list (dict and sets) with the given graph values
# # Iterate through the graphs list
# # For each nested list, add it as the values as a set and the index
# location as the key in the dictionary
# adj_list = {k:set(v) for k, v in enumerate(graph)}
# # print(adj_list)

# # Create a list to hold the results in
# results = []

# # Iterate through the adjacency list to pull all the vertices and find
# their edges (connections)
# for idx, val in adj_list.items():
#     print(f'Index: {idx}, Value: {val}')
#     for i in adj_list[idx]:
#         print(f'i in adj_list[idx]: {i}')

#     # if
#     # results.append([idx.keys() + idx.keys() if idx in val[idx].values()])
#     # Check if the next idx is in the vals of the current idx
#     # if adj_list[idx] in adj_list.items():
#     #     results.append([x for x in adj_list[idx]])
#     #     print(results)

# return results


# Testing
if __name__ == '__main__':
	# Test 1
	graph = [[1, 2], [3], [3], []]
	ans = [[0, 1, 3], [0, 2, 3]]
	if ans == csFindAllPathsFromAToB(graph):
		print('Test 1 PASSED!!!\n')
	else:
		print(f'Test 1 Failed:\nYour Output:'
		      f' {csFindAllPathsFromAToB(graph)}\nCorrect Output: {ans}\n')

		# Test 2
		graph = [[4,3,1], [3,2,4], [3], [4], []]
		ans = [[0,1,2,3,4], [0,1,3,4], [0,1,4], [0,3,4], [0,4]]
		if ans == csFindAllPathsFromAToB(graph):
			print('Test 2 PASSED!!!\n')
		else:
			print(f'Test 2 Failed:\nYour Output:'
			      f' {csFindAllPathsFromAToB(graph)}\nCorrect Output: {ans}\n')

		# Test 3
		graph = [[1], []]
		ans = [[0, 1]]
		if ans == csFindAllPathsFromAToB(graph):
			print('Test 3 PASSED!!!\n')
		else:
			print(f'Test 3 Failed:\nYour Output:'
			      f' {csFindAllPathsFromAToB(graph)}\nCorrect Output: {ans}\n')
