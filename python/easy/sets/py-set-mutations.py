"""
You are given a set A and N number of other sets.
These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.
"""

if __name__ == '__main__':
    n = int(input().strip())
    A = set(map(int, input().split()))
    nA = int(input().strip())

    for i in range(0, nA):
        action = input().split()
        action_set = set(map(int, input().split()))

        if action[0] == 'intersection_update':
            A.intersection_update(action_set)

        if action[0] == 'update':
            A.update(action_set)

        if action[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(action_set)

        if action[0] == 'difference_update':
            A.difference_update(action_set)

    print(sum(A))


