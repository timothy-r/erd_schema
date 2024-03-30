from dataclasses import dataclass, field

from schema.models.column import Column
from schema.models.relation import Relation, RelationType

@dataclass(frozen=True)
class Table:
    table_name: str
    schema: str
    primary_key: list

    columns: dict[str, Column]

    alter: dict = field(default_factory=dict)
    checks: list = field(default_factory=list)
    index: list = field(default_factory=list)
    partitioned_by: list = field(default_factory=list)
    tablespace: str = ""
    constraints: dict = field(default_factory=dict)

    @property
    def full_name(self):
        return self._table_full_name(table_name=self.table_name, schema=self.schema)

    # "constraints": {
    #     "references": [
    #         {
    #             "table": "group",
    #             "columns": [
    #                 "ID"
    #             ],
    #             "schema": "public",
    #             "on_delete": null,
    #             "on_update": null,
    #             "deferrable_initially": null,
    #             "name": "GROUP_ID",
    #             "constraint_name": "FK_group"
    #         }
    #     ]
    # },
    # alter = {
    #         "columns": [
    #             {
    #             "name": "GROUP_ID",
    #             "constraint_name": "FK_group",
    #             "references": {
    #                 "table": "group",
    #                 "schema": "public",
    #                 "on_delete": None,
    #                 "on_update": None,
    #                 "deferrable_initially": None,
    #                 "column": "id"
    #                 }
    #             }
    #         ]
    # }

    def get_references(self):
        """
            get the table_names and columns of this table that reference another table
            {"from": "this.table.column_name", "to":"other.table.full_name" }
        """
        relations = []

        if "columns" in self.alter:
            for col in self.alter["columns"]:
                if "references" in col:
                    # generate table name from table & schema values
                    other_table_name = self._table_full_name(
                        table_name=col["references"]['table'],
                        schema=col["references"]["schema"]
                    )
                    other_col_name = col["references"]["column"]
                    this_col_name = col["name"]
                    relations.append(
                        Relation(
                            from_table=self.full_name,
                            from_col=this_col_name,
                            to_table=other_table_name,
                            to_col=other_col_name,
                            # types depend on column nullability
                            from_type=RelationType.MANY,
                            to_type=RelationType.ONE
                        )
                    )

        return relations


    def references(self, table_name: str) -> bool:
        """
            table name format is "schema"."table"
            return True if this table has a reference to the parameter table + schema
        """
        pass

    def _table_full_name(self, table_name:str, schema:str) -> str:
        if not schema:
            return table_name

        return f"{schema}.{table_name}"