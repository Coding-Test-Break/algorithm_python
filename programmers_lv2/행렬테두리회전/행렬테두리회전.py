from typing import Collection


def solution(rows, columns, queries):
    mat = matrix(rows, columns)

    for query in queries:
        temp1, temp2 = mat[query[0] - 1][query[1] - 1], mat[query[2] - 1][query[3] - 1]
        print(temp1, temp2)
    return mat


def matrix(rows, columns):
    mat = [[i + j * 6 for i in range(1, columns + 1)] for j in range(rows)]
    return mat


x = 6
y = 6
q = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(x, y, q)