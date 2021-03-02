-- 이름이 없는 동물의 아이디
-- https://programmers.co.kr/learn/courses/30/lessons/59039

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL


-- 이름이 있는 동물의 아이디
-- https://programmers.co.kr/learn/courses/30/lessons/59407

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL


-- 이름이 없는 동물의 이름은 No name으로 표시
-- https://programmers.co.kr/learn/courses/30/lessons/59410?language=mysql

SELECT ANIMAL_TYPE, 
CASE
    WHEN NAME IS NOT NULL THEN NAME
    WHEN NAME IS NULL THEN "No name"
END NAME, 
SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID