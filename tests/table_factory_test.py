from unittest import TestCase

from schema.factory.table_factory import TableFactory
from schema.models.table import Table

class TableFactoryTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._factory = TableFactory()

    def test_get_table(self) -> None:
        data = self._get_test_data()

        result = self._factory.create(data=data)

        self.assertIsInstance(result, Table)

    def _get_test_data(self) -> dict:

        return {
    "table_name": "item",
    "schema": "",
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