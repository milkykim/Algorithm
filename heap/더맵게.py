import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        answer += 1

        try:
            heapq.heappush(
                scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            )
        except IndexError:  # heap이 비어있을 때 = K이상으로 만들 수 없음을 의미
            return -1

    return answer
