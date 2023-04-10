"""
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
"""


def count_substring(string, sub_string):
    counter = 0
    list_string = list(string)
    for index, _ in enumerate(list_string):
        if (index + len(sub_string)) <= len(string):
            if ''.join(list_string[index:(index + len(sub_string))]) == sub_string:
                counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)