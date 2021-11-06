from copy import deepcopy
def solution(grid, clockwise):
    answer = []
    length = len(grid)
    table = [[] for _ in range(length)]
    table[0] = [[length - 1, 0]]
    for i in range(1, length):
        temp_table = deepcopy(table[i - 1])
        for t in temp_table:
            t[0] -= 1
        table[i] = [[length - 1, i * 2], [length - 1, i * 2 - 1]] + temp_table
    
    if clockwise:
        for i, table_iter in enumerate(table):
            answer.append("")
            for j in table_iter:
                answer[i] += grid[j[0]][j[1]]
    else:
        for i in range(len(grid)):
            grid[i] = grid[i][::-1]
        for i, table_iter in enumerate(table):
            answer.append("")
            for j in table_iter:
                answer[i] += grid[j[0]][j[1]]
        for i in range(len(answer)):
            answer[i] = answer[i][::-1]

    return answer



grid = ["A","MAN","DRINK","WATER11"]
clockwise = False

solution(grid, clockwise)


#  설명
# 한 변의 길이가 1인 정삼각형 n2 개로 구성된 정삼각형 격자가 있습니다. 격자의 각 칸에는 문자(영어 대소문자 또는 숫자) 하나가 쓰여 있습니다. 당신은 이 격자를 시계 방향 또는 반시계 방향으로 120도 회전하고자 합니다.

# 격자의 정보를 나타내는 문자열 배열 grid와 회전 방향을 나타내는 clockwise가 매개변수로 주어집니다. 주어진 격자를 clockwise가 의미하는 방향으로 회전시킨 결과를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ grid의 길이 ≤ 1,000
# grid[i]의 길이 = 2 * i + 1
# grid[i]는 영어 대소문자 또는 숫자로 이루어진 문자열입니다.
# clockwise가 참이면 시계 방향, 거짓이면 반시계 방향으로 120도 회전해야 함을 의미합니다.
# 입출력 예
# grid	clockwise	result
# ["1","234","56789"]	true	["5","762","98431"]
# ["A","MAN","DRINK","WATER11"]	false	["1","K1R","NNIET","AAMRDAW"]
# 입출력 예 설명
# 입출력 예 #1

# 다음 애니메이션은 주어진 격자를 시계 방향으로 회전하는 것을 나타낸 것입니다.
# ex1

# 따라서, ["5","762","98431"]를 return 해야 합니다.
# 입출력 예 #2

# 다음 애니메이션은 주어진 격자를 반시계 방향으로 회전하는 것을 나타낸 것입니다.
# ex2

# 따라서, ["1","K1R","NNIET","AAMRDAW"]를 return 해야 합니다.
