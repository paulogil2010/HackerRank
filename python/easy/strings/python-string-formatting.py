"""
Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
"""

def print_formatted(number):
    l = len(bin(number)[2:])
    for i in range(1, number+1):
        d = i
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        print(
            str(d).rjust(l),
            str(o).rjust(l),
            str(h).rjust(l),
            str(b).rjust(l)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)