import sys

num_dict = dict()
for i in range(36):
    if i < 10: num_dict[str(i)] = i
    else: num_dict[chr(i + 55)] = i

def to_decimal(N, B):
    result = 0
    for idx, num in enumerate(N):
        result += num_dict[num] * (B ** (len(N) - 1 - idx))
    return result

print(to_decimal("ZZZZZ", 36))
        
