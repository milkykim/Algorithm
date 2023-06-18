def solution(array, commands):
    answer = []

    for case in commands:
        i, j, k = case[0], case[1], case[2]
        answer.append(sorted(array[i - 1 : j])[k - 1])

    return answer
