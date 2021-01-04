# 효율성 통과 못함

# cards 리스트에서 카드 1장을 잃어버렸는데, 해당 카드가 뭔지 맞춰라.
# 다른 카드들은 모두 2개씩 갖추고 있음.
def solution(cards):
    answer = 0

    for i in cards:
        if cards.count(i) == 1:
            answer = i
            break

    return answer

print(solution([2,3,2,1,1,4,4,5,5]))

def solution2(cards):
    answer = 0
    cards.sort()

    for idx in range(0,len(cards),2): #0부터 cards배열 길이까지 인덱스는 2씩 증가
        if cards[idx] != cards[idx+1]:
            answer = cards[idx]
            break

    return answer

print(solution2([2,3,2,1,1,4,4,5,5]))

# SQL 문제
# 3개의 join을 해야하는 문제. 
# 2019/01/06에 대여할 수 있는 장소 중, 리뷰가 달려있는 장소의 ID와 NAME 조회

# SELECT P.ID, P.NAME
# FROM PLACES P JOIN SCHEDULES S, PLACE_REVIEWS R
# WHERE S.SCHEDULED_AT = '2019-01-06 00:00:00' 
# AND P.ID = S.PLACE_ID AND P.ID=R.PLACE_ID AND S.PLACE_ID = R.PLACE_ID
# GROUP BY P.ID
# ORDER BY P.ID