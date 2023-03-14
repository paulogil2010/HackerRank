"""
In this challenge, you will be given 2 integers, N and M.
There are n words, which might repeat, in word group A.
There are M words belonging to word group B. For each M words,
check whether the word has appeared in group A or not.
Print the indices of each occurrence of M in group A.
If it does not appear, print -1.
"""


from collections import defaultdict


if __name__ == '__main__':
    N, M = map(int, input().split())

    d = defaultdict(list)
    for i in range(0, N):
        d['A'].append(input().strip())

    for i in range(0, M):
        d['B'].append(input().strip())

    for i in d['B']:
        idx = []
        for j, v in enumerate(d['A']):
            if v == i:
                idx.append(j+1)
        if not idx:
            idx.append(-1)
        print(*idx)