
if __name__ == '__main__':
    size_a = int(input())
    set_a =  set(list(map(int, input().split())))
    size_b =  int(input())
    set_b =  set(list(map(int, input().split())))

    diff = set()
    [diff.add(i) for i in set_a.difference(set_b)]
    [diff.add(i) for i in set_b.difference(set_a)]

    for i in sorted(diff):
        print(i)
