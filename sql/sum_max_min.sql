-- 최댓값 구하기(가장 최근에 들어온 시간 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59415
SELECT DATETIME AS "시간"
FROM ANIMAL_INS
ORDER BY DATETIME DESC LIMIT 1;

SELECT MAX(DATETIME)
FROM ANIMAL_INS
ORDER BY DATETIME DESC;


-- 최솟값 구하기(가장 먼저 들어온 시간 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59038
SELECT MIN(DATETIME) AS "시간" 
FROM ANIMAL_INS
ORDER BY DATETIME;


-- 동물 수 구하기
-- https://programmers.co.kr/learn/courses/30/lessons/59406
SELECT COUNT(*) AS count
FROM ANIMAL_INS


-- 중복 제거하기(중복, NULL을 제외한 개수 세기)
-- https://programmers.co.kr/learn/courses/30/lessons/59408
SELECT COUNT(DISTINCT NAME) 
FROM ANIMAL_INS
WHERE NAME IS NOT NULL