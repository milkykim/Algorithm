# 프로그래머스 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    answer = n-len(lost)
    
    # lost배열에 있는 사람들을 체크해야함.
    for idx in range(len(lost)):
        
        if lost[idx] in reserve:
            answer += 1
            reserve.pop(reserve.index(lost[idx]))
        
        # 앞뒤로 빌려줄 수 있는 사람을 체크
        else:
            if (lost[idx]-1 in reserve) and (lost[idx]-1 not in lost):
                answer += 1
                reserve.pop(reserve.index(lost[idx]-1))
            elif (lost[idx]+1 in reserve) and (lost[idx]+1 not in lost):
                answer += 1
                reserve.pop(reserve.index(lost[idx]+1))
    
    return answer