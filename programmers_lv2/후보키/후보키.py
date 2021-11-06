from itertools import combinations

def solution(relation):
    col_len = len(relation[0])
    combination_list = []
    answer = 0
    for i in range(1, col_len + 1):
        combination_list += list(combinations([j for j in range(col_len)], i))

    while combination_list:
        com = combination_list.pop(0)
        temp_list = list()
        for r in relation:
            temp = list()
            for c in com:
                temp.append(r[c])
            temp_list.append(temp)
        # print(temp_list, "\n-----------")
        for i in range(len(temp_list)):
            break_count = 0
            for j in range(i + 1, len(temp_list)):
                if temp_list[i] == temp_list[j]:
                    print(temp_list[i], temp_list[j])
                    break_count += 1
                    break
                if break_count > 0:
                    break
            if break_count > 0:
                break
                
        else: 
            answer += 1 
            print(com)
            idx = 0
            while idx < len(combination_list):
                count = 0
                for c in com:
                    if c in combination_list[idx]:
                        count += 1
                    if count == len(com):
                        combination_list.pop(idx)
                        idx -= 1
                idx += 1
    return answer


relation = [["a","aa"],["aa","a"],["a","a"]]
for i in relation:
    print(i)
print(solution(relation))
