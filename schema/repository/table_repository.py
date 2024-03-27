import json
import logging

from simple_ddl_parser import DDLParser

class TableRepository:

    def __init__(self) -> None:
        self._tables = []

    def load_from_string(self, source:str) -> bool:

        logging.info("load_from_string")

        data = json.loads(
            DDLParser(source, silent=False).run(
                json_dump=True,
                group_by_type=True
            )
        )

        # create table objects for each table using a factory
        self._tables = data['tables']

    def get_table(self, name:str, schema:str = None) -> dict:

        for table in self._tables:
            if table['table_name'] == name:
                return table

    def get_tables(self) -> list[(str, str)]:
        """
            return a list of tuples of (schema_name, table_name)
        """
        return [
            (table['schema'], table['table_name']) for table in self._tables
        ]
