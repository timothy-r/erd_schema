from dataclasses import dataclass, field

from schema.models.column import Column
@dataclass(frozen=True)
class Table:
    table_name: str
    schema: str
    primary_key: list

    columns: list[Column]

    alter: dict = field(default_factory=dict)
    checks: list = field(default_factory=list)
    index: list = field(default_factory=list)
    partitioned_by: list = field(default_factory=list)
    tablespace: str = ""
    constraints: dict = field(default_factory=dict)

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