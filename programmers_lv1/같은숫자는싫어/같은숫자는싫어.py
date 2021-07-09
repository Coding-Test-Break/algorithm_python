def solution(a):
    answer = a[:1]
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            answer.append(a[i + 1])
    return answer