def solution(rows, columns, queries):
    mat = matrix(rows, columns)
    answer = []

    for query in queries:
        x, y, p, q = query
        
        inner_vertex = mat[x - 1][y - 1]
        outer_vertex = mat[p - 1][q - 1]
        minimum = min(inner_vertex, outer_vertex)

        for i, j in zip(range(x, p), reversed(range(x, p))):
            mat[i - 1][y - 1] = mat[i][y - 1]
            mat[j][q - 1] = mat[j - 1][q - 1]
            minimum = min(minimum, mat[i][y - 1], mat[j - 1][q - 1])
        
        for i, j in zip(range(y, q), reversed(range(y, q))):
            if i == q - 1:
                mat[p - 1][i - 1] = outer_vertex
                mat[x - 1][j] = inner_vertex
            else:
                mat[p - 1][i - 1] = mat[p - 1][i]
                mat[x - 1][j] = mat[x - 1][j - 1]
                minimum = min(minimum, mat[p - 1][i],mat[x - 1][j - 1])
        
        answer.append(minimum)
    
    return answer
                


def matrix(rows, columns):
    mat = [[i + j * columns for i in range(1, columns + 1)] for j in range(rows)]
    return mat