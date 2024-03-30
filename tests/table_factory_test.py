from unittest import TestCase

from tests.test_fixtures import TestFixtures

from schema.factory.table_factory import TableFactory
from schema.models.table import Table
from schema.models.column import Column
class TableFactoryTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._factory = TableFactory()
        self._fixtures = TestFixtures()

    def test_create_table(self) -> None:
        data = self._fixtures.get_test_table_data()

        result = self._factory.create(data=data)

        self.assertIsInstance(result, Table)
        self.assertEqual(data['table_name'], result.table_name)
        self.assertEqual(data['schema'], result.schema)
        self.assertEqual(['ID'], result.primary_key)

        cols = result.columns
        self.assertTrue(2, len(cols))

        for key in cols:
            self.assertIsInstance(cols[key], Column)

        id_col = cols['ID']
        self.assertEqual('ID', id_col.name)
        self.assertEqual('INT', id_col.type)
        self.assertEqual(None, id_col.size)
        self.assertEqual(None, id_col.references)
        self.assertEqual(True, id_col.unique)
        self.assertEqual(False, id_col.nullable)
        self.assertEqual('', id_col.default)
        self.assertEqual('', id_col.check)

