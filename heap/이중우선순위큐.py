import heapq
from collections import deque


def solution(operations):
    min_hq = []
    max_hq = []
    operations = deque(operations)

    while operations:
        op = operations.popleft()
        if op[0] == "I":
            num = int(op.split()[1])
            heapq.heappush(min_hq, num)
            heapq.heappush(max_hq, (-num, num))
        elif min_hq and op == "D -1":
            heapq.heappop(min_hq)
            max_hq.pop()
        elif max_hq and op == "D 1":
            heapq.heappop(max_hq)
            min_hq.pop()

    if max_hq or min_hq:
        return [heapq.heappop(max_hq)[1], heapq.heappop(min_hq)]

    return [0, 0]
