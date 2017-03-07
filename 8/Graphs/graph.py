#!/usr/bin/python
#
# graph.py - represent a labeled digraph
#		Note: labels may well be weights
#
# Kurt Schmidt
# 2/07
#
# editor:  tabstop=2, cols=80
#
# NOTES
#		This file uses a modified adjacency-list.  Each adj. list is actually,
#		in turn, a dictionary of (neighbor, edgeweight) pairs.  So, finding an
#		edge is O(1), rather than O(|E|).  The space, however, is still
#		O(|V|+|E|)
#
#		Saving an edgeweight as "None" will cause you some problems.  hasEdge()
#		returns None if it fails to find an edge, the edge label otherwise.
#
#		Um, some of these functions are superfluous.  I put them there to maybe
#		make this easier to see, but maybe I shouldn't've.
#
#		To test for a vertex:	G.has_key( v )
#		To test for an edge, from a to b:  G[a].has_key(b)
#		Its weight (label): G[a][b]
#		List of vertices: G.keys()
#
#		initialise() and build() are for convenience
#

import sys

def initialise( V=None ) :
	'''returns an object to which vertices and edges can be added

	V might be an initial list (any iterable object) of vertices

	Returns a dict of dicts, really
	'''

	rV = {}

	if V :
		for v in V :
			rV[v] = {}
	
	return rV


def build( fName ) :
	'''given a filename, file in the format:
		v1 a1,l1 a2,l2 ...
		...
	, where vn are vertices, followed by adjacency list w/labels,
	builds and returns a graph'''

	f = open( fName, 'r' )
	if not f :
		print "### not f\n"
		return None

	rV = {}

	for l in f :
		adj = l.split()
		v = adj[0]
		rV[ v ] = {}
		adj.pop( 0 )
		for p in adj :
			u,w = p.split( ',' )
			if u not in rV :
				rV[u] = {}
			rV[v][u] = float(w)
	
	f.close()

	return rV


def addVert( G, v ) :
	'''Adds vertex labelled v to graph G'''

	if not G.has_key( v ) :
		G[ v ] = {}
		return True
	else :
		return False


def addEdge( G, start, end, label=True ) :
	'''Adds arc start->end, with the optional label
	Note: if start and end do not exist in G, they will be added
	If edge already exists, label will be updated'''

	if not G.has_key( start ) :
		G[ start ] = {}

	if not G.has_key( end ) :
		G[ end ] = {}
	
	G[start][end] = label


def getVertices( G ) :
	'''returns a list of vertices in G'''
	return G.keys()

def hasVert( G, v ) :
	'''returns True if v exists in G, False otherwise'''
	return G.has_key( v )


def getEdge( G, start, end ) :
	'''Returns label of edge if it exists, None otherwise
	Note:  labeling an edge as `None' will cause you some pain'''

	if G.has_key( start ) and G[start].has_key( end ) :
		return G[start][end]
	else :
		return None


def main( argv=None ) :
	'''codes up Figure 6.9 from Aho, Hopcroft, & Ullman'''

	g = initialise( range( 1, 4 ))

	if not hasVert( g, 3 ) :
		print "g doesn't have 3, and it really should!"
		return 1

	if not hasVert( g, 1 ) :
		print "g doesn't have 1, and it really should!"
		return 1

	if hasVert( g, 5 ) :
		print "g  has 5, and it shouldn't!"
		return 1

	addVert( g, 4 )
	if not hasVert( g, 4 ) :
		print "g doesn't have 4, and now it really should!"
		return 1

	addEdge( g, 1, 5, 100 );

	if not hasVert( g, 5 ) :
		print "g doesn't have 5, and now it really should!"
		return 1

	e = getEdge( g, 1, 5 )
	if e is None :
		print "that new edge (1,5) isn't there"
	elif e != 100 :
		print "that new edge (1,5) has weight", e, ", should be 100 "
	
	addEdge( g, 1, 2, 10 )
	addEdge( g, 2, 3, 50 )
	addEdge( g, 1, 4, 30 )
	addEdge( g, 3, 5, 10 )
	addEdge( g, 4, 5, 60 )
	addEdge( g, 4, 3, 20 )
	
	print "\nDone!\n"


def display( G ) :
	'''prints out graph (debugging)'''

	for v in G :
		print v,":",
		for w in G[v] :
			print '  (%s : %s)' % ( w, G[v][w] ),
		print ""


if __name__ == '__main__' :
	sys.exit( main( sys.argv ))
