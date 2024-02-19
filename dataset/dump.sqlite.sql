-- TABLE
CREATE TABLE "questions" (ID integer primary key, question varchar(100), choices TEXT, correct varchar(100), imageUrl varchar(100));
CREATE TABLE "user" (ID integer primary key, name varchar(20), email text , highscore INTEGER NOT NULL DEFAULT '0');
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
