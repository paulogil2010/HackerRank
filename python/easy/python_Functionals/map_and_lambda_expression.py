"""calculates cube value for each fibonacci in a range of numbers"""


cube = lambda x: x**3


def fibonacci(n):
    fibo = []
    for val in range(n):
        if not val or val == 1:
            fibo.append(val)
        else:
            fibo.append(fibo[-2] + fibo[-1])
    return fibo


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
