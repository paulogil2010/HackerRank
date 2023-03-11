"""
The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed
to the English newspaper. The third line contains the number of students who have subscribed
to the French newspaper. The fourth line contains the space separated list of student roll
numbers who have subscribed to the French newspaper.
"""


if __name__ == '__main__':
    ne = int(input().strip())
    e = set(map(int, input().split()))
    nf = int(input().strip())
    f = set(map(int, input().split()))

    res = e.symmetric_difference(f)

    print(len(res))