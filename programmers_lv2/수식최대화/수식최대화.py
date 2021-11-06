from itertools import permutations
from copy import deepcopy

def solution(expression):
    operator_ = ["+", "-", "*"]
    operator_list = []
    priorities = [1, 2, 3]
    answer = 0

    for tuple in permutations(priorities, 3):
        operator_dict = dict()
        for key, value in zip(operator_, tuple):
            operator_dict[key] = value
        operator_list.append(operator_dict)
    
    operands, operators = seperator(expression)
    for priority_dict in operator_list:
        answer = max(abs(expression_calculator(deepcopy(operands), deepcopy(operators), priority_dict)), answer)
        
    return answer


def seperator(expression):
    temp = ""; operands = []; operators = []
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            operands.append(int(temp))
            operators.append(i)
            temp = ""
    else: 
        operands.append(int(temp))

    return operands, operators

def expression_calculator(operands, operators, priority_dict):
    priority_sorted = sorted(priority_dict, key= lambda x: priority_dict[x])

    for operator in priority_sorted:
        index = 0
        while index < len(operators):
            if operators[index] == operator:
                operators.pop(index)
                result = num_calculator(operator, operands.pop(index), operands.pop(index))
                operands.insert(index, result)
                continue
            index += 1
    
    return operands[0]

def num_calculator(operator, *nums):
    if operator == "+":
        return nums[0] + nums[1]
    elif operator == "-":
        return nums[0] - nums[1]
    elif operator == "*":
        return nums[0] * nums[1]

a = solution("100-200*300-500+20")