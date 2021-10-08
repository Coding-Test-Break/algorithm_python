from itertools import combinations

def solution(orders, course):
    answer = list()

    for menu_num in course:
        menu_dict = dict()
        for order in orders:
            menu_combination = combinations(sorted(order), menu_num)
            for menu_combination_iter in menu_combination:
                try:
                    menu_dict["".join(menu_combination_iter)] += 1
                except:
                    menu_dict["".join(menu_combination_iter)] = 1         

        max_count = max(menu_dict.values())
        for key in menu_dict.keys():
            if menu_dict[key] == max_count and menu_dict[key] > 1:
                answer.append(key)

    return sorted(answer)


a = "abc"
b = "cab"
print(b)
print(sorted(b))