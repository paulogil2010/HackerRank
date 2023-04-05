"""
You are given two values  and .
Perform integer division and print .
"""


if __name__ == '__main__':
    T = int(input().strip())

    for i in range(T):
        a, b = map(str, input().split())

        try:
            print("%.0f" % (int(a) / int(b)))
        except ZeroDivisionError as errz:
            print("Error Code: integer division or modulo by zero")
        except ValueError as errv:
            print(f"Error Code: {errv}")