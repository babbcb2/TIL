
-- 1. ������а�(�а��ڵ� 002) �л����� �й��� �̸�, ���� �⵵�� ���� �⵵�� ���� ������ ǥ���ϴ� SQL ������ �ۼ��Ͻÿ�.
--    ( ��, ����� "�й�", "�̸�", "���г⵵" ��ǥ�õǵ��� ����.)

SELECT  STUDENT_NO AS �й�,
        STUDENT_NAME AS �̸�,
        ENTRANCE_DATE AS ���г⵵
FROM    TB_STUDENT
WHERE   DEPARTMENT_NO = 002
ORDER BY ���г⵵ ;


-- 2. �� ������б��� ���� �� �̸��� �� ���ڰ� �ƴ� ������ �Ѹ� �ִٰ� �Ѵ�. 
--    �� ������ �̸��� �ֹι�ȣ�� ȭ�鿡 ����ϴ� SQL ������ �ۼ��� ����.
--    (* �̶� �ùٸ��� �ۼ��� SQL ������ ��� ���� ����� �ٸ��� ���� �� �ִ�. ������ �������� �����غ� ��)

SELECT  PROFESSOR_NAME,
        PROFESSOR_SSN
FROM    TB_PROFESSOR
WHERE   LENGTH(PROFESSOR_NAME) > 3 OR LENGTH(PROFESSOR_NAME) < 3 ;


-- 4. �������� �̸� �� ���� ������ �̸��� ����ϴ� SQL ������ �ۼ��Ͻÿ�. 
--    ��� ����� ?�̸�? �� �������� ����. (���� 2 ���� ���� ������ ���ٰ� �����Ͻÿ�)

SELECT SUBSTR(PROFESSOR_NAME, 2, 2) AS "�̸�"
FROM TB_PROFESSOR

-- 5. �� ������б��� ����� �����ڸ� ���Ϸ��� �Ѵ�. ��� ã�Ƴ� ���ΰ�?
--    �̶�, 19 �쿡 �����ϸ� ����� ���� ���� ������ �����Ѵ�.

SELECT  STUDENT_NO,
        STUDENT_NAME AS �����,
        TO_CHAR(TO_DATE(SUBSTR(STUDENT_SSN,1,6), 'RRMMDD'),'YYYY/MM/DD') AS "�����",
        TO_CHAR(ENTRANCE_DATE, 'RRRR/MM/DD') AS "������",
        TRUNC (MONTHS_BETWEEN (ENTRANCE_DATE, TO_DATE(SUBSTR(STUDENT_SSN,1,6),'RRMMDD')) / 12) AS "����"
FROM    TB_STUDENT
WHERE   TRUNC (MONTHS_BETWEEN (ENTRANCE_DATE, TO_DATE(SUBSTR(STUDENT_SSN,1,6),'RRMMDD')) / 12) > 19; 


-- 6. 2020 �� ũ���������� ���� �����ΰ�?
SELECT  TO_CHAR(TO_DATE('20201225','YYYYMMDD'),'DAY')
FROM    DUAL;


-- 7. TO_DATE('99/10/11','YY/MM/DD'), TO_DATE('49/10/11','YY/MM/DD') �� ���� �� �� ��� �� ���� �ǹ��ұ�?
--    �� TO_DATE('99/10/11','RR/MM/DD'), TO_DATE('49/10/11','RR/MM/DD') �� ���� �� �� �� �� �� ���� �ǹ�����?
SELECT  TO_CHAR(TO_DATE('99/10/11', 'YY/MM/DD'), 'YYYY"��" MM"��" DD"��"'),
        TO_CHAR(TO_DATE('49/10/11', 'YY/MM/DD'), 'YYYY"��" MM"��" DD"��"'),
        TO_CHAR(TO_DATE('99/10/11', 'RR/MM/DD'), 'RRRR"��" MM"��" DD"��"'),
        TO_CHAR(TO_DATE('49/10/11', 'RR/MM/DD'), 'RRRR"��" MM"��" DD"��"')
FROM    DUAL;


-- 8. �� ������б��� 2000 �⵵ ���� �����ڵ��� �й��� A �� �����ϰ� �Ǿ��ִ�.
--    2000 �⵵ ���� �й��� ���� �л����� �й��� �̸��� �����ִ� SQL ������ �ۼ��Ͻÿ�.
    
