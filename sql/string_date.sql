-- 루시와 엘라 찾기(이름이 'Lucy','Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty' 인 동물 조회)
-- https://programmers.co.kr/learn/courses/30/lessons/59046
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN('Lucy','Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID

-- 이름에 'EL'이 들어가는 '개' 조회
-- https://programmers.co.kr/learn/courses/30/lessons/59047?language=mysql
-- %el : el로 끝나는 것 조회
-- el% : el로 시작하는 것 조회
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME

-- 중성화한 동물 O,X로 표기하기
-- https://programmers.co.kr/learn/courses/30/lessons/59409?language=mysql
SELECT ANIMAL_ID, NAME, 
CASE
    WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
    WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
    ELSE 'X'
END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회
-- https://programmers.co.kr/learn/courses/30/lessons/59411
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY OUTS.DATETIME - INS.DATETIME DESC LIMIT 2


-- DATETIME에서 DATE로 형 변환
-- https://programmers.co.kr/learn/courses/30/lessons/59414
SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') AS "날짜"
FROM ANIMAL_INS

