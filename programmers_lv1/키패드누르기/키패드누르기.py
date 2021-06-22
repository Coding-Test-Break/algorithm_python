def coordinator(num):
    if num % 3 == 0:
        row = num // 3 - 1
        col = 2
    else:
        row = num // 3
        col = num % 3 - 1

    if num == 0:
        row = 3
        col = 1
    return row, col


def solution(numbers, hand):
    answer = ''
    left = set([1, 4, 7])
    right = set([3, 6, 9])
    middle = set([2, 5, 8, 0])

    left_row = 3
    left_col = 0

    right_row = 3
    right_col = 2
    
    for number in numbers:
        if number in left:
            answer = answer + 'L'
            left_row, left_col = coordinator(number)
            
        elif number in right:
            answer = answer + 'R'
            right_row, right_col = coordinator(number)

        else:
            row, col = coordinator(number)
            left_diff = abs(left_row - row) + abs(left_col- col)
            right_diff = abs(right_row - row) + abs(right_col - col)

            if left_diff > right_diff:
                answer += 'R'
                right_row, right_col = row, col

            elif left_diff < right_diff:
                answer += 'L'
                left_row, left_col = row, col
            else:
                if hand == "right":
                    answer += 'R'
                    right_row, right_col = row, col
                else:
                    answer += 'L'
                    left_row, left_col = row, col

    return answer