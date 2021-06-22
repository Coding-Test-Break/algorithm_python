``` python
def solution(n, lost, reserve):
    
    # 우선 번호가 동일한 친구들을 지워줍니다. 두 번의 계산이 필요하므로 임시로 값을 담아줄 변수인 temp_lost를 선언했습니다. 
    temp_lost = list(set(lost) - set(reserve))
    reserve =list(set(reserve) - set(lost))
    lost = temp_lost

    # 번호가 오른쪽인 친구를 지워줍니다.
    temp_lost = list(set(lost) - set(addition(reserve, create_one_list(reserve))))
    reserve = list(set(reserve) - set(subtraction(lost, create_one_list(lost))))
    lost = temp_lost

    # 왼쪽인 친구를 지워줍니다. 이 후의 연산이 없고, lost값만 구하면 되기에 reserve는 구하지 않습니다. 
    lost = list(set(lost) - set(subtraction(reserve, create_one_list(reserve))))

    return n - len(lost)

# 1로 이루어진 list를 만듭니다 (행렬의 합연산과 차연산을 위해)
def create_one_list(X):
    one_list = list([1] * len(X))
    return one_list

# 행렬의 차연산을 해줍니다 (한칸 왼쪽에 있는 번호를 비교하기 위해)
def subtraction(X, one_list):
    sub = list()
    for i in range(len(X)):
        sub.append(X[i] - one_list[i])
    return sub

# 행렬의 합연산을 해줍니다 (1칸 오른쪽에 있는 번호를 비교하기 위해)
def addition(X, one_list):
    add = list()
    for i in range(len(X)):
        add.append(X[i] + one_list[i])
    return add
```
