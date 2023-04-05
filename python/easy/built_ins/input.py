"""
You are given a polynomial P of a single indeterminate (or variable), X.
You are also given the values of X and K. Your task is to verify if P(x) == K.
"""


if __name__ == '__main__':

    x, k = map(int, input().split())
    print(eval(input()) == k)
