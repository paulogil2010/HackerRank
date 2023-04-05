"""
You are asked to ensure that the first and last names of people
begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
"""

import os
import re


# Complete the solve function below.
def solve(s):
    res_regex = re.split(r'(\s+)', s)
    res = []
    for i in res_regex:
        res.append(i.capitalize())
    return ''.join(res)

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', '/tmp/file.txt'), 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
