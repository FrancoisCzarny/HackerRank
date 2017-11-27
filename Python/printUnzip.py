#!/usr/bin/env python
# -*- coding : utf-8 -*-

"""
Task
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.
"""

# first version 
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    l = []
    for i in range(1,n+1):
        l.append(i)
    print(*l, sep='')

# second version
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    print(*[i for i in range(1, n+1)], sep='')
