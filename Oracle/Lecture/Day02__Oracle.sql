
-- �Լ��� SELECT, WHERE �� ���밡��
-- LENGTH() : NUMBER -> ������ ������ ��ȯ�ϴ� �Լ�
-- ���ڿ�
-- CHAR(��������) -->    ���Ӻ� ����Ʈ ������ ���ؼ��� �������� ó��
-- VARCHAR2(��������)--> ������ ����Ʈ ������ ���ؼ��� ��Ű�� (�ظ��ϸ� �ش� ���ڿ��� ������ ����)
-- �ѱ� 1 ���� = 3 byte (����) ������������ 18 byte
-- 20 - 18 = 2 
--           :
--     6  +  2 = 8 = LENGTH(CHARTYPE)
SELECT  CHARTYPE,
        LENGTH(CHARTYPE),
        VARCHARTYPE,
        LENGTH(VARCHARTYPE)        
FROM    COLUMN_LENGTH;


-- LPAD/RPAD : ���ڿ��� ���̸� �����̴� �Լ�
-- ����ȿ���� �������� ���ؼ� ����ϴ� ��찡 ����
-- EMAIL �� 30 byte�� �ְ� ����ִ� ������ '.' ��Ʈ�� ä���ش�

-- LPAD ���ڿ��� ���������� ����
SELECT  EMAIL,
        LPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

-- RPAD ���ڿ��� �������� ����
SELECT  EMAIL,
        RPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

SELECT  EMAIL,
        RPAD(EMAIL,30,'.'),
        LPAD(EMAIL,30,''),
        LENGTH(LPAD(EMAIL,30,''))
FROM    EMPLOYEE;


-- TRIM: ���ڸ� �����Ҷ� ����ϴ� �Լ�
-- LTRIM : ���ڿ��� �������� ���� / RTRIM : ���ڿ��� ������ ����
-- DUAL

SELECT  LTRIM('  TEST  '),
        LENGTH(LTRIM('  TEST  ')),
        LTRIM('123123TEST','123'),  -- ���� ��ĭ�� 1 �Ǵ� 2 �Ǵ� 3 ���� ã�� ����
        LTRIM('XYZYYTEST','XYZ'),   -- ���� ��ĭ�� X �Ǵ� Y �Ǵ� Z ���� ã�� ����
        TRIM(LEADING  '1'  FROM 'TEST1'),       -- LTRIM ��ɰ� ���� - '1' ���� ������ ������ ���� X
        TRIM(TRAILING '1'  FROM '123TEST111')   -- RTRIM ��ɰ� ���� - ������ '1' ����
FROM    DUAL;


-- SUBSTR  : ���� ����
SELECT  SUBSTR('This.is.a.test', 6, 2),     -- 6��° ���� �����Ͽ� 2���� ���ڸ� �����´�
        SUBSTR('This.is.a.test', 6),        -- 6��° ���� ������ ��ü�� �����´�
        SUBSTR('�̰���.�����Դϴ�', 3, 4),     
        SUBSTR('TechOnTheNet', 1, 4),
        SUBSTR('TechOnTheNet', -3, 3),      -- N(-3) ���� �����Ͽ� Net(3) ���� �����´�
        SUBSTR('TechOnTheNet', -6, 3),
        SUBSTR('TechOnTheNet', -8, 2)
FROM    DUAL;


-- ROUND : ������ �ڸ������� �ݿø��ϴ� �Լ�
SELECT  ROUND(123.315),     --> 123.315 ���
        ROUND(123.315, 0),  --> 123.315 ���
        ROUND(123.315, 1),  --> .31  ���� �ݿø��Ͽ� .3 ���� ���
        ROUND(123.315, -1), --> 123. ���� �ݿø��Ͽ� 130 ���� ���
        ROUND(123.315, 3),  
        ROUND(-123.315, 2)   --> -125.32 ���� �ݿø��Ͽ� -125.32 ���
FROM    DUAL;


-- TRUNC : ������ �ڸ������� �����ϴ� �Լ�
SELECT  TRUNC(123.315),     --> 123 ���
        TRUNC(123.315, 0),  --> 123 ���
        TRUNC(123.315, 1),  --> .3 ���� �����ϰ� ������ ._15�� ����
        TRUNC(123.315, -1), --> 1�ڸ����ڸ� ������ �� ���ڸ� �����Ͽ� 130 ���� ���
        TRUNC(123.315, 3),  --> 123.315 ���
        TRUNC(-123.315, -3) --> 100�ڸ��� ���ڸ� ������ �� ���ڸ� �����Ͽ� 0 ���
FROM    DUAL;


SELECT  *
FROM    EMPLOYEE;

SELECT  SYSDATE
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        ADD_MONTHS(HIRE_DATE, 240)  -->  + 240���� �� ���
FROM    EMPLOYEE;

SELECT  MONTHS_BETWEEN (SYSDATE, '21/03/14'),
        MONTHS_BETWEEN (SYSDATE, '20/03/14'),
        MONTHS_BETWEEN (SYSDATE, '21/01/19'),
        MONTHS_BETWEEN (SYSDATE, '20/11/19')
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        MONTHS_BETWEEN (SYSDATE, HIRE_DATE)/12 AS �ٹ����
FROM    EMPLOYEE
WHERE   MONTHS_BETWEEN (SYSDATE, HIRE_DATE) > 120;


