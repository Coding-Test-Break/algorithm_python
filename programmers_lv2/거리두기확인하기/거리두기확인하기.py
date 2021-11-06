def solution(places):
    answer = []
    for place in places:
        answer.append(is_distancing(place))
            
    return answer
    
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
movements = [(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 0), (3, 2), (3, 3)]

def is_distancing(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if make_movements(i, j, place) == False:
                    return 0
    return 1

def make_movements(x, y, place):
    for move in movements:
        nx = x; ny = y
        for m in move:
            nx += dx[m]
            ny += dy[m]
            try: 
                if nx < 0 or ny < 0 or place[nx][ny] == "X":
                    break
                if place[nx][ny] == "P":
                    return False
            except IndexError:
                pass
    else:
        return True

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))