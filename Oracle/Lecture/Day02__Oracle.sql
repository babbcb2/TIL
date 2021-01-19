
-- 함수는 SELECT, WHERE 에 적용가능
-- LENGTH() : NUMBER -> 문자의 갯수를 반환하는 함수
-- 문자열
-- CHAR(고정길이) -->    나머비 바이트 공간에 대해서는 공백으로 처리
-- VARCHAR2(가변길이)--> 나머지 바이트 공간에 대해서는 패키지 (왠만하면 해당 문자열을 사용것이 좋다)
-- 한글 1 문자 = 3 byte (예시) 엘지씨엔에스 18 byte
-- 20 - 18 = 2 
--           :
--     6  +  2 = 8 = LENGTH(CHARTYPE)
SELECT  CHARTYPE,
        LENGTH(CHARTYPE),
        VARCHARTYPE,
        LENGTH(VARCHARTYPE)        
FROM    COLUMN_LENGTH;


-- LPAD/RPAD : 문자열의 길이를 덧붙이는 함수
-- 정렬효과를 가져오기 위해서 사용하는 경우가 많다
-- EMAIL 에 30 byte를 주고 비어있는 공강은 '.' 도트로 채워준다

-- LPAD 문자열을 오른쪽으로 정렬
SELECT  EMAIL,
        LPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

-- RPAD 문자열을 왼쪽으로 정렬
SELECT  EMAIL,
        RPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

SELECT  EMAIL,
        RPAD(EMAIL,30,'.'),
        LPAD(EMAIL,30,''),
        LENGTH(LPAD(EMAIL,30,''))
FROM    EMPLOYEE;


-- TRIM: 문자를 제거할때 사용하는 함수
-- LTRIM : 문자열의 오른쪽을 제거 / RTRIM : 문자열의 왼쪽을 제거
-- DUAL

SELECT  LTRIM('  TEST  '),
        LENGTH(LTRIM('  TEST  ')),
        LTRIM('123123TEST','123'),  -- 문자 한칸씩 1 또는 2 또는 3 값을 찾아 제거
        LTRIM('XYZYYTEST','XYZ'),   -- 문자 한칸씩 X 또는 Y 또는 Z 값을 찾아 제거
        TRIM(LEADING  '1'  FROM 'TEST1'),       -- LTRIM 기능과 동일 - '1' 없기 때문에 삭제할 내용 X
        TRIM(TRAILING '1'  FROM '123TEST111')   -- RTRIM 기능과 동일 - 문자의 '1' 삭제
FROM    DUAL;


-- SUBSTR  : 문자 추출
SELECT  SUBSTR('This.is.a.test', 6, 2),     -- 6번째 부터 시작하여 2개의 문자를 가져온다
        SUBSTR('This.is.a.test', 6),        -- 6번째 부터 문자의 전체를 가져온다
        SUBSTR('이것은.연습입니다', 3, 4),     
        SUBSTR('TechOnTheNet', 1, 4),
        SUBSTR('TechOnTheNet', -3, 3),      -- N(-3) 부터 시작하여 Net(3) 값을 가져온다
        SUBSTR('TechOnTheNet', -6, 3),
        SUBSTR('TechOnTheNet', -8, 2)
FROM    DUAL;


-- ROUND : 지정한 자릿수에서 반올림하는 함수
SELECT  ROUND(123.315),     --> 123.315 출력
        ROUND(123.315, 0),  --> 123.315 출력
        ROUND(123.315, 1),  --> .31  에서 반올림하여 .3 으로 출력
        ROUND(123.315, -1), --> 123. 에서 반올림하여 130 으로 출력
        ROUND(123.315, 3),  
        ROUND(-123.315, 2)   --> -125.32 에서 반올림하여 -125.32 출력
FROM    DUAL;


-- TRUNC : 지정한 자릿수에서 버림하는 함수
SELECT  TRUNC(123.315),     --> 123 출력
        TRUNC(123.315, 0),  --> 123 출력
        TRUNC(123.315, 1),  --> .3 까지 유지하고 나머지 ._15는 버림
        TRUNC(123.315, -1), --> 1자리숫자를 포함한 뒷 숫자를 버림하여 130 으로 출력
        TRUNC(123.315, 3),  --> 123.315 출력
        TRUNC(-123.315, -3) --> 100자리리 숫자를 포함한 뒷 숫자를 버림하여 0 출력
FROM    DUAL;


SELECT  *
FROM    EMPLOYEE;

