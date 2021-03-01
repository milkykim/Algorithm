-- 역순 정렬하기
-- https://programmers.co.kr/learn/courses/30/lessons/59035
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

-- 아픈 동물 찾기
-- https://programmers.co.kr/learn/courses/30/lessons/59036
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION LIKE "S%"

-- 어린 동물 찾기(젊은 동물 ID와 이름 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59037
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION <> "Aged"
ORDER BY ANIMAL_ID

-- 여러 기준으로 정렬하기(모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59404
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC

-- 상위 n개 레코드(가장 먼저 들어온 동물의 이름을 조회하는 SQL 문)
-- https://programmers.co.kr/learn/courses/30/lessons/59405
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC LIMIT 1;

