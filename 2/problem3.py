#!/usr/bin/env python

"""
Joseph Mulray
1/20/17
CS 260 HW2: Implimentation
problem3: Run your concatenation functions on lists of 
lengths 1,000 through 15,000 and measure how long it takes to run
"""


from cell import Cell
import timeit
from problem1 import list_concat
from problem2 import list_concat_copy


def create_list(size):
	"""creates a list of size and returns """
	concat = Cell(1)
	temp = concat

	for num in range(1, size):
	    temp.next = Cell(num)
	    temp = temp.next

	return concat


def prob1(size):
	"""function creates two list of size, and runs
	list concat"""
	A = create_list(size)
	B = create_list(size)

	list_concat(A, B)

def prob2(size):
	"""function creates two lists again of size, and runs 
	list concat copy"""
	C = create_list(size)
	D = create_list(size)

	list_concat_copy(C, D)


if __name__ == '__main__':

	#cycle through size of list, start 1000 increment
	for size in range(1000,16000,1000):

        #Timing functions for timeit, calls prob1 and prob2 computes time
		prob1Timer = timeit.Timer('prob1(size)', 'from __main__ import prob1, size')
		prob2Timer = timeit.Timer('prob2(size)', 'from __main__ import prob2, size')
		prob1Delta = prob1Timer.timeit(1)
		prob2Delta = prob2Timer.timeit(1)

		#display output
		print '%s\t %s \t%s' %(size, prob1Delta, prob2Delta)
