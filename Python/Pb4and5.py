#!/usr/bin/env python
# -*- coding : utf-8 -*-

from __future__ import division

"""
Easy
- Problem 1:
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

- Problem 2:
Read two integers and print two lines. The first line should contain integer division. The second line should contain float division,

You don't need to perform any rounding or formatting operations.
"""

if __name__ == '__main__':
    # First problem
	a = int(raw_input())
    b = int(raw_input())
    print'%i \n%i \n%i' %(a+b, a-b, a*b)

	# Problem 2:
    a = int(raw_input())
    b = int(raw_input())
	print a//b
	print a/float(b)
