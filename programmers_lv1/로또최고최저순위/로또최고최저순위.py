def solution(lottos, win_nums):
    num_zero = 0
    correct = len(set(lottos) & set(win_nums))
    for i in range(len(lottos)):
        try:
            num_zero += 1   
            lottos.remove(0)
        except ValueError:
            num_zero -= 1
            break
    
    return [lottery_rank(correct + num_zero), lottery_rank(correct)]

def lottery_rank(a):
    return 1 if a == 6 else 2 if a == 5 else 3 if a == 4 else 4 if a == 3 else 5 if a == 2 else 6
