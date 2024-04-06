
class TestFixtures:

    def get_test_table_data(self, name:str="item", schema:str="public") -> dict:

        return {
    "table_name": name,
    "schema": schema,
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
        },
        {
            "name": "GROUP_ID",
            "type": "INT",
            "size": None,
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

    def get_test_table_data_with_alter_relations(self, name:str="item", schema:str="public") -> dict:

        table_data = self.get_test_table_data(name=name, schema=schema)
        # table_data["constraints"] =  {
        #     "references": [
        #     {
        #         "table": "group",
        #         "columns": [
        #             "ID"
        #         ],
        #         "schema": "public",
        #         "on_delete": None,
        #         "on_update": None,
        #         "deferrable_initially": None,
        #         "name": "GROUP_ID",
        #         "constraint_name": "FK_group"
        #     }
        #     ]
        # }

        table_data["alter"] =  {
            "columns": [
                {
                "name": "group_id",
                "constraint_name": "FK_group",
                "references": {
                    "table": "group",
                    "schema": "public",
                    "on_delete": None,
                    "on_update": None,
                    "deferrable_initially": None,
                    "column": "id"
                    }
                }
            ]
        }
        return table_data

    def get_test_table_data_with_constraint_relations(self, name:str="item", schema:str="public") -> dict:

        table_data = self.get_test_table_data(name=name, schema=schema)
        table_data["constraints"] =  {
            "references": [
            {
                "table": "group",
                "columns": [
                    "id"
                ],
                "schema": "public",
                "on_delete": None,
                "on_update": None,
                "deferrable_initially": None,
                "name": "group_id",
                "constraint_name": "FK_group"
            }
            ]
        }

        # table_data["alter"] =  {
        #     "columns": [
        #         {
        #         "name": "group_id",
        #         "constraint_name": "FK_group",
        #         "references": {
        #             "table": "group",
        #             "schema": "public",
        #             "on_delete": None,
        #             "on_update": None,
        #             "deferrable_initially": None,
        #             "column": "id"
        #             }
        #         }
        #     ]
        # }
        return table_data

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
