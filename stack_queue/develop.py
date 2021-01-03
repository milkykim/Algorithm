# 프로그래머스 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    # 값이 남아있을 때까지
    while progresses:
        # 완료 못했다면 time을 하나씩 올려주고 반복.
        # 반복이 하나 끝나면 count를 append.
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
            
    answer.append(count)
    return answer