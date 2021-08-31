string = input()
res = ''
for i in string:
    if 97 <= ord(i) <= 122:
        res += chr((ord(i)+13) if i <= 'm' else ord(i)-13)
    elif 65 <= ord(i) <= 90:
        res += chr((ord(i)+13) if i <= 'M' else ord(i)-13)
    else:
        res += i
print(res)