-- ���ڿ��Լ� INSTR(string, searchChar, [position, occurrence]) : �ش� ������ �ε��������� ����
--                                              �ɼ�
-- EMAIL �÷� ���� '@vcc.com'���ڿ� �� . ���� ���� 'c' ��ġ�� ���Ѵٸ�?

SELECT  *
FROM    EMPLOYEE ;

SELECT  EMAIL,
        INSTR(EMAIL , 'c'),
        INSTR(EMAIL , 'c', -1, 2),
        INSTR(EMAIL , 'c', INSTR(EMAIL , '.')-1)
FROM    EMPLOYEE ;

-- TO_CHAR �Լ� : ������ Ÿ�Ժ�ȯ �Լ�
-- TO_CHAR(��¥ or ���� , ǥ������) -> ����

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
        TO_CHAR(HIRE_DATE, 'YYYY-MM-DD') AS "��Ī",
        TO_CHAR(HIRE_DATE, 'YYYY"��" MM"��" DD"��"'),
        SUBSTR(HIRE_DATE, 1, 2) || '��' ||
        SUBSTR(HIRE_DATE, 4, 2) || '��' ||
        SUBSTR(HIRE_DATE, 7, 2) || '��' AS �Ի���
FROM    EMPLOYEE ;

-- SUBSTR(����|��¥)


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
-- ���缼��    ��������
SELECT EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE, 'YYYY/MM/DD'),
        TO_CHAR(HIRE_DATE, 'YYRR/MM/DD'),
        TO_CHAR(HIRE_DATE, 'RRRR/MM/DD')
FROM    EMPLOYEE
WHERE   EMP_NAME = '�Ѽ���';


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
        DECODE(SUBSTR(EMP_NO,8,1),'1','����','3','����','����' AS GENDER 
FROM    EMPLOYEES;

SELECT  EMP_ID,
        EMP_NAME,
        DECODE(MGR_ID, NULL, 'ADMIN', MGR_ID) AS "MANAGER",
        NVL(MGR_ID, 'ADMIN') AS "OTHER CASE"
FROM    EMPLOYEE
WHERE   JOB_ID = 'J4';


-- ������ ���޺� �λ�޿��� Ȯ���ϰ� �ʹ�
-- J7 -> 20%
-- J6 -> 15%
-- J5 -> 10%
-- ������ ������ �λ� ���� �ʴ´�

SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        DECODE(JOB_ID,
            'J7', SALARY * 1.2,
            'J6', SALARY * 1.15,
            'J5', SALARY * 1.1,
            SALARY) AS "�λ�޿�"
FROM    EMPLOYEE ;      

SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE JOB_ID
            WHEN 'J7' THEN SALARY * 1.2
            WHEN 'J6' THEN SALARY * 1.15
            WHEN 'J5' THEN SALARY * 1.1
            ELSE SALARY
        END AS "�λ�޿�"
FROM    EMPLOYEE ;   


-- Group Function(�����Լ�, �׷��Լ�)
-- Group by
-- �׷��Լ��� SELECT �� ���Ǹ� �ٸ��÷� ���Ǵ� �Ұ�
-- �׷��Լ��� NULL �� ������ ������ �ϹǷ� ���ǿ��

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


-- �μ���ȣ�� 50 ���̰ų� �μ���ȣ�� �������� �ʴ� ����� �̸�, �޿��� ��ȸ�϶�
-- ���� �޿������� ������? ORDER BY [�����÷�] [ASC|DESC]
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' OR DEPT_ID IS NULL
ORDER BY SALARY DESC ;


-- �Ի����� 03�� 1�� 1�� ���� �̻��ڵ��� �̸�, �Ի���, �μ���ȣ�� ��ȸ�϶�
-- ��)�μ���ȣ�� ���������� �����ϰ� ������ �Ի����� ���������� �����ϰ� ������ �̸� ���� ������ �����Ѵ�.

SELECT  EMP_NAME �̸�,
        HIRE_DATE �Ի���,
        DEPT_ID �μ�
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('03/01/01')
ORDER BY 3 DESC NULLS LAST,
         2 ASC,
         1 ASC;
         
-- GROUP BY [����Ŀ��]
-- �μ��� ��ձ޿�
SELECT  DEPT_ID,
        ROUND (AVG(SALARY),-5) AS �޿����
FROM    EMPLOYEE
GROUP BY DEPT_ID 
ORDER BY �޿���� DESC;

SELECT  DEPT_ID,
        JOB_ID,
        ROUND (AVG(SALARY),-5) AS �޿����
FROM    EMPLOYEE
GROUP BY ROLLUP(DEPT_ID, JOB_ID)
--HAVING  AVG(SALARY) > 3000000
ORDER BY DEPT_ID ;

-- ������ ���� �޿� ����� ���Ѵٸ�?
-- ORDER BY [�����÷�]|�÷��ε���|��Ī
SELECT  DECODE(SUBSTR(EMP_NO,8,1),
                '1', '����', '3', '����', '����'),
        ROUND (AVG(SALARY),-5) AS �޿����
FROM    EMPLOYEE
GROUP BY DECODE(SUBSTR(EMP_NO,8,1),
                '1', '����', '3', '����', '����')
ORDER BY 2 DESC;


SELECT  CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '����'
            WHEN '3' THEN '����'
            ELSE '����'
        END,
        ROUND (AVG(SALARY),-5) AS �޿����
FROM    EMPLOYEE
GROUP BY CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '����'
            WHEN '3' THEN '����'
            ELSE '����'
        END
ORDER BY 2 DESC;
