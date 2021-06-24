def solution(n):
    answer = 0
    power = 0
    ternary = list()
    
    while(True):
        if n >= 3**power: power += 1 
        # 나눗셈이나 진법 계산시 등호 생각해볼 것.
        else: break

    for i in reversed(range(power)):
        ternary.append(n // 3**i)
        n = n % 3**i

    for i in range(len(ternary)):
        answer += ternary[i] * (3**i)

    return answer