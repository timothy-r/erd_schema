
class TestFixtures:

    def get_test_table_data(self) -> dict:

        return {
    "table_name": "item",
    "schema": "client_a",
    "primary_key": [
        "ID"
    ],
    "columns": [
        {
            "name": "ID",
            "type": "INT",
            "size": None,
            "references": None,
            "unique": True,
            "nullable": False,
            "default": "",
            "check": ""
        },
        {
            "name": "NAME",
            "type": "NVARCHAR",
            "size": 400,
            "references": "",
            "unique": False,
            "nullable": True,
            "default": "",
            "check": ""
        }
    ],
    "alter": {},
    "checks": [],
    "index": [],
    "partitioned_by": [],
    "constraints": {},
    "tablespace": ""
}

    def get_test_table_schema_sql(self) -> str:
        return """
        CREATE TABLE public.users
  (
     id       INT UNIQUE NOT NULL,
     EMAIL     NVARCHAR(400),
     PRIMARY KEY(ID)
  );
  """


    def get_test_table_sql(self) -> str:

        return """
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

    ALTER TABLE people ADD FOREIGN KEY (FAMILY_ID) REFERENCES FAMILY(ID)
  ;
        """
