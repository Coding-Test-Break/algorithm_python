def solution(m, musicinfos):
    answer = list()
    mm = list()
    for i in m:
        if i == "#":
            mm[-1] = mm[-1] + "#"
        else:
            mm.append(i)
            
    # 100
    for info in musicinfos:
        s, e, name, mel = info.split(",")
        s_h, s_m = s.split(":")
        e_h, e_m = e.split(":")
        t = (int(e_h) - int(s_h)) * 60 + int(e_m) - int(s_m)
        mel_l = list()
        # 1439
        for i in mel:
            if i == "#":
                mel_l[-1] = mel_l[-1] + "#"
            else:
                mel_l.append(i)
        
        cur = 0
        i = 0
        streak = False
        # 24 * 60 ~= 1200
        while i < t:
            j = i % len(mel_l)

            if mel_l[j] == mm[cur]:
                cur += 1
                streak = True
                if cur == len(mm):
                    answer.append((name, t, i))
                    break
            else:
                cur = 0
                if streak:
                    i -= 1
                streak = False
            i += 1 
    
    if not answer:
        return "(None)"
    answer.sort(key = lambda x: (-x[1], x[2]), reverse = True)
    
    return answer.pop()[0]

# 시간복잡도 신경 쓸 필요 없는데 구현이 짜증났다. 
# 첨에 생각하지 못한 엣지케이스도 존재했음.