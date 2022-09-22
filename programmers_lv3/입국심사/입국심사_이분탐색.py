def solution(n, times):
    max = 1_000_000_000_000_000
    left = 0
    right = max
    
    # logN: 1,000,000,000 * 100,000 
    while left <= right:
        m = 0
        mid = (left + right) // 2
        for t in times:
            m += mid // t
        # 합이 크거나 같을 경우 right을 당겨준다 (더 작은 값에서 만족할 수도 있으므로)
        if m >= n:
            right = mid - 1
        else: 
            left = mid + 1
    
    return left


# 이분탐색으로 아이디어를 내는게 관건인 문제 ...
# max 값 설정을 1,000,000,000이 아닌 1,000,000,000 * 100,000 으로 해줘야 했다. ; 최대 걸린 시간이므로