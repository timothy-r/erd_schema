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


    def test_table_properties_are_immutable(self) -> None:
        data = self._fixtures.get_test_table_data()

        table:Table = self._factory.create(data=data)

        with self.assertRaises(Exception) as context:
            table.table_name = 'new_table'

        with self.assertRaises(Exception) as context:
            table.schema = 'new_schema'

    def test_table_full_name_with_schema(self) -> None:
        data = self._fixtures.get_test_table_data()
        data["schema"] = 'new_schema'
        full_name = f'{data["schema"]}.{data["table_name"]}'

        table:Table = self._factory.create(data=data)
        self.assertEqual(full_name, table.full_name)

    def test_table_full_name_no_schema(self) -> None:
        data = self._fixtures.get_test_table_data()
        data["schema"] = ''
        full_name = data["table_name"]

        table:Table = self._factory.create(data=data)
        self.assertEqual(full_name, table.full_name)