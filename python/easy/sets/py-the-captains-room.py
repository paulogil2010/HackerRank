from collections import Counter

if __name__ == '__main__':
    K = int(input().strip())
    RN = list(map(int, input().split()))


    print(Counter(RN).most_common()[-1][0])
