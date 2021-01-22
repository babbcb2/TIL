-- SELECT ����

SELECT [ *(��ü�÷�) | Ư���÷� | ǥ���� (SELECT- (SUBQUERY) | DISTINCT | AS �÷���Ī ]
FROM       [ ���̺��̸� | JOIN | (SELECT- (SUBQUERY) ]
WHERE       ���ǽ� | (SELECT- (SUBQUERY)
GROUP BY    ǥ���� | (SELECT- (SUBQUERY)
HAVING      ���ǽ�
ORDER BY    �����÷�


-- ��ü�÷� EMPLOYEE
SELECT  *
FROM    EMPLOYEE;

-- Ư���÷�
SELECT  EMP_NAME,
        EMP_NO
FROM    EMPLOYEE;

-- ��Ī 
-- ���ǻ���: �ݵ�� ���ڷν���(���ڷ� �����Ҽ� ����
-- ���� Ư����ȣ�� ���� "" �ȿ� �־�����Ѵ�, ���� X 
-- AS ��������
SELECT  EMP_NAME AS "�� ��",
        EMP_NO   AS �ֹι�ȣ,
        SALARY   AS "�޿�(��)",
        DEPT_ID  �μ���ȣ
FROM    EMPLOYEE;

-- DISTINCT : ���� �ߺ��� ������ �� ����ϴ� Ű����
SELECT DISTINCT JOB_ID
FROM            EMPLOYEE;

-- ǥ����
-- �÷� ���� ���� ������ ������ �ۼ� �� �� �ִ�.
SELECT  EMP_NAME AS �����,
        SALARY AS �޿�,
        (SALARY+(SALARY*BONUS_PCT))*12 AS ����
FROM    EMPLOYEE;

-- �����÷�
-- '' < �����͸� �ǹ�
-- "" < 
SELECT  EMP_ID,
        EMP_NAME,
        '����' AS �ٹ�����
FROM    EMPLOYEE;

-- �μ���ȣ�� 90���� ������� ������ Ȯ���ϰ� �ʹٸ�
-- WHERE ���� ����
-- ���������� �����ڸ� ����� �� �ִ�.
SELECT  *
FROM    EMPLOYEE
WHERE   DEPT_ID=90;

-- �μ��ڵ尡 90 �̰� �޿��� 2000000 ���� ���� �޴� ����� �̸�, �μ��ڵ�, �޿��� ��ȸ
SELECT EMP_NAME,
        DEPT_ID,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID=90 AND SALARY > 2000000;

-- 'xxx���� ������ xxxx���Դϴ�.'
-- || - ���Ῥ����
-- [�÷�||�÷�||'���ڿ�']

SELECT   EMP_ID ||'�� ������'|| EMP_NAME || SALARY || '�� �Դϴ�'
FROM     EMPLOYEE;

-- BETWEEN
-- �޿��� 3500000�� ���� ���� �ް� 5500000������ ���� �޴� ���� �̸��� �޿� ��ȸ
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
WHERE   EMP_NAME LIKE '��%';

SELECT  EMP_NAME, PHONE
FROM    EMPLOYEE
WHERE   PHONE LIKE '___9_______';


-- E MAIL IDWND'_' ���ڸ��� 3�ڸ��� ���� ��ȸ
SELECT  EMP_NAME,
        EMAIL
FROM    EMPLOYEE
WHERE   EMAIL LIKE '___#_%' ESCAPE '#';


- '��'�� ���� �ƴ� ������ �̸��� �޿��� ��ȸ
SELECT  EMP_NAME, SALARY
FROM    EMPLOYEE
WHERE   EMP_NAME NOT LIKE '��%'


-- �μ��� ���µ��� �ұ��ϰ� ���ʽ��� ���޹޴� ������ �̸�, �μ�, ���ʽ��� ��ȸ�Ѵٸ�
SELECT  EMP_NAME, DEPT_ID, BONUS_PCT
FROM    EMPLOYEE
WHERE   DEPT_ID IS NULL AND BONUS_PCT IS NOT NULL;


-- �μ���ȣ�� 20�� �Ǵ� 90���� ��� �� �޿��� 300���� ���� ���� �޴� ������ �̸�,�޿�,�μ��ڵ� ��ȸ
SELECT  EMP_NAME, SALARY, DEPT_ID
FROM    EMPLOYEE
WHERE   DEPT_ID = 90 OR DEPT_ID = 20
AND     SALARY > 3000000;


-- TB ����
SELECT  *
FROM    TB_CLASS;



