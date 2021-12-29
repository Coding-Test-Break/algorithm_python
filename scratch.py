import sys

N = int(sys.stdin.readline())
schedule = list()

for _ in range(N):
  s_t, e_t = map(int, sys.stdin.readline().split())
  schedule.append([s_t, e_t])

schedule.sort(key= lambda x: (x[1], x[0]))
end_time = 0
count = 0
for s in schedule:
  if end_time <= s[0]:
    count += 1
    end_time = s[1]

print(count)