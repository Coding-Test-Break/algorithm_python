from collections import deque

def solution(priorities, location):
    target = priorities[location]
    priorities = deque(priorities)
    numed = deque()
    for i, v in enumerate(priorities):
        numed.append((v, i))
    stack = list()
    
    while numed:
        p, i = numed.popleft()
        for k, j in numed:
            if k > p:
                numed.append((p, i))
                break
        else:
            stack.append((p, i))
    
    for i, (v, idx) in enumerate(stack):
        if idx == location:
            return i + 1
  
# priorities의 길이가 1 ~ 100 까지 밖에 안돼서 무지성으로 풀었다.
# O(n^2)