if __name__ == '__main__':
    N = int(input())

    arr = []
    for i in range(N):
        inputed = input().split()
        if inputed[0] == 'print':
            print(arr)
        elif inputed[0] == 'insert':
            arr.insert(int(inputed[1]), int(inputed[2]))
        elif inputed[0] == 'remove':
            arr.remove(int(inputed[1]))
        elif inputed[0] == 'append':
            arr.append(int(inputed[1]))
        elif inputed[0] == 'sort':
            arr.sort()
        elif inputed[0] == 'pop':
            arr.pop()
        elif inputed[0] == 'reverse':
            arr.reverse()
