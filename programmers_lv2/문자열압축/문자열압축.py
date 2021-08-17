def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        result_array = calculator(s, i)
        while (0 in result_array):
            result_array.remove(0)
        print(result_array)
        total_len = len(s) - sum(result_array) * i + len(result_array) 
        count = 0
        for i in result_array:
            if i // 10: 
                count += len(str(i // 10))
            
        total_len += count
        print(total_len)
        if total_len < answer:
            answer = total_len
        
    return answer
    
def calculator(array, split_len):
    iter_num = (len(array) // split_len) if (len(array) % split_len == 0) else (len(array) // split_len + 1)
    new_array = [0]
    index = 0
    for i in range(iter_num - 1):
        if array[split_len * i : split_len * (i + 1)] == array[split_len * (i + 1) : split_len * (i + 2)]:
            new_array[index] += 1

        else:
            index += 1
            new_array.append(0)
    return new_array

aa = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# print(calculator(aa, 3))
# print(solution(aa))
k = 99
print(len(str(k // 10)))
