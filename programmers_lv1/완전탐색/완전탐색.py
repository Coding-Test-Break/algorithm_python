def solution(answers):
    answer = []

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 1, 2, 4, 5]
    count_ans = list(0 for i in range(3))

    for i, ans in enumerate(answers):
        if student1[i % 5] == ans: count_ans[0] += 1
        if student2[i % 8] == ans: count_ans[1] += 1
        if student3[(i // 2) % 5] == ans: count_ans[2] += 1   

    max_num = max(count_ans)
    for i in range(count_ans.count(max_num)):
        answer.append(count_ans.index(max_num) + 1 + i)
        count_ans.remove(max_num)

    return answer

