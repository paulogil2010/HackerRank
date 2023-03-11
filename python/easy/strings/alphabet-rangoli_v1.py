import string

def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)
    left_side = alphabet[1:size]
    left_side.reverse()
    right_side = alphabet[1:size]
    central_line = left_side + ['a'] + right_side
    for i in range(1,size):
        center_letter = list(alphabet[size-i])
        spaces = len(central_line) - (len(center_letter))
        if i == 1:
            print(f'{"-" * spaces}{("-").join(center_letter)}{"-" * spaces}')
            continue
        aux = i - 1
        top_left = list(alphabet[size-aux:size])
        top_right = top_left.copy()
        top_left.reverse()
        line = list(top_left) + center_letter + list(top_right)
        spaces = len(central_line) - (len(line))
        print(f'{"-" * spaces}{("-").join(line)}{"-" * spaces}')
    print(('-'.join(central_line)))
    for i in range(size-1,0,-1):
        center_letter = list(alphabet[size-i])
        spaces = len(central_line) - (len(center_letter))
        if i == 1:
            print(f'{"-" * spaces}{("-").join(center_letter)}{"-" * spaces}')
            continue
        aux = i - 1
        top_left = list(alphabet[size-aux:size])
        top_right = top_left.copy()
        top_left.reverse()
        line = list(top_left) + center_letter + list(top_right)
        spaces = len(central_line) - (len(line))
        print(f'{"-" * spaces}{("-").join(line)}{"-" * spaces}')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)