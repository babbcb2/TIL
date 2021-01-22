-- 1. �л��̸��� �ּ����� ǥ���Ͻÿ�. ��, ��� ����� "�л� �̸�", "�ּ���"�� �ϰ�, ������ �̸����� �������� ǥ���ϵ��� �Ѵ�.

SELECT  STUDENT_NAME AS "�л��̸�",
        STUDENT_ADDRESS AS "�ּ���"
FROM    TB_STUDENT
ORDER BY 1;

-- 2. �������� �л����� �̸��� �ֹι�ȣ�� ���̰� ���� ������ ȭ�鿡 ����Ͻÿ�.
SELECT  STUDENT_NAME AS "�л��̸�",
        STUDENT_SSN AS "�ֹι�ȣ"
FROM    TB_STUDENT
WHERE   ABSENCE_YN = 'Y'
ORDER BY 2 DESC;


-- 3. �ּ����� �������� ��⵵�� �л��� �� 1900 ��� �й��� ���� �л����� �̸��� �й�, �ּҸ� �̸��� ������������ ȭ�鿡 ����Ͻÿ�. 
      ��, ���������� "�л��̸�","�й�", "������ �ּ�" �� ��µǵ��� �Ѵ�.

SELECT  STUDENT_NAME "�л��̸�", 
        STUDENT_NO "�й�",
        STUDENT_ADDRESS "������ �ּ�"
FROM TB_STUDENT 
WHERE ((STUDENT_ADDRESS LIKE '����%' OR STUDENT_ADDRESS LIKE '%���%')
AND TO_CHAR(ENTRANCE_DATE,'YYYY') LIKE '19__') 
ORDER BY 1,2,3


-- 4. ���� ���а� ���� �� ���� ���̰� ���� ������� �̸��� Ȯ���� �� �ִ� SQL ������ �ۼ��Ͻÿ�. 
--    (���а��� '�а��ڵ�'�� �а� ���̺�(TB_DEPARTMENT)�� ��ȸ�ؼ� ã�� ������ ����)

SELECT  PROFESSOR_NAME,
        PROFESSOR_SSN
FROM    TB_PROFESSOR
WHERE   DEPARTMENT_NO = '005'
ORDER BY 2;

SELECT  *
FROM    TB_DEPARTMENT
WHERE   DEPARTMENT_NAME = '���а�'
-- ���а� = 005

-- 5. 2004 �� 2 �б⿡ 'C3118100' ������ ������ �л����� ������ ��ȸ�Ϸ��� �Ѵ�.
--    ������ ���� �л����� ǥ���ϰ�, ������ ������ �й��� ���� �л����� ǥ���ϴ� ������ �ۼ��غ��ÿ�.
    
SELECT  STUDENT_NO,
        POINT
FROM    TB_STUDENT
JOIN    TB_GRADE USING(STUDENT_NO)
WHERE   TERM_NO = '200402' AND CLASS_NO = 'C3118100'
ORDER BY 2 DESC;


-- 6. �л� ��ȣ, �л� �̸�, �а� �̸��� �л� �̸����� �������� �����Ͽ� ����ϴ� SQL ���� �ۼ��Ͻÿ�.

SELECT  S.STUDENT_NO,
        S.STUDENT_NAME,
        D.DEPARTMENT_NAME
FROM    TB_DEPARTMENT_NO D
LEFT JOIN    TB_STUDENT S ON(S.DEPARTMENT_NO = D.DEPARTMENT_NO)
LEFT JOIN    TB_CLASS C ON (C.DEPARTMENT_NO = D.DEPARTMENT_NO)


