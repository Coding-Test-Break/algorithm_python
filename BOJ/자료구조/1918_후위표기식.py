import sys

string = sys.stdin.readline().strip()
calculator = ["+", "-", "*", "/"]
answer = []
stack = []

for iter in string:
    if iter.isalpha():
        answer.append(iter)
        if stack and stack[-1]:
            answer.append(stack.pop())
    elif iter in calculator:
        if iter in "*/" and answer[-1] in "+-":
            stack.append(answer.pop())
        stack.append(iter)
    elif iter == "(":
        stack.append(False)
    elif iter == ")":
        if stack[-1]:
            answer.append(stack.pop())
        else: stack.pop()

while stack:
    if stack[-1]:
        a = stack.pop()
        answer.append(a)
    else: 
        a = stack.pop()

print("".join(answer))
