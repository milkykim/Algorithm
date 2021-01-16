# 프로그래머스 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

def solution(people, limit):
    answer = len(people)
    
    # 내림차순으로 정렬 [50,40,30,20,10]
    p = sorted(people,reverse = True)
    s,e = 0, len(p)-1
    
    while s < e : 
        if p[s] + p[e] <= limit :
            e -= 1
            answer -= 1
        s += 1
        
    return answer