"""
Read four numbers, a, b, c, and d, and print the result of a**b + c**d.
"""

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    d = int(input().strip())

    print(pow(a, b) + pow(c, d))