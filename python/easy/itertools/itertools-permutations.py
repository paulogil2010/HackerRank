"""
You are given a string S.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order.
"""

from itertools import permutations


if __name__ == '__main__':
    S, K = input().split()

    R = list(permutations(S, int(K)))
    R.sort()

    for i in R:
        print(''.join(i))