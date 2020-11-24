# 입국심사: https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    times.sort()
    
    # 시작 시간
    start = 0
    # 끝(제일 오래 걸리는) 시간
    end = times[len(times)-1] * n
    
    answer = 0
    
    while(start <= end):
        total = 0
        mid = (start+end) // 2
        
        for x in times:
            # mid를 7,10분으로 나눈 몫을 total에 넣어서 다 수용가능한지 보는 것
            total += mid // x
            
            # total이 심사하는 사람보다 더 크면 break문으로 미리 나감
            if total > n:
                break

        # 일단 answer에 값을 저장해둠
        if total >= n:
            answer = mid
            end = mid-1

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        else:
            start = mid+1

    return answer