from itertools import permutations
import copy

def operate(x, y, operator):
    if operator == "*":
        return x * y
    elif operator == "-":
        return x - y
    else:
        return x + y

def solution(expression):
    answer = 0
    x = ["+", "-", "*"]
    priorities = permutations(x, 3)
    
    operators = list()
    operands = list()
    chunk = ""
    for i in list(expression):
        if i in x:
            operators.append(i)
            if chunk != "":
                operands.append(int(chunk))
                chunk = ""
        else:
            chunk += i    
    if chunk != "":
        operands.append(int(chunk))
        
    # 6
    for priority in priorities:
        temp_ops = copy.deepcopy(operators)
        temp_opers = copy.deepcopy(operands)
        # 3
        for op in priority:
            # 50 
            while op in temp_ops:
                # 50 49 ... 1 
                for i, v in enumerate(temp_ops):
                    if v == op:
                        # 50 
                        temp_ops.pop(i)
                        temp_opers[i] = operate(temp_opers.pop(i), temp_opers[i], op)
                        break
        answer = max(answer, abs(temp_opers[0]))
    
    return answer

# O(n^3) 인데 n이 50 이므로 passsss

print(solution("50*6-3*2"))

