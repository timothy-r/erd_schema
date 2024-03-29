import logging
import json
import jsonpickle

from schema.command.command import Command
from schema.repository.table_repository import TableRepository

class InfoCommand(Command):
    """
        displays information on the cli about Tables read from an SQL source file
    """
    def __init__(self, table_repo:TableRepository) -> None:
        self._table_repo = table_repo

    def __repr__(self) -> str:
        return f"{__class__.__name__}"

    def execute(self) -> None:
        """
            display parsed table data
        """
        for table_name in self._table_repo.get_table_names():
            # print(f"Schema: {schema_table[0]}")
            print(f"Table: {table_name}")

            # next print table data
            table = self._table_repo.get_table(name=table_name)

            print(jsonpickle.encode(table, unpicklable=False, indent=4))
