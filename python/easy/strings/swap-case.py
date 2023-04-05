"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):

    word = ''
    for letter in s:
        if letter.isupper():
            word += letter.lower()
        elif letter.islower():
            word += letter.upper()
        else:
            word += letter
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)