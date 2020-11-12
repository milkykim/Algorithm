def solution(N, stages):
    answer = []
    result = []
    length = len(stages)
    str = ''

    for i in range(1, N+1):
        # stages에서 개수를 세기
        cnt = stages.count(i)
        
        if cnt == 0:
            failureRate=0
        else:    
            # 실패율 계산 
            failureRate = cnt / length
        
        length -= cnt
        answer.append((i,failureRate))
            

    answer = sorted(answer, key = lambda x: x[1], reverse=True)
    
    for i in answer:
        result.append(i[0])
    
    # answer = [i[0] for i in answer]
    
    return result