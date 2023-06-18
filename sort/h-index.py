# 프로그래머스 h-index
# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3


def solution(citations):
    citations.sort()
    l = len(citations)

    for i in range(l):
        # 정렬되어있기 때문에, [1,2,3,4,5]
        if citations[i] >= l - i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l - i
    return 0


def solution(citations):
    citations.sort(reverse=True)
    h = 0

    for i, c in enumerate(citations, start=1):
        if c >= i:
            h = i

    return h
