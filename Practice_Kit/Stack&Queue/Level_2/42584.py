# 주식가격
# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

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
