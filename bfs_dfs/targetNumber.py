def solution(numbers, target):
    # result는 0부터 시작. 하나식 원소를 빼서 더하고 뺀 값이 계속 추가 될 것.
    result = [0]

    # i는 numbers의 각 원소들
    for i in range(len(numbers)):
        temp = []

        
        # result의 값을 하나씩 빼서 number의 한 원소를 더하고 빼서 그 값을 result로 대치해준다.
        for j in range(len(result)):
            temp.append(result[j] - numbers[i])
            temp.append(result[j] + numbers[i])

        result = temp
        print(result)

    return result.count(target)

solution([1, 1, 1, 1, 1],3)