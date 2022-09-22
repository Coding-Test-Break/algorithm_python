import heapq

def solution(n, times):
    pq = list()
    answer = 0
    for t in times:
        heapq.heappush(pq, (t, t))

    # O(n) - 1,000,000,000
    while n > 0:
        # O(logn) ... 
        v, i = heapq.heappop(pq)
        n -= 1
        answer = v
        heapq.heappush(pq, (v + i, i))
        
    return answer

# n 이 1,000,000,000 으로 O(n)안에 끝내야 했음.
# 병목 구간의 시간 복잡도는 O(mlogn) - m: 100,000 / n: 1,000,000,000  >> 시간초과