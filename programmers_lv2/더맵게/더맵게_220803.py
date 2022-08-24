import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        h1 = heapq.heappop(scoville)
        h2 = heapq.heappop(scoville)
        heapq.heappush(scoville, h1 + (h2 * 2))
        answer += 1 
        if scoville[0] >= K:
            break
    else:
        answer = -1
    return answer