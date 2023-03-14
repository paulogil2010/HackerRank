"""
You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.
"""

from itertools import combinations


if __name__ == '__main__':
    S, K = input().split()

    S = ''.join(sorted(S))
    for i in range(1, int(K) +1):
        R = list(combinations(S, int(i)))
        for j in R:
            print(''.join(j))