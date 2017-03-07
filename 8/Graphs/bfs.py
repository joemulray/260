#!/usr/bin/python
#
# bfs.py - breadth-first search.  Here as an example to my
#		students, adapted from Kormen, Leiserson, et. al., and Aho, Hopcroft,
#		and Ullman.
#
# Kurt Schmidt
# 2/07
#
# editor:  tabstop=2, cols=80
#


import sys
import graph

INF = float( 'infinity' )
( WHITE, GRAY, BLACK ) = range(3)

def bfs( G, source ) :

	color = {} # a status (array-based set, really, w/a dict on the keys)
	dist = {}	# est. length of shortest special paths to each node
						# (updated as nodes are moved to S)
	pred = {}	# dictionary of predecessors

		# a Queue
	Q = []

		# init distance, predecessor 
	for v in G.keys() :
		color[v] = WHITE
		dist[v] = INF
		pred[v] = None

		# add source node to S, remove from Q
	if not source in G.keys() :
		print "\nError!  source node not in graph!  Exiting.\n"
		sys.exit( 1 )

	color[source] = GRAY
	dist[source] = 0
	Q.append( source )

	while Q :	# while we haven't discovered everybody
		u = Q.pop( 0 )

			# expand frontier
		for v in G[u] :		# walk adjacency list
			if color[v] == WHITE :
				color[v] = GRAY
				dist[v] = dist[u] + 1
				pred[v] = u
				Q.append( v )
		color[u] = BLACK

	return ( dist, pred )


def main( args=None ) :

	G = graph.build( "6.9" )

	print "Here is the input graph:"
	graph.display( G )

	distance, predecessor = bfs( G, '1' )

	print "\nHere is the result of the BFS:"
	print "  distance list:\n    ", distance
	print "  predecessor list:\n    ", predecessor


if __name__ == '__main__' :
	main( sys.argv )
