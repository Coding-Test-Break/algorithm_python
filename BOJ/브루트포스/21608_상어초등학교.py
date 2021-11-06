import sys

N = int(sys.stdin.readline())
info_dict = dict()
seat = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N ** 2):
    idx, *favorite = list(map(int, sys.stdin.readline().split()))
    info_dict[idx] = favorite

def counter(i, j, who, N):
    # 동 남 서 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    like_count = 0
    empty_count = 0
    for p in range(4):
        temp_i, temp_j = i, j
        temp_i += dx[p]
        temp_j += dy[p]
        if temp_i < 0 or temp_j < 0 or temp_i >= N or temp_j >= N:
            pass
        else:
            if seat[temp_i][temp_j] in info_dict[who]:
                like_count += 1
            if seat[temp_i][temp_j] == 0:
                empty_count += 1
    
    return like_count, empty_count


for key in info_dict.keys():
    print(key)
    like_dict = dict()
    empty_dict = dict()
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                like_count, empty_count = counter(i, j, key, N)
                try: 
                    like_dict[like_count].append((i, j))
                except:
                    like_dict[like_count] = [(i, j)]
                try: empty_dict[empty_count].append((i, j))
                except: empty_dict[empty_count] = [(i, j)]

    max_like_key = sorted(like_dict, reverse= True)[0]
    max_empty_key = sorted(empty_dict, reverse= True)[0]

    if len(like_dict[max_like_key]) == 1:
        i, j = like_dict[max_like_key].pop()
        seat[i][j] = key
        continue
    if len(empty_dict[max_empty_key]) == 1:
        i, j = empty_dict[max_empty_key].pop()
        seat[i][j] = key
        continue
    filtered_list = list(set(like_dict[max_like_key]) & set(empty_dict[max_empty_key]))
    min_row = 999
    min_column = 999
    for iter in filtered_list:
        min_row = min(min_row, iter[0])
        min_column = min(min_column, iter[1])

    filtered_list2 = []
    for iter in filtered_list:
        if iter[0] == min_row:
            filtered_list2.append(iter)

    if len(filtered_list2) == 1:
        i, j = filtered_list2[0]
        seat[i][j] = key
        continue
    for iter in filtered_list2:
        if iter[1] == min_column:
            i, j = iter        
            seat[i][j] = key

print(seat)