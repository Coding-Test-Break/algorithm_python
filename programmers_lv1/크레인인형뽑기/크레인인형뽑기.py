def solution(board, moves):
    answer = 0
    stack = list()
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    while(True):
        breakpoint = 0
        for i in range(len(stack) - 1):
            if stack[i] == stack[i + 1]:
                answer += 2
                stack = stack[:i] + stack[i + 2:]
                breakpoint = 1
                break
        if breakpoint == 0:
            break

    return answer