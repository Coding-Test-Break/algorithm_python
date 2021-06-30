answer = 0
def solution(nums):
    nums.sort()
    prime_combination(nums, 0, 0, )
    return answer

def is_prime(number):
    if number % 2 == 0:
        return False
    else: 
        for i in range(3, number, 2):
            if number % i == 0:
                return False
    return True

def prime_combination(X, Y, count):
    global answer
    if count < 3:
        for i in range(len(X)):
            prime_combination(X[i + 1:], Y + X[i], count + 1)
    elif is_prime(Y):
        answer += 1