if __name__ == '__main__':

    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    scores.sort(key = lambda x: x[1])
    unique_scores = list(set(x[1] for x in scores))
    unique_scores.sort()
    second_students = [x[0] for x in scores if x[1] == unique_scores[1]]

    second_students.sort()
    for i in second_students:
        print(i)
