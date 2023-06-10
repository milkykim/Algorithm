from collections import deque


def solution(s):
    dq_s = deque(s)
    tmp = []

    while dq_s:
        if tmp and dq_s[0] == ")" and tmp[-1] != dq_s[0]:
            tmp.pop()
            dq_s.popleft()
        else:
            tmp.append(dq_s.popleft())

    return not tmp
