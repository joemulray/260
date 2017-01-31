#!/usr/bin/env python

"""
Joseph Mulray
CS 260: 1/29/2017
HW3: Implimentation
Prob 1: A simple recursive fib function 
without using memoisation
"""

import sys


def fib(num):
	#fib function passes in num from arugment

	#let Fib(0)=1, and Fib(1)=1.
	if num <= 1:
		return 1

	#use recursion to calculate the fib numbers
	return fib(num - 1) + fib(num - 2)



if __name__ == '__main__':

	#set number equal to argument the argument 
	num = int(sys.argv[1])
	print fib(num)	