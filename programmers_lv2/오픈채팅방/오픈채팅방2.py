def solution(record):
    mapping = dict()
    logs = list()
    for record_iter in record:
        try:
            action, id, nickname = record_iter.split() 
        except:
            action, id = record_iter.split()

        if action == "Enter":
            mapping[id] = nickname
            logs.append([id, "님이 들어왔습니다."])
        elif action == "Leave":
            logs.append([id,"님이 나갔습니다."])
        elif action == "Change":
            mapping[id] = nickname

    for i in range(len(logs)):
        logs[i] = mapping[logs[i][0]] + logs[i][1]

    return logs
