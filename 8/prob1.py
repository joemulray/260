#!/usr/bin/env python

"""
Joseph Mulray
CS 260
HW8: Implimentation
Graphs I:
Implement Floyd's all-pairs shortest-path algorithm.
"""

import sys

def info():
	
	data = []
	
	#for each line read in by user add to array
	for line in sys.stdin:
		data.append(line)

	#return array of stdin
	return (data)


def build( data ) :
	#using the build function from graphs
	dict_ = {}

	#read through data dont open file
	for line in data :
		adj = line.split()
		vertice = adj[0]
		dict_[ vertice ] = {}
		adj.pop( 0 )
		for pos in adj :
			u,w = pos.split( ',' )
			if u not in dict_ :
				dict_[u] = {}
			dict_[vertice][u] = float(w)
	
	#return graph
	return dict_



def display(matrix):
	"""function to display given matrix
	using specified format"""


	print "%3s" %"", 
	
	for size in range(len(matrix)):
		print "%3s" %size,

	print

	for size in range(len(matrix)):
		print "%3s" % size,
		for pos in range(len(matrix)):
			print "%3s" % matrix[size][pos],
		print
	print

def initailize(graph):
	"""initailizes a Predecessor matrix and a distance matrix
	from an inputed graph"""

	#intinitalize two matricies
	distance = [[ float("inf") for column in graph] for row in graph]
	pred = [[ 0  for column in graph] for row in graph]

	#populate predecessor matrix with intial nodes
	for row in range(len(pred)):
		for column in range(len(pred)):
			pred[row][column] = row
		

	#fill in non existing postions
	for pos in range(len(distance)):
		distance[pos][pos] = 0

	for pos in range(len(pred)):
		pred[pos][pos] = "-"

	#return both matrices
	return (distance, pred)




def floyd(graph, distance, pred):
	"""floyd all pairs shortest path algorithm"""

	#populate empty matrices with inputted data
	for point in graph:
		for element in graph[point]:
			pos1 = int(point)
			pos2 = int(element)
			data = graph[point][element]

			pred[pos1][pos2] = point
			distance[pos1][pos2] = int(data)
			distance[pos2][pos1] = int(data)

	#using the APSP algorithm cycle through both matrices
	size = len(distance)
	for k in range(size):
		for i in range(size):
			for j in range(size):
				if distance[i][k] + distance[k][j] < distance[i][j]:
					distance[i][j] = distance[i][k] + distance[k][j]
					distance[j][i] = distance[i][k] + distance[k][j]
					pred[i][j] = pred[k][j]
					pred[j][i] = pred[k][j]


	return (distance, pred)

if __name__ == '__main__':

	#get data from user input
	data = info()

	#build the graph from the data given
	graph = build(data)

	#initialize two empty matrices for distance and predecessor
	idist, ipred = initailize(graph)

	#calculate and populate matrices
	distance, pred = floyd(graph, idist, ipred)

	#Display each matrix
	print "Distance Matrix:"
	display(distance)

	print "Predecessor Matrix:"
	display(pred)

	
