from dataclasses import dataclass

from schema.models.column import Column
@dataclass
class Table:
    name: str
    schema: str
    primary_key: list

    columns: list[Column]

    alter: dict
    checks: list
    index: list
    partitioned_by: list
    tablespace: str
    constraints: dict

    # "constraints": {
    #     "references": [
    #         {
    #             "table": "group",
    #             "columns": [
    #                 "ID"
    #             ],
    #             "schema": null,
    #             "on_delete": null,
    #             "on_update": null,
    #             "deferrable_initially": null,
    #             "name": "GROUP_ID",
    #             "constraint_name": "FK_group"
    #         }
    #     ]
    # },

    def references(self, schema:str, table: str) -> bool:
        """
            return True if this table has a reference to the parameter table + schema
        """
        pass