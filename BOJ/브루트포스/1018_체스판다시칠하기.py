import sys
N, M = map(int, sys.stdin.readline().split())


chess_board = list()
count = []

for _ in range(N):
    chess_board.append(list(map(sys.stdin.readline().split())))

print(chess_board[0])