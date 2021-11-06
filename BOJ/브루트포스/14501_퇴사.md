import sys

N = int(sys.stdin.readline().strip())
schedule = [0]
schedule_queue = []

dp = [0 for _ in range(N + 1)]
for _ in range(N):
    schedule.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    dp[i] = dp[i - 1]
    days_left, pay = schedule[i]
    schedule_queue.append([pay + dp[i - 1], days_left])
    idx = 0
    while idx < len(schedule_queue):
        schedule_queue[idx][1] -= 1
        if schedule_queue[idx][1] == 0:
            dp[i] = max(dp[i], schedule_queue[idx][0])
            schedule_queue.pop(idx)
            idx -= 1
        idx += 1
        
print(dp[-1])