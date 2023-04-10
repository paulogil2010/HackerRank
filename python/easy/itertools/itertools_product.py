"""
You are given a two lists A and B. Your task is to compute their cartesian product AxB.
"""

from itertools import product


if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(*list(product(*[A, B])))