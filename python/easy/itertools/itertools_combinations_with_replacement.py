
from itertools import combinations_with_replacement


if __name__ == '__main__':
    S, K = input().split()

    S = ''.join(sorted(S))

    R = list(combinations_with_replacement(S, int(K)))
    for j in R:
        print(''.join(j))