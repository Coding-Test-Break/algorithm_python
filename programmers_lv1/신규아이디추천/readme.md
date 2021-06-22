``` python
def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    for i, v in enumerate(new_id):
        if not(v == '_' or v == '-' or v == '.' or (ord(v) <=  122 and ord(v) >=97) or (ord(v) >= 48 and ord(v) <= 57)):
            new_id = new_id.replace(new_id[i], ' ')
    new_id = new_id.replace(' ', '')

    # 3
    while new_id.count('..') > 0:
        new_id = new_id.replace('..', '.')

    # 4
    if new_id[0] == '.': new_id = new_id[1:]

    # 5
    if not new_id:
        new_id += 'a'

    # 6
    if len(new_id) >= 16 : 
        new_id = new_id[:15]
    if new_id[-1] =='.':
        new_id = new_id[:-1]

    # 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id
```
