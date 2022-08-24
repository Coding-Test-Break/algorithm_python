def solution(relation):
    answer = 0
    global collection
    collection = []
    
    
    for i in range(1, len(relation[0]) + 1):
      for j in range(0, len(relation[0])):
          comb(j, [], len(relation[0]), i)
    
    sorted_col = sorted(collection, key = lambda x: len(x))
    keys = []
    for c in sorted_col:
        bp = False
        for k in keys:
          s1 = set(k)
          s2 = set(c)
          if s1 & s2 == s1:
            bp = True
            break
        if bp:
          continue
        s = set()
        for i in range(len(relation)):
            t = tuple()
            for j in c:
                t += tuple(relation[i][j])
            if t not in s:
                s.add(t)
            else:
                break
        else:
            keys.append(c)
    return len(keys)


def comb(i, arr, n, r):
    if len(arr) == r:
        if arr not in collection:
          collection.append(arr)
          return 
    for j in range(i, n):
        temp = arr.copy()
        temp.append(j)
        comb(j + 1, temp, n, r)
  
# print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))