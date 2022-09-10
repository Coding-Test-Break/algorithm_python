def solution(n, k):
    answer = 0
    arr = recur(n, k).split("0")
    
    # 2진법일 경우 2^20까지 -> 20자리 수 -> 최대 10개
    # 10 * 1,000,000 이니까 sqrt 안해도 안전하지 않나 .. 
    for a in arr:
        if a and is_prime(int(a)):
            answer += 1
        
    return answer


# log_kn
def recur(n, k):
    몫, 나머지 = divmod(n, k)
    if 몫 == 0:
        return str(나머지) 
    return recur(몫, k) + str(나머지)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
          return False
    return True