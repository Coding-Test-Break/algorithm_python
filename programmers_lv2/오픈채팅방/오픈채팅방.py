def solution(record):
    answer = []
    split_array = []
    user_list = dict()
    user_name = []
    hash_count = 0
    
    for record_iter in record:
        split_array.append(record_iter.split(" "))

    for i in split_array:
        if i[0] == "Enter":
            user_list[i[1]] = hash_count
            user_name.append(i[2])
            hash_count += 1
        
        elif i[0] == "Change":
            temp_index = user_list[i[1]]
            user_name[temp_index] = i[2]
        
    for i in split_array:
        if i[0] == "Enter":
            temp_index = user_list[i[1]]
            temp_name = user_name[temp_index]
            answer.append("{}님이 들어왔습니다.".format(temp_name))
        elif i[0] == "Leave":
            temp_index = user_list[i[1]]
            temp_name = user_name[temp_index]
            answer.append("{}님이 나갔습니다.".format(temp_name))
    
    return answer