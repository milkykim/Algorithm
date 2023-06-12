from collections import deque


def solution(bridge_length, weight, truck_weights):
    crossings = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    sum = 0

    while crossings:
        time += 1
        sum -= crossings.popleft()

        if truck_weights:
            if weight - sum >= truck_weights[0]:
                sum += truck_weights[0]
                crossings.append(truck_weights.popleft())
            else:
                crossings.append(0)

    return time


# sum(crossings)이 O(n) 시간복잡도이므로, 따로 변수를 두고 계속 기억하는 방식을 썼나봄
# reverse()하여, pop(0) 보다 pop()을 하여 시간을 더 줄이는 방법도 씀
