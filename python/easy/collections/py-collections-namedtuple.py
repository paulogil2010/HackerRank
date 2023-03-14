"""
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.

average = sum(marks) / total students
"""

from collections import namedtuple


if __name__ == '__main__':
    N = int(input().strip())
    columns = list(input().split())
    table = namedtuple('grades', columns)

    rows = []
    for i in range(N):
        inputed_rows = input().split()
        rows.append(table(*inputed_rows))

    total_marks = [int(i.MARKS) for i in rows]
    avg = sum(total_marks) / N

    print("{:.2f}".format(avg))

