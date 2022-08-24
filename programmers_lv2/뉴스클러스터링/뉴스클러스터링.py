from collections import deque

def solution(str1, str2):
    answer = 0
    g = 0
    h = 0
    str1 = str1.lower()
    str2 = str2.lower()
    set_a = deque([])
    set_b = deque([])
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            set_a.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            set_b.append(str2[i: i + 2])
    set_a = deque(sorted(set_a))
    set_b = deque(sorted(set_b))
    
    while set_a and set_b:
        if set_a[0] == set_b[0]:
            set_a.popleft()
            set_b.popleft()
            g += 1
            h += 1
        elif set_a[0] < set_b[0]:
            set_a.popleft()
            h += 1
        elif set_a[0] > set_b[0]:
            set_b.popleft()
            h += 1
    h += (len(set_a) + len(set_b))
    
    if h == 0:
        return 65536
    return divmod((g / h) * 65536, 1)[0]

# sort O(nlog(n)), O(n) -> 1,000
# 1,000 이니 O(n^3) 미만이면 풀 수 있었다. 교/합집합을 python 모듈 써서 구했어도 충분히 통과했을듯