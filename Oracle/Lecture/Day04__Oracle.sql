
-- SET Operator - UNION 

SELECT  EMP_ID,
        ROLE_NAME
FROM    EMPLOYEE_ROLE
UNION
SELECT  EMP_ID,
        ROLE_NAME
FROM    ROLE_HISTORY;


SELECT  EMP_NAME,
        JOB_ID,
        HIRE_DATE
FROM    EMPLOYEE
WHERE   DEPT_ID = '20'
UNION
SELECT  DEPT_NAME,
        DEPT_ID,
        NULL
FROM    DEPARTMENT
WHERE   DEPT_ID = '20';

-- UNION 50번 부서원을 관리자 직원으로 구분하여 표시하고 싶다면?

SELECT  *
FROM    EMPLOYEE
WHERE   DEPT_ID = '50';
UNION
SELECT  TO_CHAR(MGR_ID = '관리자')
FROM    EMPLOYEE
WHERE   MGR_ID IS NULL


SELECT  EMP_ID,
        EMP_NAME,
        '노예' AS 구분
FROM    EMPLOYEE
WHERE   MGR_ID IS NOT NULL
AND     DEPT_ID = '50'
UNION
SELECT  EMP_ID,
        EMP_NAME,
        '관리자' AS 구분
FROM    EMPLOYEE
WHERE   MGR_ID IS NULL
AND     DEPT_ID = '50'
ORDER BY 3 ;


-- 직급(JOB_TITLE)이 대리 또는 사원 직원정보를 조회 (이름,직급)
-- UNION

SELECT  EMP_NAME, JOB_TITLE
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '대리'
UNION
SELECT  EMP_NAME, JOB_TITLE
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '사원'
ORDER BY 2 ; 

-- 나승원의 이름을 이용하여
-- 직급이 동일하고, 나승원보다 급여(SALARY)가 많은 사원의 이름, 직급, 급여를 조회하라

SELECT  EMP_NAME, JOB_ID, SALARY
FROM    EMPLOYEE
WHERE   JOB_ID = (SELECT  JOB_ID
                  FROM    EMPLOYEE
                  WHERE   EMP_NAME = '나승원')
AND     SALARY > (SELECT  SALARY
                  FROM    EMPLOYEE
                  WHERE   EMP_NAME = '나승원')

-- 최소급여를 받는 사원의 이름, 직급, 급여를 조회하라

SELECT  EMP_NAME,
        JOB_ID,
        SALARY
FROM    EMPLOYEE
WHERE   SALARY = (SELECT  MIN(SALARY)
                  FROM    EMPLOYEE)


-- 부서별(GROUP BY) 급여총합이 가장 많은 부서의 이름, 급여 총합을 조회하라

SELECT  DEPT_NAME,
        SUM(SALARY)
FROM    EMPLOYEE
JOIN    DEPARTMENT USING(DEPT_ID)
GROUP BY DEPT_NAME
HAVING  SUM (SALARY) = (SELECT  MAX(SUM(SALARY))
                        FROM    EMPLOYEE
                        GROUP BY DEPT_ID)


-- IN, NOT IN, ANY, ALL 연산자를 다중행 서브쿼리에서 사용할 수 있다.

SELECT  EMP_ID,
        EMP_NAME,
        '관리자' AS 구분
FROM    EMPLOYEE
WHERE   EMP_ID IN (SELECT MGR_ID
                   FROM EMPLOYEE)
UNION
SELECT  EMP_ID,
        EMP_NAME,
        '직원' AS 구분
FROM    EMPLOYEE
WHERE   EMP_ID NOT IN (SELECT MGR_ID
                       FROM EMPLOYEE
                       WHERE MGR_ID IS NOT NULL)

-- 위 구현 코드를 다른 방식으로 (UNION)사용하지 않고 구현한다면?
-- IF ~ ELSE 제한 (DECODE, CASE ~ END)

SELECT  EMP_ID,
        EMP_NAME,
        CASE 
            WHEN MGR_ID IS NULL THEN '관리자'
            ELSE '직원'
        END
FROM    EMPLOYEE;


-- ANY 연산자
-- 서브쿼리 결과안에서 값에서 체크됨  
-- 2100000  > ANY   210 보다 높은 값을 체크
-- 2300000
-- 2600000  < ANY   260 보다 낮은 값을 체크

SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '대리'
AND     SALARY > ANY
                    (SELECT SALARY
                    FROM    EMPLOYEE
                    JOIN    JOB USING (JOB_ID)
                    WHERE   JOB_TITLE = '과장');


SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '대리'
AND     SALARY < ANY
                    (SELECT SALARY
                    FROM    EMPLOYEE
                    JOIN    JOB USING (JOB_ID)
                    WHERE   JOB_TITLE = '과장');
                    
-- ALL 연산자   
-- 서브쿼리 결과밖의 값에서 체크됨     
-- 2100000  < ALL   210 보다 낮은 값을 체크
-- 2300000
-- 2600000  > ALL   260 보다 높은 값을 체크
                    
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '대리'
AND     SALARY > ALL
                    (SELECT SALARY
                    FROM    EMPLOYEE
                    JOIN    JOB USING (JOB_ID)
                    WHERE   JOB_TITLE = '과장');
  
                  
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '대리'
AND     SALARY < ALL
                    (SELECT SALARY
                    FROM    EMPLOYEE
                    JOIN    JOB USING (JOB_ID)
                    WHERE   JOB_TITLE = '과장');
                    

-- 자기 직급(JOB_ID)의 평균 급여를 받는 직원을 조회하라
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   (JOB_ID, SALARY) IN (SELECT  JOB_ID, TRUNC(AVG(SALARY), -5)
                             FROM    EMPLOYEE
                             JOIN    JOB USING(JOB_ID)
                             GROUP BY JOB_ID)
-- 서브쿼리
SELECT  JOB_ID, TRUNC(AVG(SALARY), -5)
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
GROUP BY JOB_ID

-- 다른접근방식
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    (SELECT  JOB_ID, TRUNC(AVG(SALARY), -5) AS JOBANG
                             FROM    EMPLOYEE
                             JOIN    JOB USING(JOB_ID)
                             GROUP BY JOB_ID) V
JOIN    EMPLOYEE E ON(V.JOB_ID = E.JOB_ID AND V.JOBANG = E.SALARY)
JOIN    JOB J ON(E.JOB_ID = J.JOB_ID)
 
 -- 상관관게 서브커리(Correlated SbuQuery)
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE E
JOIN    JOB J ON(E.JOB_ID = J.JOB_ID)
WHERE   SALARY = (  SELECT  TRUNC(AVG(SALARY),-5)
                    FROM    EMPLOYEE
                    WHERE   JOB_ID = E.JOB_ID)
                    
                    
SELECT  EMP_ID,
        EMP_NAME,
        '관리자' AS 구분
FROM    EMPLOYEE E
WHERE   EXISTS (SELECT  NULL
                FROM    EMPLOYEE
                WHERE E.EMP_ID = MGR_ID)
UNION
SELECT  EMP_ID,
        EMP_NAME,
        '직원' AS 구분
FROM    EMPLOYEE E2
WHERE   EXISTS (SELECT  NULL
                FROM    EMPLOYEE
                WHERE E2.EMP_ID = MGR_ID)
ORDER BY 3;