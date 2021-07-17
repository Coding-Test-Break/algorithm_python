def solution(x):
    harshad = 0
    for i in str(x):
        harshad += int(i)
    if x % harshad == 0:
        return True
    else: return False