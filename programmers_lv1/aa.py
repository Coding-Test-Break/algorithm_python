
def solution(arr):
    i = 1
    while(len(arr) > i):
        if arr[i- 1] == arr[i]:
            del arr[i - 1]
        else: i += 1
    return arr


def solution2(arr, index):
    if arr[index - 1] == arr[index]:
        solution(arr[1:], index)
    else: solution(arr, index + 1)

    return arr



# print(solution([1,1,3,3,0,1,1]))
a = [1, 2, 3, 4, 5,]
print(a[1:])