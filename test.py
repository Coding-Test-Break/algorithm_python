import sys
import heapq

N = int(sys.stdin.readline())

time = []
for _ in range(N):
  time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x: (x[1], x[0]))

on_class = [time[0][1]]
heapq.heapify(on_class)

print(time)
cnt = 1

for i in time[1:]:
    if on_class[0] <= i[0]:
        heapq.heappop(on_class)
    else: 
        cnt += 1
        heapq.heappush(on_class, i[1])
    
print(cnt)
# onclass -> 수업중일 때 넣고 
# onclass 돌면서 수업시간시작전 이면, 

# for i in time[1:]:
#     if end[-1][1] <= i[0]:
#         end.append(i)
#     else: 
#         cnt += 1
# print(end)
# print(cnt)