def solution(dartResult):
    count = 0
    digit_count = 0
    score = list([None] * 3)
    for i in dartResult:
        if i.isdigit():
            if digit_count == 0:
                score[count] = int(i)
                digit_count += 1
            else:
                score[count] = score[count] * 10 + int(i)
        elif i.isalpha():
            if i == "S":
                score[count] **= 1
            elif i == "D":
                score[count] **= 2
            elif i == "T":
                score[count] **= 3
            count += 1
            digit_count = 0
        else: 
            if i == "#":
                score[count - 1] *= -1
            elif i == "*":
                score[count - 1] *= 2
                if not(count == 1):
                    score[count - 2] *= 2
    return sum(score)