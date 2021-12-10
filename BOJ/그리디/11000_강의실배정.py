import sys
import heapq

N = int(sys.stdin.readline())
schedule = list(); on_class = list()

for _ in range(N):
    schedule.append(list(map(int, sys.stdin.readline().split())))

schedule.sort(key = lambda x :  x[0])
heapq.heappush(on_class, schedule.pop(0)[1])

for schedule_iter in schedule: 
    if on_class[0] <= schedule_iter[0]:
        heapq.heappop(on_class)
        heapq.heappush(on_class, schedule_iter[1])
    # for i in reversed(range(len(on_class))):
    #     if on_class[i] <= schedule_iter[0]:
    #         on_class[i] = schedule_iter[1]
            # break
    else:
        heapq.heappush(on_class, schedule_iter[1])
        
print(len(on_class))