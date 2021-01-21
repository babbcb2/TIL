-- SELECT 구문

SELECT [ *(전체컬럼) | 특정컬럼 | 표현식 (SELECT- (SUBQUERY) | DISTINCT | AS 컬럼별칭 ]
FROM       [ 테이블이름 | JOIN | (SELECT- (SUBQUERY) ]
WHERE       조건식 | (SELECT- (SUBQUERY)
GROUP BY    표현식 | (SELECT- (SUBQUERY)
HAVING      조건식
ORDER BY    기준컬럼


-- 전체컬럼 EMPLOYEE
SELECT  *
FROM    EMPLOYEE;

-- 특정컬럼
SELECT  EMP_NAME,
        EMP_NO
FROM    EMPLOYEE;

-- 별칭 
-- 주의사항: 반드시 문자로시작(숫자로 시작할수 없다
-- 만약 특수부호가 들어가면 "" 안에 넣어줘야한다, 공백 X 
-- AS 생략가능
SELECT  EMP_NAME AS "이 름",
        EMP_NO   AS 주민번호,
        SALARY   AS "급여(원)",
        DEPT_ID  부서번호
FROM    EMPLOYEE;

-- DISTINCT : 값의 중복을 제거할 때 사용하는 키워드
SELECT DISTINCT JOB_ID
FROM            EMPLOYEE;

-- 표현식
-- 컬럼 값에 대한 연산을 식으로 작성 할 수 있다.
SELECT  EMP_NAME AS 사원명,
        SALARY AS 급여,
        (SALARY+(SALARY*BONUS_PCT))*12 AS 연봉
FROM    EMPLOYEE;

-- 더미컬럼
-- '' < 데이터를 의미
-- "" < 
SELECT  EMP_ID,
        EMP_NAME,
        '재직' AS 근무여부
FROM    EMPLOYEE;

-- 부서번호가 90번인 사원들의 정보를 확인하고 싶다면
-- WHERE 행의 제한
-- 조건절에서 연산자를 사용할 수 있다.
SELECT  *
FROM    EMPLOYEE
WHERE   DEPT_ID=90;

-- 부서코드가 90 이고 급여를 2000000 보다 많이 받는 사원의 이름, 부서코드, 급여를 조회
SELECT EMP_NAME,
        DEPT_ID,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID=90 AND SALARY > 2000000;

-- 'xxx님의 월급은 xxxx원입니다.'
-- || - 연결연산자
-- [컬럼||컬럼||'문자열']

SELECT   EMP_ID ||'의 월급은'|| EMP_NAME || SALARY || '원 입니다'
FROM     EMPLOYEE;

-- BETWEEN
-- 급여를 3500000원 보다 많이 받고 5500000원보다 적게 받는 직원 이름과 급여 조회
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   SALARY BETWEEN 3500000 AND 6600000;

SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   SALARY >= 3500000
AND     SALARY <= 5500000;

-- LIKE
SELECT  EMP_NAME, SALARY
FROM    EMPLOYEE
WHERE   EMP_NAME LIKE '김%';

SELECT  EMP_NAME, PHONE
FROM    EMPLOYEE
WHERE   PHONE LIKE '___9_______';


-- E MAIL IDWND'_' 앞자리가 3자리인 직원 조회
SELECT  EMP_NAME,
        EMAIL
FROM    EMPLOYEE
WHERE   EMAIL LIKE '___#_%' ESCAPE '#';


- '김'씨 성이 아닌 직원의 이름과 급여를 조회
SELECT  EMP_NAME, SALARY
FROM    EMPLOYEE
WHERE   EMP_NAME NOT LIKE '김%'


-- 부서가 없는데도 불구하고 보너스를 지급받는 직원의 이름, 부서, 보너스를 조회한다면
SELECT  EMP_NAME, DEPT_ID, BONUS_PCT
FROM    EMPLOYEE
WHERE   DEPT_ID IS NULL AND BONUS_PCT IS NOT NULL;


-- 부서번호가 20번 또는 90번인 사원 중 급여가 300만원 보다 많이 받는 직원의 이름,급여,부서코드 조회
SELECT  EMP_NAME, SALARY, DEPT_ID
FROM    EMPLOYEE
WHERE   DEPT_ID = 90 OR DEPT_ID = 20
AND     SALARY > 3000000;


-- TB 연습
SELECT  *
FROM    TB_CLASS;



