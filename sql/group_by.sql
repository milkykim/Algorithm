-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC

-- 동명 동물 수 찾기(두 번 이상 쓰인 이름, 해당 이름 쓰인 횟수 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59041
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL 
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME

-- 입양 시각 구하기(1)(몇 시에 입양이 가장 활발하게 일어났는지 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59412#qna

-- DATETIME 형식엔 HOUR라는 함수가 기본적으로 있다.
SELECT HOUR(dateTime) as "HOUR", count(HOUR(dateTime)) as COUNT 
FROM ANIMAL_OUTS
where HOUR(dateTime) > 8 and HOUR(dateTime) < 20
group by HOUR(dateTime)
order by HOUR(dateTime)


-- 입양 시각 구하기(2)(각 시간대별 입양이 몇건 발생했는지 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59413#qna
with recursive time as
(select 0 as hour union all select hour+1 from time where hour<23)
select hour, count(animal_id) count
from time
left outer join animal_outs on (hour = date_format(datetime, '%H') )
group by hour;
