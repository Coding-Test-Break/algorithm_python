def solution(n, arr1, arr2):
    answer = [[] for i in range(n)]
    print(answer)
    binary_arr1 = list(); binary_arr2 = list()
    for i , j in zip(arr1, arr2):
        binary_arr1.append(to_binary(i, n))
        binary_arr2.append(to_binary(j, n)) 

    for i in range(n):
        for j in range(n):
            if binary_arr1[i][j] == 1 or binary_arr2[i][j] == 1:
                answer[i] += "#"
            else: answer[i] += " "
        answer[i] = "".join(answer[i])
    
    return answer

def to_binary(num, arrLen):
    arr_binary = list()
    for i in reversed(range(arrLen)):
        arr_binary.append(num // 2 ** i)
        num = num % 2 ** i
    return arr_binary