``` python 
import heapq
def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while (scoville[0] < K):
        if len(scoville) == 1:return -1
        scoville.append(heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        count += 1
    return count
```

- `heapq` 모듈에 대해서 좀 더 공부할 것
- 먼저 `heapify`를 실행 한 후, `heappush`, `heappop`을 실행하자
- 그래야지 list의 순서가 유지됨