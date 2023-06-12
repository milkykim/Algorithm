from collections import deque


def solution(priorities, location):
    idx_priorities = deque([(p, i) for i, p in enumerate(priorities)])
    completed_process = []

    while idx_priorities:
        (p, i) = idx_priorities.popleft()
        if idx_priorities and p < max(idx_priorities)[0]:
            idx_priorities.append((p, i))
        else:
            completed_process.append(i)

    return completed_process.index(location) + 1
