#!/usr/bin/env python

"""
Joseph Mulray
1/20/17
CS 260 HW2: Implimentation
problem1: function that takes two lists and returns a 
list that is the concatenation of both of them.
"""

from cell import Cell


def list_concat(A, B):

	#temp holder for list A
	temp = A
	
	#get the last element in the list
	while temp.next != None:
		temp = temp.next

	#assign last element of A to B
	temp.next = B

	#return the concatenated list
	return A


