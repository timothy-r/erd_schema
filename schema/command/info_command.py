import logging
import json

from schema.command.command import Command
from schema.repository.table_repository import TableRepository

class InfoCommand(Command):

    def __init__(self, table_repo:TableRepository) -> None:
        self._table_repo = table_repo

    def __repr__(self) -> str:
        return f"{__class__.__name__}"

    def execute(self) -> None:
        """
            display parsed table data
        """

        for schema_table in self._table_repo.get_tables():
            print(f"Schema: {schema_table[0]}")
            print(f"Table: {schema_table[1]}")
            # next print table data
            table = self._table_repo.get_table(
                schema=schema_table[0],
                name=schema_table[1]
            )
            print(json.dumps(table, indent=4))
