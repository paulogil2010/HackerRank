"""
RAGHU is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay Xi
amount of money only if they get the shoe of their desired size.

Your task is to compute how much money RAGHU earned.
"""

from collections import Counter


if __name__ == '__main__':
    X = int(input().strip())
    sizes = list(map(int, input().split()))
    customers = int(input().strip())

    desired = []
    for i in range(0, customers):
        desired.append(list(map(int, input().split())))

    num_of_shoes_by_size = Counter(sizes)
    amount_money = 0
    for i in desired:
        if num_of_shoes_by_size[i[0]]:
            amount_money += i[1]
            num_of_shoes_by_size[i[0]] -= 1
    print(amount_money)