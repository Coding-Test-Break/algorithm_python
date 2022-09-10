def solution(fees, records):
    temp = dict()
    r = dict()
    for rcd in records:
        (t, n, st) = rcd.split(" ")
        if st == "IN":
            temp[n] = t
            if n not in r.keys():
                r[n] = 0
    
        else:
            time = calc(t, temp[n])
            del temp[n]
            r[n] += time
    
    for k in temp.keys():
        time = calc("23:59", temp[k])
        r[k]  += time
        
    for k in r.keys():
        r[k] = calc2(r[k], fees[0], fees[1], fees[2], fees[3])
    
    answer = []
    ans = sorted(r)
    for a in ans:
        answer.append(r[a])
            
    return answer

def calc(x, y):
    h_x, m_x = map(int, x.split(":"))
    h_y, m_y = map(int, y.split(":"))
    return (h_x - h_y) * 60 + (m_x - m_y)
    
    

def calc2(time, base_time, base_fee, std_time, time_fee):
    if time <= base_time:
        return base_fee
    a, b = divmod(time - base_time, std_time)
    if b != 0:
        a += 1
    return base_fee + a * time_fee
                    

# n < 1,000인 문자열 문제. 딱히 시간복잡도 생각안했음
# 문제라면 좀 더럽게 풀었다.