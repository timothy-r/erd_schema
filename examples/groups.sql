CREATE TABLE item
  (
     ID       INT UNIQUE NOT NULL,
     NAME     NVARCHAR(400),
     PRIMARY KEY(ID),
     GROUP_ID INT,
     CONSTRAINT FK_group FOREIGN KEY (GROUP_ID)
    REFERENCES group(ID)
  )
    CREATE TABLE group
  (
     ID       INT PRIMARY KEY,
     NAME     NVARCHAR(400),
  )

  ;