if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    c = int(input())

    a = []
    for i in range(0, c):
        a.append(input().split())

    for i in a:
        if i[0] == 'pop':
            s.pop()
        elif i[0] == 'remove':
            s.discard(int(i[int(1)]))
        elif i[0] == 'discard':
            s.discard(int(i[int(1)]))
    print(sum(s))