SELECT  SYSDATE
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        ADD_MONTHS(HIRE_DATE, 240)  -->  + 240월의 값 출력
FROM    EMPLOYEE;

SELECT  MONTHS_BETWEEN (SYSDATE, '21/03/14'),
        MONTHS_BETWEEN (SYSDATE, '20/03/14'),
        MONTHS_BETWEEN (SYSDATE, '21/01/19'),
        MONTHS_BETWEEN (SYSDATE, '20/11/19')
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        MONTHS_BETWEEN (SYSDATE, HIRE_DATE)/12 AS 근무년수
FROM    EMPLOYEE
WHERE   MONTHS_BETWEEN (SYSDATE, HIRE_DATE) > 120;


-- 문자열함수 INSTR(string, searchChar, [position, occurrence]) : 해당 문자의 인덱스번지를 리턴
--                                              옵션
-- EMAIL 컬럼 값의 '@vcc.com'문자열 중 . 앞의 문자 'c' 위치를 구한다면?

SELECT  *
FROM    EMPLOYEE ;

SELECT  EMAIL,
        INSTR(EMAIL , 'c'),
        INSTR(EMAIL , 'c', -1, 2),
        INSTR(EMAIL , 'c', INSTR(EMAIL , '.')-1)
FROM    EMPLOYEE ;

-- TO_CHAR 함수 : 데이터 타입변환 함수
-- TO_CHAR(날짜 or 숫자 , 표현형식) -> 문자

SELECT  TO_CHAR(1234, '99999'),
        TO_CHAR(1234, '09999'),
        TO_CHAR(1234, 'L9999'),
        TO_CHAR(1234, '99,999'),
        TO_CHAR(1234, '09,999'),
        TO_CHAR(1000, '9.9EEEE'),
        TO_CHAR(1234, '999')
FROM    DUAL;

SELECT  SYSDATE,
        TO_CHAR(SYSDATE, 'YYYY'),
        TO_CHAR(SYSDATE, 'YEAR'),
        TO_CHAR(SYSDATE, 'YYYY-MONTH'),
        TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS'),
        TO_CHAR(SYSDATE, 'YYYY-MM-DD Q HH:MI:SS')
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE, 'YYYY-MM-DD') AS "별칭",
        TO_CHAR(HIRE_DATE, 'YYYY"년" MM"월" DD"일"'),
        SUBSTR(HIRE_DATE, 1, 2) || '년' ||
        SUBSTR(HIRE_DATE, 4, 2) || '월' ||
        SUBSTR(HIRE_DATE, 7, 2) || '일' AS 입사일
FROM    EMPLOYEE ;

-- SUBSTR(문자|날짜)


-- TO DATE
SELECT  TO_DATE('20210112', 'YYYYMMDD')
FROM    DUAL ;

SELECT  TO_CHAR(TO_DATE('20100101', 'YYYYMMDD'),'YYYY, MON'),
        TO_CHAR(TO_DATE('041030 143000', 'YYMMDD HH24MISS'), 'DD-MON-YY HH:MI:SS PM')
FROM    DUAL ;

SELECT  HIRE_DATE        
FROM    EMPLOYEE
WHERE   HIRE_DATE = TO_DATE('900401 133030', 'YYMMDD HH24MISS');

SELECT  HIRE_DATE        
FROM    EMPLOYEE
WHERE   TO_CHAR(HIRE_DATE, 'YYMMDD') = '900401' ;


-- YYYY     - RRRR
-- 현재세기    이전세기
SELECT EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE, 'YYRR/MM/DD'),
        TO_CHAR(HIRE_DATE, 'RRRR/MM/DD')
FROM    EMPLOYEE
WHERE   EMP_NAME = '한선기';


-- TO NUMBER(CHAR) -> NUMBER
SELECT  EMP_NO,
        SUBSTR(EMP_NO, 1, 6),
        SUBSTR(EMP_NO, 8),
        TO_NUMBER(SUBSTR(EMP_NO, 1, 6)) + TO_NUMBER(SUBSTR(EMP_NO, 8))
FROM    EMPLOYEE;

-- NVL
SELECT  EMP_NAME, SALARY, NVL(BONUS_PCT,0)
FROM    EMPLOYEE
WHERE   SALARY > 3500000;

SELECT  EMP_NAME,
        (SALARY*12)+((SALARY*12)*BONUS_PCT)
FROM    EMPLOYEE
WHERE   SALARY > 3500000;

SELECT  EMP_NAME,
        (SALARY*12)+((SALARY*12)*NVL(BONUS_PCT,0))
