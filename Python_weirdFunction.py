#!/usr/bin/env python
#-*- coding : utf-8 -*-

"""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

"""

def weird(n):
    t = n%2
    if (t != 0) | (t==0) & (6<=n<=20):
        s = "Weird"
    elif t==0 & (2<=n<=5) | t==0 & (n>20):
        s = "Not Weird"
    return s

if __name__ == '__main__':
    n = int(raw_input())
    print weird(n)
