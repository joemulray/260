#!/usr/bin/env python

"""
Joseph Mulray
1/20/17
CS 260 HW2: Implimentation
problem2: function that takes two lists and returns 
a list that is the concatenation of both of them, but 
without re-using the data
"""

from cell import Cell

def list_concat_copy(A, B):
	
	#create a new list with A element start as head
	concat = Cell(A.data)
	temp = concat
	
	#cycle through list A and B creating new cell for each element
	while A.next != None:
		temp.next = Cell(A.next.data)
		A = A.next

	temp = B.next

	while B.next != None:
		temp.next = Cell(B.next.data)
		B = B.next

	#return the concatenated list
	return concat
