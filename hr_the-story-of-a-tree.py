#!/bin/python3

import sys

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    # Create list for tree of size N
    tree = [[] for _ in range (n)]
    # Record each connection to the tree in a manner: append to the list[u - 1] element v - 1 and vice versa
    for _ in range(n-1):
        u,v = input().strip().split(' ')
        u,v = [int(u) - 1,int(v) - 1]
        tree[u].append(v)
        tree[v].append(u)
    g,k = input().strip().split(' ')
    g,k = [int(g),int(k)]
    # Record guess list in a manner: append to the list[u - 1] (parent) element v - 1 (child)
    g_lst = [[] for _ in range (n)]
    for _ in range(g):
        u,v = input().strip().split(' ')
        u,v = [int(u) - 1,int(v) - 1]
        g_lst[u].append(v)
    # Set initial guess score to zero
    score = 0
    # Set relative (to the root of u = 1) scores for each node to zero
    rel_score = [0 for _ in range(n)]
    # Set queue to the the first element (root: u = 1)
    q_lst = [0]
    #print(*tree)
    # Commence BFS
    for i in range(n):
        # Set current node
        cr_nd = q_lst[i]
        #print(cr_nd, tree[cr_nd])
        # For each child of current node
        for child in tree[cr_nd]:
            # Remove parent element from child lists (as it was created as mutual connections)
            tree[child].remove(cr_nd)
            rel_score[child] = rel_score[cr_nd]
            # If child in the guess list of parrent
            if child in g_lst[cr_nd]:
                # Increase guess score
                score += 1
                # Decrease relative score for the child (that guess would be wrong for that child as root)
                rel_score[child] -= 1
            # If parent in the guess list of chld 
            if cr_nd in g_lst[child]:
                # Increase relative score for the child (that guess would be right for that child as root)
                rel_score[child] += 1
            # Append child to queue
            q_lst.append(child)
    #print(*rel_score)
    # Number of wins init to zero
    p = 0
    # Traverse the list of relative score and increase number of wins if rel + score greater than k
    for el in rel_score:
        if el + score >= k:
            p += 1        
    # Get reduced fraction of p / n where p number of wins and n - number of nodes
    # Case for zero wins
    if p == 0:
        n = 1
    # Another common case
    elif n % p == 0:
        n = n // p
        p = 1
    else:
        # Reduce p and n if both devisible by i
        dev = gcd(n, p)
        p = p // dev
        n = n // dev
    print('%d/%d' % (p, n))