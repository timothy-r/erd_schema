CREATE TABLE people
  (
     id       INT UNIQUE NOT NULL,
     EMAIL     NVARCHAR(400),
     PRIMARY KEY(ID),
     FAMILY_ID INT
  )
    CREATE TABLE car
  (
     id       INT PRIMARY KEY,
     NAME     NVARCHAR(400),
     OWNER_ID INT,
     CONSTRAINT fk_category FOREIGN KEY (OWNER_ID)
                         REFERENCES people(ID)
  )

      CREATE TABLE FAMILY
  (
     id       INT PRIMARY KEY,
     NAME     NVARCHAR(400)
  )

ALTER TABLE people ADD CONSTRAINT family_fk FOREIGN KEY (FAMILY_ID) REFERENCES FAMILY(ID)

  ;