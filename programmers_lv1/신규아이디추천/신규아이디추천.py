def solution(new_id):
    # 1
    new_id = new_id.lower()
    print(new_id)
    # 2
    for i, v in enumerate(new_id):
        if not(v == '_' or v == '-' or v == '.' or (ord(v) <=  122 and ord(v) >=97) or (ord(v) >= 48 and ord(v) <= 57)):
            new_id = new_id.replace(new_id[i], ' ')
    new_id = new_id.replace(' ', '')
    print(new_id)   
    # 3
    while new_id.count('..') > 0:
        new_id = new_id.replace('..', '.')
    print(new_id)
    # 4
    if new_id[0] == '.': new_id = new_id[1:]
    print(new_id)
    # 5
    if not new_id:
        new_id += 'a'
    print(new_id)
    # 6
    if len(new_id) >= 16 : 
        new_id = new_id[:15]
    if new_id[-1] =='.':
        new_id = new_id[:-1]
    print(new_id)
    # 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    print(new_id)
    return new_id

solution("...!@BaT#*..y.abcdefghijklm")


# a = '_!afevE@0'
# a = a.upper()
# print(a[2:])
# b = ''
# if b:
#     print("b is empth") 
# for i in a:
#     print(i)

# a = a.replace('_', '1')

# print(a.count(''))

# p = 'AAABBBBBBCCCBBBBBBBBBB'
# k = p.replace("BB", "B")
# print(k)
# print(k.join(' '))