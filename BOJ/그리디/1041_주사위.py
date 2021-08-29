import sys

# n = int(sys.stdin.readline())
# array = list(map(int,sys.stdin.readline().strip().split()))

n = 3
array = [1, 2, 4, 5, 6, 3]

def dice(n, array):
    array = sorted(reversed(array))
    print(array)
    answer = 0
    if n  == 1:
        return sum(array[:5])
    answer += 4 * sum(array[:3])
    answer += (8*n - 12) * sum(array[:2])
    answer += ((n-2)**2 + 4 * (n-1) * (n-2)) * array[0] 
    return answer

print(dice(n, array))