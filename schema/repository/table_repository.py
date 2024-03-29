import json
import logging

from simple_ddl_parser import DDLParser

from schema.factory.table_factory import TableFactory
from schema.models.table import Table
class TableRepository:

    def __init__(self, table_factory:TableFactory) -> None:
        self._factory = table_factory
        self._tables:list[Table] = []

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
            self._tables.append(table)

    def get_table(self, name:str, schema:str = "") -> dict:

        for table in self._tables:
            # logging.info(table)

            if table.table_name == name:
                return table

    def get_tables(self) -> list[(str, str)]:
        """
            return a list of tuples of (schema_name, table_name)
        """
        return [
            (table.schema, table.table_name) for table in self._tables
        ]
