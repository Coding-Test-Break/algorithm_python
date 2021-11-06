language = {"python": [], "java": [], "cpp": []}
career = {'senior': [], "junior": []}
soulfood = {'chicken': [], 'pizza': []}
career_type = {'frontend': [], 'backend': []}
all = []
score = []

def solution(info, query):
    answer = []
    for i, info_iter in enumerate(info):
        lan, car_type, car, soul, sc = info_iter.split()
        language[lan].append(i)
        career_type[car_type].append(i)
        career[car].append(i)
        soulfood[soul].append(i)
        all.append(i)
        score.append(sc)
    
    for query_iter in query:
        q = query_iter.split(" and ")
        q += q.pop().split()
        lan, car_type, car, soul, sc = q
        temp_set = set(all)
        if lan == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(language[lan])
        if car_type == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(career_type[car_type])
        if car == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(career[car])
        if soul == "-":
            temp_set = temp_set & set(all)
        else: 
            temp_set = temp_set & set(soulfood[soul])
            
        temp_set = list(temp_set)
        count = 0
        while temp_set:
            if int(sc) <= int(score[temp_set.pop()]):                
                count += 1

        answer.append(count)
    
    return answer
            

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))