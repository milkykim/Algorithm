# 프로그래머스 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

def solution(priorities, location):
    # priorities -> 문서의 중요도가 순서대로 담긴 배열
    # location -> 현재 대기목록의 어떤 위치에 있는지 알려주는 배열
    q = []
    
    while priorities:
        print(priorities)
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
        else:
            q.append(priorities[0])
            if location == 0:
                return len(q)
            priorities.pop(0)
            location -= 1