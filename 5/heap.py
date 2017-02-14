#!/usr/bin/env python

"""
Joseph Mulray
HW5: Implimentation
Find an upper bound for the make_heap() algorithm.
1/14/17
"""

import sys
import random
import timeit

class HEAP:

	def __init__(self):
		#intializers
		self.array = []
		self.heap = []


	def make_heap(self, array):

		#declarations
		self.array = array
		size = len(self.array)

		for num in range(size):
			#append each element to heap and downheap nodes
			self.heap.append(self.array[size - (num + 1)])
			self.heap = self.downheap(self.heap)
		
		#return the heap when finished
		return self.heap


	def last_node(self, heap):
		#return last node of the heap
		return len(self.heap) - 1


	def downheap(self, heap):
		#move data down the heap 
	    last = self.last_node(self.heap)
	    parent = last//2

	    #compare values of parent node and last node of heap
	    while (self.heap[parent] > self.heap[last]):

	    	#set swap equal to stack
	        self.heap = self.swap(last,parent ,self.heap)

	        last = parent
	        parent = last//2

	    return self.heap

	def swap(self, last,parent,heap):
		
		#temp place holder
	    node = self.heap[last]

	    #swap last node with parent node
	    self.heap[last] = self.heap[parent]
	    self.heap[parent] = node

	    return self.heap


def create_heap(array):
	"""
	helper function for timeit 
	creation of class and instantiation 
	"""
	heap = HEAP()
	heap.make_heap(array)



if __name__ == '__main__':

	print'\nn\tT(n)'
	#Timing functions for timeit, calls create_heap and computes time
	for size in range(0,16000,1000):
		array=[random.randrange(1,100,1) for num in range (size)]
		heapTimer = timeit.Timer('create_heap(array)', 'from __main__ import create_heap,array')
		heapDelta = heapTimer.timeit(1)
		print "%s\t%s" %(size, heapDelta)
	print''
