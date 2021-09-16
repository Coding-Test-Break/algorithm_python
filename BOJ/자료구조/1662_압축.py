import sys

ext = sys.stdin.readline().rstrip()

num_stack = list()
oper_stack = list()

def operator(a, b, oper):
    if oper == "*":
        return a * b
    elif oper == "+":
        return a + b

for i in range(len(ext)):
    # i가 0이면 그냥 1 추가 
    if not i:
        num_stack.append(1)
        continue
        
    if ext[i].isnumeric():
        # i가 1이상이고, 숫자이며 이전이 숫자면 가장 위 stack에 1 더해줌
        if ext[i - 1].isnumeric():
            num_stack[-1] += 1
        # i가 1 이상이고, 숫자지만 이전에 괄호가 나왔다면 stack에 1을 추가함            
        else:
            num_stack.append(1)

    # 여는 괄호가 나온다면 가장 위 stack에서 1을 빼주고 이전 숫자를 stack에 추가 -> operation stack에 + 와 * 순차적으로 추가
    elif ext[i] == "(":
        num_stack[-1] -= 1
        num_stack.append(int(ext[i - 1]))
        oper_stack.append("+")
        oper_stack.append("*")
    
    # 닫는 괄호가 나오면 operation stack을 2개 소비해서 계산함
    elif ext[i] == ")":
        num_stack.append(operator(num_stack.pop(), num_stack.pop(), oper_stack.pop()))
        num_stack.append(operator(num_stack.pop(), num_stack.pop(), oper_stack.pop()))

        # 더 문자열이 남아있고, 다음에 괄호가 아닌 숫자가 나온다면 operation stack에 + 를 추가해줌.
        if i + 1 < len(ext) and ext[i + 1].isnumeric():
            oper_stack.append("+")

# 남은 operation stack을 모두 소비해서 계산한 후 마지막 계산의 결과를 pop
while oper_stack:
    num_stack.append(operator(num_stack.pop(), num_stack.pop(), oper_stack.pop()))
else:
    print(num_stack.pop()) 