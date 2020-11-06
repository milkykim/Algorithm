def solution(numbers, target):
    # result는 0부터 시작. 그리고, [0, 0-a, 0+a, 0-a-b, 0-a+b, 0+a-b, 0+a+b, ... ] 이런 식으로 간다.
    result = [0]

    # i는 numbers의 각 원소들
    for i in range(len(numbers)):
        temp = []

        # result는 0부터 numbers의 각 원소들을 빼고 더한 값들이 있다.
        # result의 값을 하나씩 빼서 number의 한 원소를 더하고 빼서 그 값을 result로 대치해준다.
        for j in range(len(result)):
            
            temp.append(result[j] - numbers[i])
            temp.append(result[j] + numbers[i])
            print("temp=>",temp)

        result = temp
        print(result)

    return result.count(target)

solution([1, 1, 1, 1, 1],3)