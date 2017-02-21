#!/usr/bin/python

class node23 :
	'''a node in a 2-3 tree'''

	def __init__( self ) :
		self.keys = []
		self.kids = []


class tree23 :
	'''Just a wrapper, holds the root of the tree'''

	def __init__( self ) :
		self.root = node23()

# Of course, you'll want to fill in function definitions so this does
# something!


def create():
    return tree23()

def insert( T, x ) :
	'''inserts x into 2-3 tree T
	Calls insert_aux on T.root'''

	nc = insert_aux( T.root, x )

	if nc is not None :	# then the tree actually grows, at the top
		nk, nt = nc
		new_root = node23()
		new_root.keys = [nk]
		new_root.kids = [ T.root, nt ]

		T.root = new_root

def insert_aux( t, x ) :
	'''recursively inserts x into tree t
	returns tuple if split:  ( key, new (right) sibling ),
		None otherwise'''

		# if leaf, gets inserted *here*
	if len( t.kids ) == 0 :
		t.keys.append( x )
		t.keys.sort()
	
	else :	# not a leaf.  Keep looking
			# choose subtree for insertion
		if x < t.keys[0] :
			c = 0
		elif len( t.keys ) == 1 or x < t.keys[1] :
			c = 1
		else :
			c = 2
		
		nc = insert_aux( t.kids[c], x )

		if nc is not None :		# our child split
			nk, nt = nc		# break out new key, new (right) tree
			t.keys.insert( c, nk )
			t.kids.insert( c+1, nt )

		# does *this* node need to split?
	if len( t.keys ) > 2 :
			# make new right sibling
		rs = node23()
		rs.keys = t.keys[2:]
		rs.kids = t.kids[2:]

		nk = t.keys[1]	# save median value out, for promotion

			# this node will be the left sibling
		t.keys = t.keys[0:1]
		t.kids = t.kids[0:2]

		return ( nk, rs )


def delete( T, x ) :
    return

def test( T, x ) :
    return

def walk( T ) :
	'''calls walk_aux() on T.root
	Returns: list'''

	return walk_aux( T.root )

def walk_aux( t ) :
	if t is None :
		return []

		# check for leaf
	if len( t.kids ) == 0 :
		rV = t.keys
		return rV

	rV = walk_aux( t.kids[0] )
	rV.append( t.keys[0] )
	rV.extend( walk_aux( t.kids[1] ))
	if len( t.keys ) == 2 :
		rV.append( t.keys[1] )
		rV.extend( walk_aux( t.kids[2] ))
	
	return rV


def printTree( t, l=0 ) :
	if t is None :
		return

	print "  "*l,
	for i in t.keys :
		print i,
	print

	for i in t.kids :
		printTree( i, l+1 )


def main() :

	l = [ 3, 5, 10, 13, 16, 24 ]

	T = create()

	for i in l :
		print "### inserting ", i
		insert( T, i )
	
	printTree( T.root )
	
	result = walk( T )

	print "l:", l
	print "result:", result


if __name__ == "__main__" :
	main()
