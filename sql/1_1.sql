# 모든 레코드 조회 문제
/*SELECT * 를 통해 ANIMAL_INS의 모든 컬럼을 가져올 수 있게 된다.
ANIMAL_ID 순으로 가져오라고 했으므로 FROM 아래에 
ORDER BY ANIMAL_ID 를 넣어 ANIMAL_ID 순으로 가져오면 해결이다.*/

SELECT * FROM ANIMAL_INS 
ORDER BY ANIMAL_ID


#역순 정렬 문제
/*SELECT * 를 통해 ANIMAL_INS의 모든 컬럼을 가져올 수 있게 된다.
name과 datetime 가져오고 ANIMAL_ID 순을 역순으로.*/

SELECT NAME, DATETIME FROM ANIMAL_INS 
ORDER BY ANIMAL_ID DESC
