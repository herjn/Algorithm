# 모든 레코드 조회 문제
/*SELECT * 를 통해 ANIMAL_INS의 모든 컬럼 조회
ANIMAL_ID 순으로.*/
SELECT * FROM ANIMAL_INS 
ORDER BY ANIMAL_ID


#역순 정렬 문제
/* name과 datetime 가져오고 ANIMAL_ID 순을 역순으로.*/
SELECT NAME, DATETIME FROM ANIMAL_INS 
ORDER BY ANIMAL_ID DESC

#조건 선택 문제
/* 아픈 동물만 선택하여 id와 name을 조회*/
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
WHERE ANIMAL_INS.INTAKE_CONDITION = 'Sick' ORDER BY ANIMAL_ID

#어린 동물 찾기 문제
/* 젊은 동물 id와 name을 조회*/
SELECT ANIMAL_ID,NAME FROM ANIMAL_INS 
WHERE INTAKE_CONDITION != "Aged"

#동물의 아이디순 정렬 조회 문제
/* 모든 동물의 id와 name을 조회*/
SELECT ANIMAL_ID,NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID

#여러 기준으로 정렬하기 문제
/* 이름순으로 (같을때 보호 시작일 순) 정렬*/
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS 
ORDER BY NAME ASC, DATETIME DESC

#상위 n개 레코드 문제
/*가장 먼저 들어온 애 조회*/
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
