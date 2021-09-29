import sys

N = int(sys.stdin.readline())
rgb_list = list()
# N = 1000, 1] for _ in range(1000)]

if N == 1:
    print(min(rgb_list))
else:
    for _ in range(N):
        rgb_list.append(list(map(int, sys.stdin.readline().split())))

    dp_dict = dict({0 : [1, 2], 1 : [0, 2], 2 : [0, 1]})
    answer = list()

    for k in dp_dict.keys():
        p, q = dp_dict[k]    
        dp_list = list()
        for i in range(1, N):
            temp = dp_list.copy()
            if i == 1:
                dp_list = [rgb_list.copy()[i][p], rgb_list.copy()[i][q]]
                continue
            dp_list[0] = temp[1] + rgb_list[i][p]
            dp_list[1] = temp[0] + rgb_list[i][q]
        answer.append(min(dp_list) + rgb_list[0][k])
    print(min(answer))

# if N == 1:
#     print(min(rgb_list))
# else:
#     print(min(answer))
    