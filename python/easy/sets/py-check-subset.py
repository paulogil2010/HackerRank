
if __name__ == '__main__':
    T = int(input())

    for i in range(0, T):
        input()
        A = set(map(int, input().split()))
        input()
        B = set(map(int, input().split()))

        print(A.issubset(B))