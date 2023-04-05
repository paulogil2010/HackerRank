"""
You are given a complex x. Your task is to convert it to polar coordinates.
"""

import cmath

if __name__ == '__main__':
    c = input()
    z = complex(c)

    print(abs(z))
    print(cmath.phase(z))
