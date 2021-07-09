def solution(s):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]
    for i in range(10):
        s = s.replace(number[i], str(i))
    return int(s)