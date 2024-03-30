import json
import logging

from simple_ddl_parser import DDLParser

from schema.factory.table_factory import TableFactory
from schema.models.table import Table
class TableRepository:

    def __init__(self, table_factory:TableFactory) -> None:
        self._factory = table_factory
        self._tables:dict[str, Table] = {}

    def load_from_string(self, source:str) -> bool:

        logging.info("load_from_string")

        data = json.loads(
            DDLParser(source, silent=False).run(
                json_dump=True,
                group_by_type=True
            )
        )

        # create table objects for each table using a factory
        for table_data in data['tables']:
            table = self._factory.create(table_data)
            self._tables[table.full_name] = table

    def get_table(self, name:str) -> dict:
        """
            name is schema.name of the table, if schema is specified
        """
        if name in self._tables:
            return self._tables[name]

        return None

    def get_table_names(self) -> list[str]:
        """
            return a list of "schema_name.table_name"
        """
        return self._tables.keys()
