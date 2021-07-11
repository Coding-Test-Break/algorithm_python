# def solution(s, n):
#     for i, j in enumerate(s):
#         if s[i].isupper():
#             s[i] = chr((ord(j) - 65 + n) % 26 + 65)
#         elif s[i].islower():
#             s[i] = chr((ord(j) - 97 + n) % 26 + 97)
#     return s
def solution(s, n):
    answer = ""
    for i in s:
        if i.isupper():
            answer += chr((ord(i) - 65 + n) % 26 + 65)
        elif i.islower():
            answer += chr((ord(i) - 97 + n) % 26 + 97)
        elif i == " ": answer += " "
        
    return answer


print(solution("a B z", ))


