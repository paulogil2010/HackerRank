

if __name__ == '__main__':
    N, M = map(int, input().split())
    if N*3 != M:
        exit(0)

    middle = '.|.'
    item_middle = middle
    message = 'WELCOME'
    c = '-'

    for i in range(1, ((N//2) + 1)):
        if i != 1:
            item_middle = item_middle + (middle * 2)
        len_middle = len(item_middle)
        print(((int((M-len_middle) / 2) * c).ljust(int((M-len_middle) / 2))+item_middle+(int(((M-len_middle) / 2)) * c).rjust(int((M-len_middle) / 2))))

    print((int((M-7) / 2) * c).ljust(int((M-7) / 2))+message+(int(((M-7) / 2)) * c).rjust(int((M-7) / 2)))

    for i in range(1, ((N//2) + 1)):
        if i != 1:
            item_middle = item_middle.replace(middle, '', 2)
        len_middle = len(item_middle)
        print(((int((M-len_middle) / 2) * c).ljust(int((M-len_middle) / 2))+item_middle+(int(((M-len_middle) / 2)) * c).rjust(int((M-len_middle) / 2))))
