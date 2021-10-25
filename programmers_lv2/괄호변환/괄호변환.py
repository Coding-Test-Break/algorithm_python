def solution(p):
    answer = recur(p)
    return answer

def seperator(original):
    count = 0; index = 0; is_correct = True
    for char in original:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        index += 1
        if count < 0:
            is_correct = False
        if count == 0:
            break

    return original[:index], original[index:], is_correct

def reverser(target):
    result = ""
    for char in target:
        if char == "(":
            result += ")"
        elif char == ")":
            result += "("
    return result 

def recur(original):
    if not original:
        return ""
    u, v, is_correct = seperator(original)
    if not is_correct:
        return "(" + recur(v) + ")" + reverser(u[1:-1])
    else:
        return u + recur(v)
