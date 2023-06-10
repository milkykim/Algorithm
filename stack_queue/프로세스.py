from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    indexes = deque(list(i for i in range(0, len(priorities))))
    answer = []
    num_of_priorities = len(priorities)

    while len(answer) < num_of_priorities:
        p = priorities.popleft()
        i = indexes.popleft()
        if priorities and p < max(priorities):
            priorities.append(p)
            indexes.append(i)
        else:
            answer.append(i)

    return answer.index(location) + 1
