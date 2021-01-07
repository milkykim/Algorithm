# 프로그래머스 124나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    num = ['1','2','4']
    answer = ""
    
    # 삼진법 - 3으로 나눈 후 나머지를 num리스트의 인덱스로 사용
    # 나머지가 0이면 num[0] = 1, 나머지 1이면 num[1] = 2, 나머지 2이면 num[2] = 4
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
        
    return answer