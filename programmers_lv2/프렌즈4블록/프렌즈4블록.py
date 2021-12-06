# 2 * 2 블록을 형성하는지 확인하는 함수. 맞을 경우 True를 return. 
def block_check(i, j, board):
    cur = board[i][j]
    if cur == board[i + 1][j] and cur == board[i][j + 1] and cur == board[i + 1][j + 1]:
        return True
    return False

def solution(m, n, board):
    board_list = []
    answer = 0
    # input인 board는 string (immutable type)이므로 element 변경이 용이한 list (mutable type)으로 옮겨담아줌. 
    for b in board: 
        board_list.append(list(b))
    
    # 블록을 더 이상 형성하지 않을 때까지 while loop을 실행.
    while True:
        # 블록을 형성해서 0이 될 블록의 좌표들을 담는 set 자료형 (중복 불가능)
        clear_set = set()
        # 각 좌표 (맨 오른쪽 column과 맨 밑의 row는 검사하지 않음)를 순회하며 블록을 형성하는지 확인.
        for i in range(m - 1):
            for j in range(n - 1):
                if board_list[i][j] == 0:
                    continue
                elif block_check(i, j, board_list):
                    # 블록을 형성할 경우, 각 좌표들을 set에 추가.
                    clear_set.update([(i, j),(i + 1, j), (i, j + 1), (i + 1, j + 1)])

        # set에 추가된 것이 없다는 건, 이번 회차에 블록이 형성되지 않은 것이므로 while loop를 탈출한다. 
        if not clear_set: 
            break

        # clear_set에 들어있는 좌표들의 값을 0으로 바꾸어주고, 이 때마다 answer를 1씩 늘려준다.  
        for i, j in clear_set:
            board_list[i][j] = 0
            answer += 1

        # 좌표를 우하단부터 좌상단까지 reversed로 순회하면서, 0을 만날 경우 해당 column의 바로 위에 있는 0이 아닌 값을 찾아 해당 위치에 넣어준다. 
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if board_list[i][j] == 0:
                    for k in reversed(range(i)):
                        if board_list[k][j]:
                            board_list[i][j], board_list[k][j] = board_list[k][j], board_list[i][j]
                            break
    
    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
solution(m, n, board)