FROM    EMPLOYEE
WHERE   SALARY > 3500000;


SELECT  EMP_NO,
        DECODE(SUBSTR(EMP_NO,8,1),'1','남자','3','남자','여자' AS GENDER 
FROM    EMPLOYEES;

SELECT  EMP_ID,
        EMP_NAME,
        DECODE(MGR_ID, NULL, 'ADMIN', MGR_ID) AS "MANAGER",
        NVL(MGR_ID, 'ADMIN') AS "OTHER CASE"
FROM    EMPLOYEE
WHERE   JOB_ID = 'J4';


-- 직원의 직급별 인상급여를 확인하고 싶다
-- J7 -> 20%
-- J6 -> 15%
-- J5 -> 10%
-- 나머지 직급은 인상 하지 않는다

SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        DECODE(JOB_ID,
            'J7', SALARY * 1.2,
            'J6', SALARY * 1.15,
            'J5', SALARY * 1.1,
            SALARY) AS "인상급여"
FROM    EMPLOYEE ;      

SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE JOB_ID
            WHEN 'J7' THEN SALARY * 1.2
            WHEN 'J6' THEN SALARY * 1.15
            WHEN 'J5' THEN SALARY * 1.1
            ELSE SALARY
        END AS "인상급여"
FROM    EMPLOYEE ;   


-- Group Function(집계함수, 그룹함수)
-- Group by
-- 그룹함수가 SELECT 절 사용되면 다름컬럼 정의는 불가
-- 그룹함수는 NULL 값 제거후 연산을 하므로 주의요망

SELECT  SUM(SALARY), SUM(DISTINCT SALARY), EMP_NAME
FROM    EMPLOYEE;

SELECT  AVG(BONUS_PCT),
        AVG(NVL(BONUS_PCT,0))
FROM    EMPLOYEE;

-- MIN, MAX, COUNT -> ANY
SELECT  MIN(SALARY), MAX(SALARY),
        MIN(HIRE_DATE), MAX(HIRE_DATE),
        MIN(JOB_ID), MAX(JOB_ID)
FROM    EMPLOYEE;

-- COUNT
SELECT  COUNT(*), COUNT(JOB_ID)
FROM    EMPLOYEE;


-- 부서번호가 50 번이거나 부서번호가 존재하지 않는 사원의 이름, 급여를 조회하라
-- 높은 급여순으로 볼려면? ORDER BY [기준컬럼] [ASC|DESC]
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' OR DEPT_ID IS NULL
ORDER BY SALARY DESC ;


-- 입사일이 03년 1월 1일 이후 이사자들의 이름, 입사일, 부서번호를 조회하라
-- 단)부서번호가 높은순으로 정렬하고 같으면 입사일이 빠른순서로 정렬하고 같으면 이름 빠른 순서로 정렬한다.

SELECT  EMP_NAME 이름,
        HIRE_DATE 입사일,
        DEPT_ID 부서
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('03/01/01')
ORDER BY 3 DESC NULLS LAST,
         2 ASC,
         1 ASC;
         
-- GROUP BY [기준커럼]
-- 부서별 평균급여
SELECT  DEPT_ID,
        ROUND (AVG(SALARY),-5) AS 급여평균
FROM    EMPLOYEE
GROUP BY DEPT_ID 
ORDER BY 급여평균 DESC;

SELECT  DEPT_ID,
        JOB_ID,
        ROUND (AVG(SALARY),-5) AS 급여평균
FROM    EMPLOYEE
GROUP BY ROLLUP(DEPT_ID, JOB_ID)
--HAVING  AVG(SALARY) > 3000000
ORDER BY DEPT_ID ;

-- 성별에 따른 급여 평균을 구한다면?
-- ORDER BY [기준컬럼]|컬럼인덱스|별칭
SELECT  DECODE(SUBSTR(EMP_NO,8,1),
                '1', '남자', '3', '남자', '여자'),
        ROUND (AVG(SALARY),-5) AS 급여평균
FROM    EMPLOYEE
GROUP BY DECODE(SUBSTR(EMP_NO,8,1),
                '1', '남자', '3', '남자', '여자')
ORDER BY 2 DESC;


SELECT  CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '남자'
            WHEN '3' THEN '남자'
            ELSE '여자'
        END,
        ROUND (AVG(SALARY),-5) AS 급여평균
FROM    EMPLOYEE
GROUP BY CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '남자'
            WHEN '3' THEN '남자'
            ELSE '여자'
        END
ORDER BY 2 DESC;
