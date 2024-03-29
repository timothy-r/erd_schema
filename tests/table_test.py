from unittest import TestCase

from tests.test_fixtures import TestFixtures
from schema.factory.table_factory import TableFactory

from schema.models.table import Table
from schema.models.column import Column

class TableTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._factory = TableFactory()
        self._fixtures = TestFixtures()


    def test_table_properties_are_immutable(self):
        data = self._fixtures.get_test_table_data()

        table:Table = self._factory.create(data=data)

        with self.assertRaises(Exception) as context:
            table.table_name = 'new_table'

        with self.assertRaises(Exception) as context:
            table.schema = 'new_schema'