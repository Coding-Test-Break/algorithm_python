from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = 0
    max_cnt = 3 * max(len(queue1), len(queue2))
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    # n < 300_000 이므로 O(nlog(n)) 안에는 해결해야 했음.
    # O(n) 으로 패슨데 솔직히 이 아이디어가 통과할 줄은 몰랐다 
    while True:
        if sum1 == sum2:
            break
        elif sum1 > sum2:
            res = q1.popleft()
            q2.append(res)
            sum1 -= res
            sum2 += res
        elif sum1 < sum2:
            res = q2.popleft()
            q1.append(res)
            sum1 += res
            sum2 -= res
            
        answer += 1
        if answer > max_cnt:
            answer = -1
            break
    
    return answer