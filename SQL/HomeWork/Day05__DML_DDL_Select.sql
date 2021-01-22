-- 1. ���������� �����Ͽ� ���̺��� �����Ͻÿ�.
CREATE TABLE CUSTOMERS(
    CNO     NUMBER(5) PRIMARY KEY,
    CNAME   VARCHAR2(10) NOT NULL,
    ADDRESS VARCHAR2(50) NOT NULL,
    EMAIL   VARCHAR2(20) NOT NULL,
    PHONE   VARCHAR2(20) NOT NULL
)
SELECT *
FROM    CUSTOMERS
DROP TABLE CUSTOMERS

CREATE TABLE ORDERS(
    ORDERNO     NUMBER(10) PRIMARY KEY,
    ORDERDATE   DATE DEFAULT SYSDATE NOT NULL,
    ADDRESS     VARCHAR2(50) NOT NULL,
    PHONE       VARCHAR2(20) NOT NULL,
    STATUS      VARCHAR2(20) NOT NULL CHECK(STATUS IN ('�����Ϸ�','�����','��ۿϷ�')),
    CNO         NUMBER(5) NOT NULL,
    FOREIGN KEY (CNO) REFERENCES CUSTOMERS (CNO)
)
SELECT  *
FROM    ORDERS
DROP TABLE ORDERS


CREATE TABLE PRODUCTS(
    PNO         NUMBER(5) PRIMARY KEY,
    PNAME       VARCHAR2(20) NOT NULL,
    COST        NUMBER(8) DEFAULT 0 NOT NULL,
    STOCK       NUMBER(5) DEFAULT 0 NOT NULL 
)
SELECT  *
FROM    PRODUCTS
DROP TABLE PRODUCTS



CREATE TABLE ORDERDETAIL(
    ORDERNO     NUMBER(10) PRIMARY KEY,
    PNO         NUMBER(5) NOT NULL,
    QTY         NUMBER(5) DEFAULT 0,
    COST        NUMBER(5) DEFAULT 0,
    FOREIGN KEY (ORDERNO) REFERENCES ORDERS (ORDERNO),
    FOREIGN KEY (PNO) REFERENCES PRODUCTS (PNO)
)
SELECT  *
FROM    ORDERDETAIL
DROP TABLE ORDERDETAIL

-- 2. PRODUCTS ���̺� ���� �����͸� �Է��Ͻÿ�.
INSERT INTO PRODUCTS VALUES(1001, '�����', 1000, 200)
INSERT INTO PRODUCTS VALUES(1002, '�����', 1500, 500)
INSERT INTO PRODUCTS VALUES(1003, '������', 2000, 350)
INSERT INTO PRODUCTS VALUES(1004, '������', 2000, 700)
INSERT INTO PRODUCTS VALUES(1005, '��ī�ݶ�', 1800, 550)
INSERT INTO PRODUCTS VALUES(1006, 'ȯŸ', 1600, 300)

SELECT  *
FROM    PRODUCTS


-- 3. customers ���̺� ���� �����͸� �Է��Ͻÿ�.
INSERT INTO CUSTOMERS VALUES(101, '��ö��', '���� ������', 'cskim@naver.com', '899-6666')
INSERT INTO CUSTOMERS VALUES(102, '�̿���', '�λ� ����', 'yhlee@empal.com', '355-8882')
INSERT INTO CUSTOMERS VALUES(103, '������', '���� ������', 'jkchoi@gmail.com', '852-5764')
INSERT INTO CUSTOMERS VALUES(104, '����ȣ', '���� ȫ����', 'jhkang@hanmail.com', '559-7777')
INSERT INTO CUSTOMERS VALUES(105, '�κ���', '���� ���ε�', 'bgmin@hotmail.com', '559-8741')
INSERT INTO CUSTOMERS VALUES(106, '���μ�', '���� �ϱ�', 'msoh@microsoft.com', '542-9988')
SELECT  *
FROM    CUSTOMERS

-- 4. ������ ���� �ֹ� ������ orders ���̺�� orderdetail ���̺� �Է��Ͻÿ�. 
--    cno�� customers ���̺��� �˻��Ͽ� �Է��� ��. orders�� 1��, orderdetail�� 1���� �Է��Ѵ�.
--    ����ö��(101)�� 3������ �����(1001)�� ���� 1000���� 50�� �ֹ��Ͽ���."

SELECT *
FROM    CUSTOMERS

INSERT INTO ORDERS VALUES (1 , SYSDATE - 3 , '���� ������', '899-6666', '�����Ϸ�', 101)
INSERT INTO ORDERDETAIL VALUES (1, 1001, 50, 100)

SELECT  *
FROM    ORDERS
SELECT  *
FROM    ORDERDETAIL



-- 5.���� ���� �ֹ� �������� �ش� ��ǰ(products)�� ���(stock)�� �����Ͻÿ�.

UPDATE  PRODUCTS
SET     STOCK = 200 - 50
WHERE   PNO = 1001

SELECT  *
FROM    PRODUCTS

-- 6. ������ ���� �ֹ� ������ orders ���̺�� orderdetail ���̺� �Է��Ͻÿ�. cno�� customers ���̺��� �˻��Ͽ� �Է��� ��.
--    orders�� 1��, orderdetail�� 2���� �Է��Ѵ�.
--    ���̿���(102)�� ��Ʋ���� �����(1002)�� ���� 1500���� 100��, ������(1003)�� ���� 2000���� 150���ֹ��Ͽ���.��

INSERT INTO ORDERS VALUES (2 , SYSDATE - 2 , '�λ� ������', '337-5000', '�����Ϸ�', 102)
INSERT INTO ORDERDETAIL VALUES ( , 1002, 100, 1500)
INSERT INTO ORDERDETAIL VALUES (2, 1003, 150, 2000)

DELETE
FROM    ORDERDETAIL
WHERE   ORDERNO = 2

SELECT  *
FROM    ORDERDETAIL
