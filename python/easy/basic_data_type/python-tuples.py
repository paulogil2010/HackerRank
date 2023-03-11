"""
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.
"""

# Python 3 has a different result -> changed to pipy3

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    print(hash(t))

