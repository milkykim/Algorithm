# k번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    result = []
    
    for temp_arr in commands:
        i = temp_arr[0] - 1
        j = temp_arr[1] - 1
        k = temp_arr[2] - 1
        
        answer = []
        
        for i in array[i:j+1]:
            answer.append(i)
        answer.sort()
        result.append(answer[k])
    
    return result
