def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, counter(i, s))
    return answer

def counter(i, s):
    p = 0; q = 0; length = 0; count = 1
    while(p < len(s)):
        if s[q : q + i] == s[p + i : p + 2 * i]:
            count += 1
            p  += i
        else: 
            if count > 1:
                length += len(str(count)) + i
                count = 1
                p += i
                q = p
            else: 
                length += min(i, len(s[q: q + i]))
                p += i
                q += i
                
    return length