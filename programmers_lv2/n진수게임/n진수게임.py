jin = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def solution(n, t, m, p):
    answer = ''
    nums = ""
    
    # 1,000 * 1,000 (상한을 얼마로 둬야 할지 몰라서 시간 복잡도 안터지는 선에서 큰 수를 줌.)
    for i in range(t * 1000):
        nums += njin(n, i)

    cur = 0
    while cur < len(nums) and len(answer) < t:
        if (cur % m) + 1 == p:    
            answer += nums[cur]
        cur += 1 
        
    return answer

def njin(n, k):
    몫, 나머지 = divmod(k, n) 
    if 몫 == 0:
        return jin[나머지]
    return njin(n, 몫) + jin[나머지]

# n진법으로 바꾸고 돌리기만 하면 되는 쉬운 문제