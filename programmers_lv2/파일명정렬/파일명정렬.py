num = "0123456789"

def solution(files):
    lst = list()
    answer = []
    # 소문자화 
    # 1000
    for i, f in enumerate(files):
        cur = 0
        head, number, tail = "", "", ""
        status = "H"
        # 100
        while cur < len(f):
            if status == "H":
                if f[cur] in num:
                    status ="N"
                    continue
                head += f[cur]
            elif status == "N":
                if f[cur] not in num:
                    status = "T"
                    continue
                number += f[cur]
                    
            elif status == "T":
                tail += f[cur]
            cur += 1
        # 요 구간에서 0인 경우를 생각못하고 돌려서 런타임에러가 주구장창 났다. 빨리 알아채서 다행.
        nb = number.lstrip("0") 
        if not nb:
            nb = 0
        else:
            nb = int(nb)
        
        lst.append((head, number, tail, head.lower(), nb, i))
    
    lst.sort(key = lambda x: (x[3], x[4], x[5]))
    for head, number, tail, h, nb, cur in lst:
        answer.append("".join([head, number, tail]))
    
    return answer

# 그냥 문자열 구현 문제.
# 시간 복잡도나 알고리즘 생각 안해도 되니 편했지만 엣지케이스에 걸리는 걸 조심해야할 듯 .. 