#!/bin/python3

import sys


g = int(input().strip())
for _ in range(g):
    n,m,s = map(int,input().strip().split(' ')) 
    nprev = ((n - 1) * (n - 2)) // 2
    # First case
    if m <= nprev + 1:
        min_sum = (m - 1) + s - n + 2       
    else:
        min_sum = s * m
        vers = m - nprev
        # Second case one edge
        extra = (s - n + 1)
        sm = m + extra * vers
        if sm < min_sum:
            min_sum = sm
        # Second case another edge
        com_num = s // (n - 1)
        extra = (s - com_num * (n - 1))
        sm = m * com_num + extra * vers
        if sm < min_sum:
            min_sum = sm
        # Third case
        if (s % (n - 1) != 0):
            tr_count = (s // (n - 1) + 1) * (n - 1) - s
            tr_num = (s // (n - 1) + 1)
            sm = (tr_num - 1) * ((tr_count * (tr_count + 1)) // 2) + tr_num * (m - (tr_count * (tr_count + 1)) // 2)
            if sm < min_sum:
                min_sum = sm
    print(min_sum)