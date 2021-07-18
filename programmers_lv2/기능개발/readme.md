``` python
def solution(progresses, speeds):
    daysRemaining = list(); answer = list()
    for i, j in zip(progresses, speeds):
        if (100 - i) % j == 0:
            daysRemaining.append((100 - i) // j)
        else: daysRemaining.append((100 - i) // j + 1)
    temp = -1
    index = -1
    for i in daysRemaining:
        if i > temp:
            answer.append(1)
            temp = i
            index += 1
        else: answer[index] += 1 
    return answer
```