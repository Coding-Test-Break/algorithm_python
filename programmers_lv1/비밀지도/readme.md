``` python
def solution(n, arr1, arr2):
    answer = [[] for i in range(n)]
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
```

- `bin()`, `oct()`, `hex()` 내장함수를 통해 `2진수`, `8진수`, `16진수`를 다룰 수 있다. 
- 각각 string 형식으로 return 해주는데, 앞에 `0b`, `0o`, `0x` 가 붙으니 원하는 수를 return 한 후 indexing을 거쳐주면 편하게 이용할 수 있을듯..! 
- `.rjust()`, `.ljust()`, `.zfill()` 함수도 기회가 되면 이용해 볼 것 