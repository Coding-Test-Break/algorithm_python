def solution(N, stages):
    failure = dict()
    len_stage = len(stages)
    answer = []
    for i in range(1, N + 1):
        if len_stage == 0: 
            failure[i] = 0
        else:
            failure[i] = stages.count(i) / len_stage
        len_stage -= stages.count(i)
        
    answer = sorted(failure, reverse=True, key=lambda x: failure[x])
    return answer