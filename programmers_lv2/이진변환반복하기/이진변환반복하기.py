def solution(s):
    answer = []
    binary_count = 1
    zero_count = 0
    
    for i in range(len(s)):
        if s[i] == '0':
            zero_count += 1
    
    num = len(s) - zero_count
    print(num)
    while num != 1:
        print(num)
        binary_count += 1
        bnum, zc = binary(num, 0)

        num = len(bnum)

        zero_count += zc
            
    return [binary_count, zero_count]


def binary(m, z_cnt):
    nm, nn = divmod(m, 2)
    if nm == 0:
        return (str(nn), z_cnt)
    if nn == 0:
        z_cnt += 1
        nn = ""
    else:
        nn = str(nn)
    
    bs, zc = binary(nm, z_cnt)
    return (bs + nn, zc)


print(solution("110010101001"))
    
    