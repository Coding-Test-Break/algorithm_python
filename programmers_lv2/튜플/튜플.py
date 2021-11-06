def solution(s):
    s_list = s.lstrip("{").rstrip("}").split("},{")
    s_list = [iter.split(",") for iter in s_list]
    s_list = sorted(s_list, key= lambda x : len(x))

    answer = list(); temp = list()

    for iter in s_list: 
        for i in iter:
            if i not in temp:
                answer.append(int(i))
        temp = iter
        
    return answer