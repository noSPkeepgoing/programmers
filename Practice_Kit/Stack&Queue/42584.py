from collections import deque


def solution(prices):
    prices = deque(prices)
    answer = []

    while prices:
        cnt = 0
        price = prices.popleft()
        for p in prices:
            cnt += 1
            if p < price:
                break
        answer.append(cnt)
    return answer
