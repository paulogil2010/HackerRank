if __name__ == '__main__':
    S = set(map(int, input().split()))

    n = int(input())

    is_superset = False
    for i in range(0, n):
        sub_set = set(map(int, input().split()))
        if sub_set.issubset(S):
            is_superset = True
        else:
            is_superset = False
            break

    print(is_superset)
