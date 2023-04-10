"""
You are given a space separated list of integers.
If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""


if __name__ == '__main__':
    N = int(input().strip())
    M = list(map(int, input().split()))

    print(all([i > 0 for i in M]) and any([str(i)[::-1] == str(i) for i in M]))
