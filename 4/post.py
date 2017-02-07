#!/usr/bin/env python

"""
Joseph Mulray
2/7/17
HW4: Implimentation
Print the expression, from the parse tree, in pre-order,
in-order, and post-order.
"""

from lexer import *

class tree():
    #class to represent Parse Tree, set default to none if DNE
	def __init__(self, label=None, left=None, right=None):
		self.node = label
		self.left = left
		self.right = right


def isOperator(token):
	#function returns bool, if is operator
	operator = ['*','+','/','-','(',')']

	if token in operator:
		return True
	return False


def parse():

	stack = []
	token = get_next_token()

	while token:
		if isOperator(token):
			#When you hit an operator, take 2 expressions subtrees from the stack
			right = stack.pop()
			left = stack.pop()
			stack.append(tree(token + " " ,left,right))

		else:
			#if is a nuber append token to stack
			stack.append(tree(token + " "))

		#get the value of next token
		token = get_next_token()

	return stack.pop()


def post(tree):
	#returns postfix expression, takes tree and gets values left and write of node
	if tree is not None:
		return post( tree.left ) + post( tree.right) + tree.node

	return ''


def pre(tree):
	#returns the prefix expr, takes tree and returns label, left and right side of tree
	if tree is not None:
		return tree.node + pre( tree.left ) + post( tree.right)

	return ''


def infix(tree):
	#if the tree is not empty, return left side, label, then right side
	if tree is not None:
		return pre( tree.left ) + tree.node + post( tree.right)

	return ''


def output(tree):
		#output values in pre, infix, and postfix
		print "pre: %s " % pre(bTree)
		print "in: %s" % infix(bTree)
		print "post: %s\n" % post(bTree)

if __name__ == '__main__':
	#while there is an expression available from stdin
	while get_expression():
		#create and populate Tree
		bTree = parse()
		#output the tree in each format
		output(bTree)
