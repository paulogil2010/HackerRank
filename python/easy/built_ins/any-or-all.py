"""
You are given a space separated list of integers.
If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""


if __name__ == '__main__':
    N = int(input().strip())
    M = map(int, input().split())

    print(all([i for i in M if i > 0]) and any([] ) )
