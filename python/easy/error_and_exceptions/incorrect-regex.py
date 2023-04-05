import re


if __name__ == "__main__":
    T = int(input().strip())

    for i in range(T):
        C = input()
        try:
            re.compile(C)
            print(True)
        except re.error:
            print(False)