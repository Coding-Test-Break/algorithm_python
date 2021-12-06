from collections import deque

def solution(cacheSize, cities):
    cache = deque(); cities = deque(cities); answer = 0
    
    if cacheSize == 0: return len(cities) * 5

    while cities:
        temp = cities.popleft().lower()
        for i, v in enumerate(cache):
            if v == temp:
                del cache[i]
                cache.append(temp)
                answer += 1
                break
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(temp)
            answer += 5

    return answer

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))