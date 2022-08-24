def solution(s):
    open = 0; close = 0
    
    for i in range(len(s)):
        if s[i] == "(":
            open += 1
        elif s[i] ==")":
            if open > 0:
                open -= 1
                continue
            close += 1 
    
    if open == 0 and close == 0:
        return True
    else:
        return False


# 시간복잡도 O(n) -> 100,000 번 연산