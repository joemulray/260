#!/usr/bin/python
#
# dijkstra.py - single-source, shortest path.  Here for an example to my
#		students, adapted from Kormen, Leiserson, et. al., and Aho, Hopcroft,
#		and Ullman.
#
# Kurt Schmidt
# 2/07
#
# editor:  tabstop=2, cols=80
#
# Credit where credit is due:
#		I took the representation of a Graph from David Eppstein, UC Irvine:
#		 http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
#		His implementation of Dijkstra is rather sexy, and well worth further
#		study.
#
#	This Dijkstra algorithm is (admittedly) less efficient.  It is here for
#		demonstration purposes.
#
# NOTES
#		the PQ is, indeed, a min-priority queue.  But, keys of elements might
#		change while on the queue, so, you could maintain a paralell dictionary
#		of nodes in a heap, and upheap a node when it changes (we will only
#		decrease distances, never the other way).
#
#		For legibility, extract_min() will simply scan the list; I won't
#		maintain a heap here.
#
#		Since PQ maintains the set G(V)\S, we don't really need to keep S
#
#		From our graph, G[v][w] is the weight of edge (v,w), (None if
#		non-existent)
#

DEBUG = False
TRACE = True

import sys
import graph

INF = float( 'infinity' )

def extractMin( S, d ) :
	'''given S, set of vertices, d, array of est. distances,
	Returns vertex w/smallest est. distance (in linear time)'''

	minIdx = 0
	for i in range( 1, len( S )) :
		if d[S[i]] < d[S[minIdx]] :
			minIdx = i
	
	rV = S.pop( minIdx )
	return rV


def dijkstra( G, source ) :

	if DEBUG or TRACE :
		graph.display( G )

	if DEBUG and not source in G :
		print "\nError!  source node not in graph!  Exiting.\n"
		sys.exit( 1 )

		# INIT
	PQ = []	# Priority Queue of nodes, G\S
					# NOTE: we need to update members, update keys on the fly
	D = {}	# est. length of shortest special paths to each node
					# (updated as nodes are moved to S)
	P = {}	# dictionary of predecessors

		# init distance, predecessor, for each vertex in G
	for v in G :
		D[v] = INF
		P[v] = None

		# add all vertices of G to our "undiscovered" set
	PQ = G.keys()[:]

	D[source] = 0 # source will be the first one out of the PQ
	
		# HERE WE GO
	while PQ :	# while we haven't discovered everybody
		u = extractMin( PQ, D )

			# relax distances around new node
		for v in G[u] :		# ualk adjacency list
			if D[u] + G[u][v] < D[v] :
				D[v] = D[u] + G[u][v] 
				P[v] = u

	return (D,P)


	# Not using this at the moment.  Was from Mr. Eppstein, so, I left it
	# here.
def shortestPath( G, start, end ):
	"""
	Find a single shortest path from the given start vertex
	to the given end vertex.
	The input has the same conventions as Dijkstra().
	The output is a list of the vertices in order along
	the shortest path.
	"""

	Path = []

	D,P = Dijkstra( G, start, end )

	Path.append( end )
	while end != start:
		end = P[end]
		Path.append( end )

	Path.reverse()
	return Path


def main( args=None ) :

	G = graph.build( "6.9" )

	d,p = dijkstra( G, '1' )
	print "### main> past dijkstra"

	print "d is:", d
	print "p is:", p


if __name__ == '__main__' :
	main( sys.argv )