SELECT  STUDENT_NO AS "�й�",
        STUDENT_NAME AS "�̸�",
        TO_NUMBER(TO_CHAR(ENTRANCE_DATE, 'YYYY'))
FROM    TB_STUDENT
WHERE   TO_NUMBER(TO_CHAR(ENTRANCE_DATE, 'YYYY')) < 2000 ;


-- 9. �й��� A517178 �� �ѾƸ� �л��� ���� �� ������ ���ϴ� SQL ���� �ۼ��Ͻÿ�. ��,
      �̶� ��� ȭ���� ����� "����" �̶�� ������ �ϰ�, ������ �ݿø��Ͽ� �Ҽ��� ���� ���ڸ������� ǥ���Ѵ�.

SELECT  ROUND(AVG(POINT), 1) AS "����"
FROM    TB_GRADE
WHERE   STUDENT_NO = 'A517178'

-- 10. �а��� �л����� ���Ͽ� "�а���ȣ", "�л���(��)" �� ���·� ����� ����� ������� ��µǵ��� �Ͻÿ�.

SELECT  DEPARTMENT_NO AS "�а���ȣ",
        COUNT(*) "�л���(��)"
FROM    TB_STUDENT
GROUP BY DEPARTMENT_NO
ORDER BY 1 ;


-- 11. ���� ������ �������� ���� �л��� ���� �� �� ���� �Ǵ� �˾Ƴ��� SQL ���� �ۼ��Ͻÿ�.

SELECT  COUNT(*)
FROM    TB_STUDENT
GROUP BY COACH_PROFESSOR_NO
HAVING   COACH_PROFESSOR_NO IS NULL


-- 12. �й��� A112113 �� ���� �л��� �⵵ �� ������ ���ϴ� SQL ���� �ۼ��Ͻÿ�. 
--     ��,�̶� ��� ȭ���� ����� "�⵵", "�⵵ �� ����" �̶�� ������ �ϰ�,
--     ������ �ݿø��Ͽ� �Ҽ��� ���� �� �ڸ������� ǥ���Ѵ�.

SELECT  TO_NUMBER(SUBSTR(TERM_NO,1,4)) �⵵, ROUND(AVG(POINT),1)
FROM    TB_GRADE
WHERE   STUDENT_NO = 'A112113'
GROUP BY    SUBSTR(TERM_NO,1,4)


-- 13. �а� �� ���л� ���� �ľ��ϰ��� �Ѵ�. �а� ��ȣ�� ���л� ���� ǥ���ϴ� SQL ������ �ۼ��Ͻÿ�.

SELECT  DEPARTMENT_NO, COUNT(*)
FROM  TB_STUDENT
WHERE ABSENCE_YN = 'Y'
GROUP BY DEPARTMENT_NO
ORDER BY 1;


SELECT  DEPARTMENT_NO AS "�а��ڵ��",
        SUM(CASE WHEN ABSENCE_YN = 'Y'
                 THEN 1 
                 else 0
            END) AS "���л� ��"
FROM  TB_STUDENT
GROUP BY DEPARTMENT_NO
ORDER BY 1;


-- 14. �� ���б��� �ٴϴ� ��������(��٣���) �л����� �̸��� ã���� �Ѵ�. � SQL ������ ����ϸ� �����ϰڴ°�?

SELECT  STUDENT_NAME, COUNT(*)
FROM    TB_STUDENT
GROUP BY STUDENT_NAME
HAVING  COUNT(*) > 1
ORDER BY 1;


15. �й��� A112113 �� ���� �л��� �⵵, �б� �� ������ �⵵ �� ���� ���� , �������� ���ϴ� SQL ���� �ۼ��Ͻÿ�.
    (��, ������ �Ҽ��� 1 �ڸ������� �ݿø��Ͽ� ǥ���Ѵ�.)

SELECT  TO_NUMBER(SUBSTR(TERM_NO,1,4)) AS "�⵵",
        TO_NUMBER(SUBSTR(TERM_NO,5,2)) AS "�б�",
        ROUND(AVG(POINT),1) AS "����"
FROM    TB_GRADE
WHERE   STUDENT_NO = 'A112113'
GROUP BY ROLLUP (SUBSTR(TERM_NO,1,4), STUBSTR(TERM_NO,5,2));


