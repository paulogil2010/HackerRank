"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
"""


from collections import OrderedDict


if __name__ == "__main__":
    N = int(input().strip())

    d = OrderedDict()
    for i in range(N):
        item = input().split()
        K = ' '.join(item[:-1])
        V = int(item[-1])
        if K not in d.keys():
            d[K] = V
        else:
            d[K] += V

    for k,v in d.items():
        print(k, v)
