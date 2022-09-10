import copy

comb = list()
def solution(n, info):
    max_cnt = 0
    answer = [[-1]]
    recur([], info, n)

    # 2000  (모든 가능한 조합을 돌면서 )
    for c in comb:
        cnt = 0 
        cur_cnt = 0
        # 11 (각 shot에 대해 점수 계산)
        for i, v in enumerate(c):
            if v > 0:
                cnt += 10 - i
            elif v == 0 and info[i] > 0:
                cur_cnt += 10 - i
                
        if cnt - cur_cnt > max_cnt:
            max_cnt = cnt - cur_cnt
            answer = [c]
        elif cnt - cur_cnt == max_cnt:
            answer.append(c)
    
    # 적은 수 맞춘 것을 우선으로 두기 위함
    if answer[0] != [-1]:
        answer.sort(reverse = True, key = lambda x: (x[-1], x[-2], x[-3], x[-4], x[-5], x[-6], x[-7], x[-8], x[-9], x[-10]))
        
    return answer[0]

# 각 점수별로 라이언에게 이기는 경우, 지는 경우를 상정해서 최소 shot을 배정한 뒤, 남는 shot이 있을 경우 가장 끝에 추가해준다.
# 그냥 배열 크기 11로 할당하고 sum() == 11일 경우만 셌으면 더 깔끔했을텐데 하는 아쉬움이 있음
# 2^11 의 시간복잡도 -> 2000 정도
def recur(arr, info, n):
    global comb 
    if len(arr) == 11:
        n_sum = sum(arr)
        if n_sum <= n:
            arr[-1] += n - n_sum
            comb.append(arr)
        return 
    for i in [0, 1]:
        temp_arr = copy.copy(arr)
        if i == 1:
            temp_arr.append(info[len(temp_arr)] + 1)
        else:
            temp_arr.append(i)
        recur(temp_arr, info, n)
