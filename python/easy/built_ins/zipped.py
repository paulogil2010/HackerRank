"""
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
"""


if __name__ == '__main__':
    N, X = map(int, input().split())

    G = []
    for i in range(X):
        G.append(map(float, input().split()))

    # zip(*G) transpose the matrix
    for i in zip(*G):
        print("%.1f" % (sum(i) / len(i)))