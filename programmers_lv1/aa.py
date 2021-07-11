def solution(num):
    temp = num % 10 
    compare = num // 10 + num % 10
    count = 1
    while num != compare:
        if compare // 10 != 0:
            temp = compare % 10
            compare = compare // 10 + compare % 10
        else: 
            compare = temp * 10 + compare
        count += 1
        print(count)

    while num != divider(compare, temp)[0]:
        count +=1 
        
    
    return count

def divider(num, temp):
    if num >= 10:
        return [num // 10 + num % 10, num % 10]
    else: return [num + temp * 10, num]
            

print(solution(26))