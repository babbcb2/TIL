
-- 1. 영어영문학과(학과코드 002) 학생들의 학번과 이름, 입학 년도를 입학 년도가 빠른 순으로 표시하는 SQL 문장을 작성하시오.
--    ( 단, 헤더는 "학번", "이름", "입학년도" 가표시되도록 핚다.)

SELECT  STUDENT_NO AS 학번,
        STUDENT_NAME AS 이름,
        ENTRANCE_DATE AS 입학년도
FROM    TB_STUDENT
WHERE   DEPARTMENT_NO = 002
ORDER BY 입학년도 ;


-- 2. 춘 기술대학교의 교수 중 이름이 세 글자가 아닌 교수가 한명 있다고 한다. 
--    그 교수의 이름과 주민번호를 화면에 출력하는 SQL 문장을 작성해 보자.
--    (* 이때 올바르게 작성한 SQL 문장의 결과 값이 예상과 다르게 나올 수 있다. 원인이 무엇일지 생각해볼 것)

SELECT  PROFESSOR_NAME,
        PROFESSOR_SSN
FROM    TB_PROFESSOR
WHERE   LENGTH(PROFESSOR_NAME) > 3 OR LENGTH(PROFESSOR_NAME) < 3 ;


-- 4. 교수들의 이름 중 성을 제외한 이름한 출력하는 SQL 문장을 작성하시오. 
--    출력 헤더는 ?이름? 이 찍히도록 핚다. (성이 2 자인 경우는 교수는 없다고 가정하시오)

SELECT  TRIM(LEADING FROM PROFESSOR_NAME) AS 이름
FROM    TB_PROFESSOR;


-- 5. 춘 기술대학교의 재수생 입학자를 구하려고 한다. 어떻게 찾아낼 것인가?
--    이때, 19 살에 입학하면 재수를 하지 않은 것으로 간주한다.



