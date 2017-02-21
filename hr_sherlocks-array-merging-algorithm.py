#!/bin/python3

import sys

def req(ind, m_rows, left, m_lst, sep_i):
    global n
    global flen
    
    # Check if we've reached the end
    if ind == n - 1:
        return 1
    # Check if we need to shift to the next separation
    if left == 0:
        sep_i += 1
        left = sep_lst[sep_i] - ind
    # Record factorials if out of them
    if flen < m_rows:
        for i in range(flen, m_rows):
            fact_table.append(fact_table[i] * (i + 1))
        flen = m_rows
    # Case for when all numbers in one row
    incr = m_rows
    # Split into i+1 rows:
    for i in range(1, min(m_rows, left)):
        # Pick as default result
        res = results[ind + i + 1][i]
        # If result never occured
        if res == 0:
            # Calcualte recursion
            res = req(ind + i + 1, i + 1, left - i - 1, m, sep_i)
            # Record the result
            results[ind + i + 1][i] = res
        # Calculate increment
        incr += (fact_table[m_rows] // fact_table[m_rows - i - 1]) * res
        incr %= ((10 ** 9) + 7)
    return incr


n = int(input().strip())
m = list(map(int, input().strip().split(' ')))
# Separation list constains indexies when sorting order distrubed
sep_lst = []
for i in range(1, n):
    if m[i - 1] > m[i]:
        sep_lst.append(i - 1)
sep_lst.append(n - 1)
sm = 1

# Factorial table and it's length
fact_table = [1]
flen = 0

# Results table (to not calculate already done cases)
results = [[0 for _ in range(n)] for _ in range(n)]

# Starting recursion
for i in range(1, sep_lst[0] + 1):
    sm += req(i, i + 1, sep_lst[0] - i, m, 0)
    sm %= ((10 ** 9) + 7)

# Print result
print(sm)