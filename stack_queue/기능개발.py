import math
from collections import Counter


def solution(progresses, speeds):
    answer = []

    for p, s in zip(progresses, speeds):
        n = math.ceil((100 - p) / s)

        if answer and answer[-1] > n:
            answer.append(answer[-1])
        else:
            answer.append(n)

    return list(Counter(answer).values())
