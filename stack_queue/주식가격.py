from collections import deque


def solution(prices):
    dq = deque(prices)
    answer = []

    while dq:
        pos = dq.popleft()
        if not dq:
            time = 0
        for price in dq:
            time = len(dq)
            if pos > price:
                # 가격이 떨어진 적이 있는 것
                time = dq.index(price) + 1
                break

        answer.append(time)

    return answer
