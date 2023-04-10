"""
You are given a string N.
Your task is to verify that N is a floating point number.
"""

import re


regex = '^[+-]?\d*\.\d+$'


def check_is_float(floatnum):
    if (re.match(regex, floatnum)):
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input().strip())
    vals = []
    for i in range(n):
        print(check_is_float(input()))
