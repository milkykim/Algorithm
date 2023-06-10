from collections import deque


def solution(arr):
    dq = deque(arr)
    v = dq.popleft()
    answer = [v]

    while dq:
        if v != dq[0]:
            v = dq.popleft()
            answer.append(v)
        else:
            v = dq.popleft()

    return answer
