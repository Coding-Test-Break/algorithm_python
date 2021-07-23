def solution(n):
    oneTwoFourDict = {1: "1", 2: "2", 0: "4"}
    answer = ""
    while n != 0:
        answer = oneTwoFourDict[n % 3] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else: n = n // 3
    
    return answer

