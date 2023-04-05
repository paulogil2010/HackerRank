"""
Rupal has a huge collection of country stamps.
She decided to count the total number of distinct country stamps in her collection.
She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.
"""

if __name__ == '__main__':
    n = int(input())

    stamps = set()
    for i in range(0, n):
        stamps.add(input().strip())

    print(len(stamps))