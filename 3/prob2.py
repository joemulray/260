#!/usr/bin/env python

"""
Joseph Mulray
CS 260: 1/29/2017
HW3: Implimentation
Prob2 : Write a memoisation 
function as described in class using an array of size 100
"""

import sys

#assume you will never be asked for a number greater than Fib(100)
memolist = [None] * 100 


def memo(num):
	#for function purposes so resets memolist after each passing
	#want closure after each passing in of number

	#set global so resets values outside of function
	global memolist
	memolist = [None] * 100 

	fib2(num)


def fib2(num):
	#fib2, takes number in as paramter

	#let Fib(0)=1, and Fib(1)=1.
	if num <= 1:
		return 1

	# if memolist[num] exists: return that number
	if memolist[num]:
		return memolist[num]

	#does not exist populate that number
	memolist[num] = fib2(num - 1) + fib2( num - 2)

	#return value of that number
	return memolist[num]


if __name__ == '__main__':
	
	#set number equal to argument the argument 
	num = int(sys.argv[1])
	print fib2(num)


