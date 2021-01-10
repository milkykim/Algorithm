# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# https://programmers.co.kr/skill_checks/231212?challenge_id=2552

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for idx, _ in enumerate(phone_book):
        if idx == len(phone_book) - 1:
            break
        elif phone_book[idx] in phone_book[idx+1]:
            answer = False
            break
    
    return answer