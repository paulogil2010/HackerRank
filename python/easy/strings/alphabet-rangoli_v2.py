import string
import sys

def print_rangoli(size):
    if size <= 1:
        print(string.ascii_lowercase[0])
        sys.exit(0)
    letters = list(string.ascii_lowercase)[:size]
    letters_reverse = list(string.ascii_lowercase)[:size]
    letters_reverse.reverse()
    center_line = '-'.join(['-'.join(letters_reverse[:-1]), '-'.join(letters)])
    total_size = len(center_line)
    c = '-'
    for i in range(size):
        if i == size-1:
            break
        left = ''
        right = ''
        if i != 0:
            left = '-'.join(letters_reverse[:i])
            right = '-'.join(letters[size-i:])
        center = letters_reverse[i]
        all_letters = '-'.join([left, center, right])
        left_size = (total_size // 2) - len(left) - 1
        right_size = (total_size // 2) - len(right) - 1
        print((c*(left_size)).rjust(left_size)+all_letters+(c*(right_size)).rjust(right_size))
    print(center_line)
    for i in range(size-1, 0, -1):
        left = ''
        right = ''
        if i != size:
            left = '-'.join(letters_reverse[:i-1])
            right = '-'.join(letters[size-(i-1):])
        center = letters[size-i]
        all_letters = '-'.join([left, center, right])
        left_size = (total_size // 2) - len(left) - 1
        right_size = (total_size // 2) - len(right) - 1
        print((c*(left_size)).rjust(left_size)+all_letters+(c*(right_size)).rjust(right_size))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
