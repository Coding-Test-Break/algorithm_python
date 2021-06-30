def solution(d, budget):
    d = sorted(d)
    answer = 0; sum = 0
    for i in d: 
        if (sum + i) <= budget:
            sum += i
            answer += 1
        else: break
    return answer