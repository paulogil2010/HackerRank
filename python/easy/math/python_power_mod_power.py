"""
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
"""

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    m = int(input().strip())

    print(a**b)
    print(pow(a,b,m))