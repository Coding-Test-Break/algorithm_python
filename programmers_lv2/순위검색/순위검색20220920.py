odds = list()
def solution(info, query):
    q = dict()
    recur("")

    # 100,000 
    for i in query:
        언어, 분야, 직급, 음식점수 = map(str, i.split("and"))
        음식, 점수 = map(str, 음식점수.split())
        q[(언어.strip(), 분야.strip(), 직급.strip(), 음식.strip())] = []
    
    
    # 50,000 * 16 * 4 = 3_200_000
    # 50,000
    for i in info:
        언어, 분야, 직급, 음식, 점수 = map(str, i.split(" "))
        # 2^4 = 16 
        for o in odds:
            # 4
            k = to_key(o, [언어.split(), 분야.split(), 직급.split(), 음식.split()])
            try:
                q[k].append(int(점수.strip()))
            except: 
                pass
    
    # 4 * 3 * 3 * 3 = 100
    for key in q.keys():
        # nlogn
        q[key].sort()
        

    answer = []
    # 100,000 * 25,000 = 25,000,00,000 >> 시간초과
    # 100,000
    for i in query:
        언어, 분야, 직급, 음식점수 = map(str, i.split("and"))
        음식, 점수 = map(str, 음식점수.split())
        # 1 ~ 50,000 = 25,000 
        # for j in q[(언어.strip(), 분야.strip(), 직급.strip(), 음식.strip())]:
        #     if j >= int(점수):
        #         cnt += 1 
        #     else: 
        #         break
        cur = binary_search(q[(언어.strip(), 분야.strip(), 직급.strip(), 음식.strip())], 점수)
        
        
        answer.append(len(q[(언어.strip(), 분야.strip(), 직급.strip(), 음식.strip())]) - cur)
        
    return answer

def recur(st):
    global odds
    if len(st) == 4:
        odds.append(st)
        return
    recur(st + "1")
    recur(st + "0")

def to_key(st, lst):
    tup = tuple()
    for i in range(len(lst)):
        if st[i] == "0":
            tup += tuple("-")
        else:
            tup += tuple(lst[i])
    return tup

def binary_search(arr, target):
    left = 0; right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1 
    return right