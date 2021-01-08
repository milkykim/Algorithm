-- 입양 온 동물 수 구하기
-- https://programmers.co.kr/learn/courses/30/lessons/59406?language=mysql
SELECT COUNT(ANIMAL_ID) AS "count"
FROM ANIMAL_INS

-- 중복제거(DISTINCT), NULL이 아닌 것 조회
-- https://programmers.co.kr/learn/courses/30/lessons/59408
SELECT COUNT(DISTINCT NAME) AS "count"
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

-- 가장 먼저 들어온 동물의 날짜 시간 조회
-- https://programmers.co.kr/learn/courses/30/lessons/59038
SELECT MIN(DATETIME) AS "시간"
FROM ANIMAL_INS

SELECT DATETIME AS "시간"
FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1;