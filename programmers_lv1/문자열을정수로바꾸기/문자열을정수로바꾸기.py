def solution(s):
    try:
        return int(s)
    except ValueError:
        return  (-1) * int(s[1:])