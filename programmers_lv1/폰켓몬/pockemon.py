def solution(nums):
    array_len = len(nums)
    answer = 0
    pockemon = list()


    for i, new_pockmon in enumerate(nums):
        left_turns = array_len - i

        if left_turns <= (array_len / 2 - len(pockemon)):
            if new_pockmon not in pockemon:
                answer += 1
            pockemon.append(new_pockmon)
            

        else:
            if new_pockmon not in pockemon:
                pockemon.append(new_pockmon)
                answer += 1

    return answer


nums = [3,3,3,2,2,2, 4, 5, 2, 2, 2, 7, 8, 9, 2, 2]

a = 4 // 2

for i in range(a):
    print(i)