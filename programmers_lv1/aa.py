def solution(a, b):
    if a + b == 0:
        return 0
    else:
        if a*b < 0:
            return abs(a+b) * ((abs(a) + 1 + abs(b)) / 2) * ((a + b) / abs(a + b))
        if a*b > 0:
            return (abs(b-a) + 1) * (abs(a + b) / 2) * ((a + b) / abs(a + b))
        if a*b == 0:
            return abs(a + b) * ((abs(a + b) + 1) / 2) * ((a + b) / abs(a + b))

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2
