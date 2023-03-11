if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_values = list(set(arr))
    unique_values.sort()

    print(unique_values[-2:-1][0])