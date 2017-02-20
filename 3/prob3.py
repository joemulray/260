#!/usr/bin/env python

"""
Joseph Mulray
CS 260: 1/29/2017
HW3: Implimentation
Prob3: Use the timing function from homework 2 to 
print a table of Fibonacci numbers from 1 to 40 
"""

#import statements
import sys, timeit
from prob1 import fib
from prob2 import memo


#helper functions for timeit
def problem1(num):
	fib(num)


def problem2(num):
	memo(num)


if __name__ == '__main__':
	#cycle through 40 numbers
	for num in range(1,41):
        #Timing functions for timeit, calls prob1 and prob2 computes time
		prob1Timer = timeit.Timer('problem1(num)', 'from __main__ import problem1, num')
		prob2Timer = timeit.Timer('problem2(num)', 'from __main__ import problem2, num')
		prob1Delta = prob1Timer.timeit(1)
		prob2Delta = prob2Timer.timeit(1)

		#display output
		print '%s %s %s' %(str(num), str(prob1Delta), str(prob2Delta))
