# 재귀를 이용한 풀이
def solution_recursive(s):
    if len(s) == 0: 
        return 1
    for i in range(len(s) - 1):
        return solution_recursive(s.replace(s[i] + s[i], ""))
    else: return 0
  
# stack을 이용한 풀이 
def solution_with_stack(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
            continue
        elif stack[-1] == i:
            stack.pop()
        else :
            stack.append(i)

    if stack: return 0
    else : return 1