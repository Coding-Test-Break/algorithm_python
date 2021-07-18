import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while (scoville[0] < K):
        if len(scoville) == 1:return -1
        scoville.append(heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        count += 1
    return count

