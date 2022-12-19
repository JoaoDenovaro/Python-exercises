baixar sql connector
baixar outra biblioteca la
baixar XAMPP e Workbench
Configurar workbench para OP-

texto do workbech:

CREATE DATABASE INFINITY;

CREATE TABLE USERS(
	LOGIN VARCHAR(10) NOT NULL,
    FULL_NAME VARCHAR(30) NOT NULL
    );
    
SET GLOBAL LOCAL_INFILE = true;

LOAD DATA LOCAL INFILE 'c:\\temp\\users.csv'
INTO TABLE USERS FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n' IGNORE 1 ROWS;

SELECT * FROM USERS;